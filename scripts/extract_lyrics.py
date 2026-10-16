#!/usr/bin/env python
"""
Extrae la letra (con tiempos) desde un MusicXML/MXL para el reproductor de letras.

Calcula el instante de cada sílaba a partir de compases, divisions y cambios de tempo
(`<sound tempo>`), desenrollando repeticiones y casillas (voltas) simples. La salida es
una lista de líneas: [{"t": segundos, "text": "..."}], lista para `letras` en data.json.

Uso:
    python scripts/extract_lyrics.py "static/media/X.mxl" --part Soprano --offset 0.3
    python scripts/extract_lyrics.py "static/media/X.mxl" --part auto --apply 26
    python scripts/extract_lyrics.py "static/media/X.mxl" --list-parts
"""
import argparse
import io
import json
import os
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

END_PUNCT = re.compile(r'[,.;:!?¡¿…]$')
LABEL = re.compile(r'^\s*(?:C|Coro|Estribillo|A|Ant[ií]fona|\d+)\s*[.:)]\s*', re.IGNORECASE)
VOCALISE = re.compile(r'^[\s.\-–…]*(m+|mm+|o+h*|a+h*|u+|na|la|\.{0,3})[\s.\-–…]*$', re.IGNORECASE)


def load_root(path):
    if path.lower().endswith('.mxl'):
        z = zipfile.ZipFile(path)
        name = [n for n in z.namelist() if n.endswith('.xml') and not n.startswith('META')][0]
        return ET.fromstring(z.read(name))
    return ET.parse(path).getroot()


def parts_info(root):
    names = {p.get('id'): (p.findtext('part-name') or '') for p in root.findall('part-list/score-part')}
    out = []
    for part in root.findall('part'):
        count = sum(1 for _ in part.iter('lyric'))
        out.append((part.get('id'), names.get(part.get('id'), ''), count))
    return out


def unroll_measures(measures):
    """Devuelve la lista de (indice_compas, medida, pasada) respetando repeticiones y casillas simples."""
    order = []
    i = 0
    start_rep = 0
    pass_no = 1
    guard = 0
    while i < len(measures) and guard < 10000:
        guard += 1
        m = measures[i]
        ending = None
        for b in m.findall('barline'):
            e = b.find('ending')
            if e is not None and e.get('type') == 'start':
                ending = [int(x) for x in re.findall(r'\d+', e.get('number', '1'))]
        if ending is not None and pass_no not in ending:
            j = i
            while j < len(measures):
                done = False
                for b in measures[j].findall('barline'):
                    e = b.find('ending')
                    if e is not None and e.get('type') in ('stop', 'discontinue'):
                        done = True
                if done:
                    break
                j += 1
            i = j + 1
            continue
        for b in m.findall('barline'):
            r = b.find('repeat')
            if r is not None and r.get('direction') == 'forward':
                start_rep = i
        order.append((i, m, pass_no))
        back = False
        for b in m.findall('barline'):
            r = b.find('repeat')
            if r is not None and r.get('direction') == 'backward':
                back = True
        if back and pass_no == 1:
            pass_no = 2
            i = start_rep
            continue
        if back:
            pass_no = 1
        i += 1
    return order


def read_tempo_map_from_root(root):
    """Mapa {indice_compas: [(beat, bpm), ...]} combinando todas las partes de una partitura."""
    tmap = {}
    for part in root.findall('part'):
        divisions = 1
        for idx, m in enumerate(part.findall('measure')):
            pos = 0
            for el in m:
                if el.tag == 'attributes':
                    d = el.findtext('divisions')
                    if d:
                        divisions = int(d)
                elif el.tag in ('direction', 'sound'):
                    s = el if el.tag == 'sound' else el.find('sound')
                    if s is not None and s.get('tempo'):
                        entry = (pos / divisions, float(s.get('tempo')))
                        lst = tmap.setdefault(idx, [])
                        if entry not in lst:
                            lst.append(entry)
                elif el.tag == 'note':
                    if el.find('chord') is None and el.find('grace') is None:
                        pos += int(el.findtext('duration') or 0)
                elif el.tag == 'backup':
                    pos -= int(el.findtext('duration') or 0)
                elif el.tag == 'forward':
                    pos += int(el.findtext('duration') or 0)
    return tmap


def read_tempo_map(path):
    return read_tempo_map_from_root(load_root(path))


def select_parts(root, part_ref):
    """Devuelve lista de elementos <part> con letras según part_ref ('auto' combina partes vocales)."""
    infos = parts_info(root)
    name_by_id = {pid: pname for pid, pname, _ in infos}
    all_parts = {p.get('id'): p for p in root.findall('part')}

    if not part_ref or part_ref.lower() == 'auto':
        vocal_ids = [pid for pid, _, cnt in infos if cnt > 0]
        if not vocal_ids:
            vocal_ids = [infos[0][0]]
        return [all_parts[pid] for pid in vocal_ids]

    refs = [r.strip() for r in part_ref.split(',') if r.strip()]
    chosen = []
    for ref in refs:
        for pid, pname, _ in infos:
            if ref in (pid, pname) or ref.lower() in pname.lower():
                if all_parts[pid] not in chosen:
                    chosen.append(all_parts[pid])
                break
    if not chosen:
        raise SystemExit('Parte no encontrada: %s. Partes: %s' % (part_ref, infos))
    return chosen


def extract(path, part_ref='auto', offset=0.0, verse=None, gap_split=2.0, tempo_map=None):
    root = load_root(path)
    if tempo_map is None:
        tempo_map = read_tempo_map_from_root(root)

    parts = select_parts(root, part_ref)
    primary_measures = parts[0].findall('measure')
    parts_measures = [p.findall('measure') for p in parts]
    order = unroll_measures(primary_measures)

    divisions_by_part = [1] * len(parts)
    tempo = 120.0
    t_measure_start = 0.0
    syllables = []  # (time, text, syllabic, verse_number, pass_no)

    for m_idx, primary_m, pass_no in order:
        # Actualizar divisions de cada parte en este compás
        for p_i, p_measures in enumerate(parts_measures):
            if m_idx < len(p_measures):
                for attr in p_measures[m_idx].findall('attributes'):
                    d = attr.findtext('divisions')
                    if d:
                        divisions_by_part[p_i] = int(d)

        # Elegir la primera parte que tenga letras cantadas (no mmm/u) en este compás; si ninguna, la primera con cualquier letra
        chosen_p_idx = 0
        for p_i, p_measures in enumerate(parts_measures):
            if m_idx >= len(p_measures):
                continue
            m_cand = p_measures[m_idx]
            has_words = False
            for lyr in m_cand.iter('lyric'):
                t_cand = ''.join((c.text or '') for c in lyr if c.tag in ('text', 'elision')).strip()
                t_clean = LABEL.sub('', t_cand).strip()
                if t_clean and not VOCALISE.match(t_clean):
                    has_words = True
                    break
            if has_words:
                chosen_p_idx = p_i
                break

        m = parts_measures[chosen_p_idx][m_idx]
        divisions = divisions_by_part[chosen_p_idx]

        pos = 0
        max_pos = 0
        notes = []
        last_onset = 0
        for el in m:
            tag = el.tag
            if tag == 'note':
                dur = int(el.findtext('duration') or 0)
                is_chord = el.find('chord') is not None
                onset = last_onset if is_chord else pos
                if not is_chord:
                    last_onset = pos
                    if el.find('grace') is None:
                        pos += dur
                notes.append((onset, dur, el))
            elif tag == 'backup':
                pos -= int(el.findtext('duration') or 0)
            elif tag == 'forward':
                pos += int(el.findtext('duration') or 0)
            max_pos = max(max_pos, pos)

        # Si el compás en esta parte estaba vacío de duración, calcular max_pos desde la primera parte
        if max_pos == 0 and m is not primary_m:
            div0 = divisions_by_part[0]
            p0 = 0
            mp0 = 0
            for el in primary_m:
                if el.tag == 'note' and el.find('chord') is None and el.find('grace') is None:
                    p0 += int(el.findtext('duration') or 0)
                elif el.tag == 'backup':
                    p0 -= int(el.findtext('duration') or 0)
                elif el.tag == 'forward':
                    p0 += int(el.findtext('duration') or 0)
                mp0 = max(mp0, p0)
            max_pos = int(round(mp0 * divisions / div0))

        events = [(int(round(b * divisions)), bpm) for b, bpm in tempo_map.get(m_idx, [])]

        def time_at(p, _events=sorted(events), _t0=t_measure_start, _tempo0=tempo, _div=divisions):
            t, cur, last = _t0, _tempo0, 0
            for ep, et in _events:
                if ep >= p:
                    break
                t += (ep - last) / _div * 60.0 / cur
                last, cur = ep, et
            return t + (p - last) / _div * 60.0 / cur

        for onset, dur, el in notes:
            if el.find('rest') is not None:
                continue
            for lyr in el.findall('lyric'):
                texts = []
                for child in lyr:
                    if child.tag == 'text':
                        texts.append(child.text or '')
                    elif child.tag == 'elision':
                        texts.append(child.text or ' ')
                txt = ''.join(texts).replace('\xa0', ' ')
                if not txt.strip():
                    continue
                syllables.append((time_at(onset), txt, lyr.findtext('syllabic') or 'single',
                                  lyr.get('number', '1'), pass_no))

        measure_len = max_pos
        t_measure_start = time_at(measure_len)
        for ep, et in sorted(events):
            tempo = et

    by_pass = any(p > 1 for *_, p in syllables)
    chosen = []
    if by_pass:
        for t, txt, syl, num, p in syllables:
            if num == str(p) or (num == '1' and not any(s[3] == str(p) for s in syllables)):
                chosen.append((t, txt, syl))
    else:
        chosen = [(t, txt, syl) for t, txt, syl, num, p in syllables if verse is None or num == str(verse)]

    lines, cur_text, cur_t, prev_end_t, prev_syl = [], '', None, None, 'single'
    for t, txt, syl in chosen:
        if cur_t is None:
            cur_t = t
        elif (prev_end_t is not None and prev_syl in ('end', 'single')
              and (t - prev_end_t) > gap_split and cur_text.strip()):
            lines.append({'t': round(cur_t + offset, 2), 'text': cur_text.strip()})
            cur_text, cur_t = '', t
        cur_text += txt
        if syl in ('end', 'single'):
            cur_text += ' '
            if END_PUNCT.search(txt.strip()):
                lines.append({'t': round(cur_t + offset, 2), 'text': cur_text.strip()})
                cur_text, cur_t = '', None
        prev_end_t = t
        prev_syl = syl

    if cur_text.strip():
        lines.append({'t': round((cur_t or 0) + offset, 2), 'text': cur_text.strip()})
    return clean_lines(lines), round(t_measure_start + offset, 2)


def clean_lines(lines):
    """Quita etiquetas ("C.", "A.", "1."), puntos suspensivos iniciales y vocalizaciones (mmm, ah...)."""
    out = []
    for ln in lines:
        text = ln['text'].replace('\xa0', ' ')
        text = LABEL.sub('', text).lstrip('.…- ').strip()
        text = re.sub(r'\s{2,}', ' ', text)
        if not text or VOCALISE.match(text):
            continue
        out.append({'t': ln['t'], 'text': text[0].upper() + text[1:]})
    return out


def apply_to_data_json(song_id, lines, synced):
    """Escribe {'sincronizada': bool, 'lineas': [...]} en data.json conservando su formato."""
    path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data.json')
    data = json.loads(io.open(path, encoding='utf-8', newline='').read())
    for song in data:
        if song.get('id') == int(song_id):
            song['letras'] = {'sincronizada': synced, 'lineas': lines}
            break
    else:
        raise SystemExit('No existe la cancion con id %s' % song_id)
    text = json.dumps(data, indent=4, ensure_ascii=False).replace('\n', '\r\n')
    io.open(path, 'w', encoding='utf-8', newline='').write(text)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('path')
    ap.add_argument('--part', default='auto')
    ap.add_argument('--offset', type=float, default=0.0)
    ap.add_argument('--verse', default=None)
    ap.add_argument('--gap', type=float, default=2.0)
    ap.add_argument('--tempo-from', default=None,
                    help='Partitura (p.ej. la Cantamus) de la que tomar el mapa de tempos')
    ap.add_argument('--list-parts', action='store_true')
    ap.add_argument('--apply', metavar='ID', default=None, help='Guardar en data.json para esta cancion (id)')
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding='utf-8')
    if a.list_parts:
        for p in parts_info(load_root(a.path)):
            print(p)
        return
    tmap = read_tempo_map(a.tempo_from) if a.tempo_from else None
    lines, total = extract(a.path, a.part, a.offset, a.verse, a.gap, tmap)
    if a.apply:
        apply_to_data_json(a.apply, lines, True)
        print('Letra sincronizada guardada en data.json para id', a.apply, '(%d lineas)' % len(lines))
        return
    print(json.dumps({'duracion_partitura': total, 'lineas': lines}, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
