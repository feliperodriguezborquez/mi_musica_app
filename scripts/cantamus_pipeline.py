#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cantamus_pipeline.py - Pipeline Universal de Procesamiento MusicXML para Cantamus
----------------------------------------------------------------------------------
Procesa partituras en formato MusicXML (.musicxml, .xml, .mxl) y MuseScore (.mscz)
garantizando compatibilidad estricta con el motor de sintesis coral Cantamus:

1. Reindexacion correlativa P1..Pn y monofonia estricta (voz 1, sin acordes/divisi).
2. Deteccion y filtrado de cuerdas vocales (excluye contrabajo, guitarras, etc.).
3. Propagacion multicuerda de tempo (Baking) en todas las voces.
4. Curvas matematicas de ritardando/accelerando (Linear, Ease-In, Ease-Out) al final y en pasajes intermedios.
5. Duplicacion de duracion en calderones (<fermata> -> 50% BPM).
6. Normalizacion fonetica estricta (fusion de sinalefas, boca cerrada a 'U', purga de signos y cifrados).
7. Purga de estrofas multiples (conserva solo la letra activa para evitar solapamiento).
8. Ajuste de figuras largas (evitar arrastre/bleed nasal con silencios fisicos).
9. Purga de maquetacion y serializacion MusicXML 3.1 estandar con DTD.
"""

import os
import sys
import re
import shutil
import zipfile
import subprocess
import datetime
import xml.etree.ElementTree as ET
from pathlib import Path


# Rutas tipicas de MuseScore 4 en Windows
MUSESCORE_EXECUTABLES = [
    r"C:\Program Files\MuseScore 4\bin\MuseScore4.exe",
    r"C:\Program Files\MuseScore 4\MuseScore4.exe",
    r"C:\Program Files (x86)\MuseScore 4\bin\MuseScore4.exe",
    shutil.which("MuseScore4") or "",
    shutil.which("mscore") or "",
]

CLOUD_SCORES_DIR = Path.home() / "AppData" / "Local" / "MuseScore" / "MuseScore4" / "cloud_scores"

KNOWN_SCORE_DIRS = [
    CLOUD_SCORES_DIR,
    Path.home() / "OneDrive" / "Documentos" / "MuseScore4" / "Cloud Scores",
    Path.home() / "OneDrive - uc.cl" / "Yo" / "Universidad" / "Pastoral" / "Coro Misión País",
    Path.home() / "OneDrive" / "Documents" / "MuseScore4" / "Scores",
    Path.home() / "Documents" / "MuseScore4" / "Scores",
    Path.home() / "Downloads",
]


def find_musescore_bin():
    """Busca el ejecutable de MuseScore 4 en el sistema."""
    for p in MUSESCORE_EXECUTABLES:
        if p and os.path.exists(p):
            return p
    return None


def convert_mscz_to_musicxml(mscz_path, output_xml_path):
    """Convierte un archivo .mscz a .musicxml usando el CLI de MuseScore 4."""
    musescore_bin = find_musescore_bin()
    if not musescore_bin:
        raise RuntimeError(
            "MuseScore 4 no fue encontrado en las rutas estandar. "
            "Por favor exporta la partitura a MusicXML manualmente desde MuseScore."
        )
    
    cmd = [musescore_bin, "-o", str(output_xml_path), str(mscz_path)]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    if result.returncode != 0 or not os.path.exists(output_xml_path):
        raise RuntimeError(f"Fallo al convertir .mscz con MuseScore: {result.stderr or result.stdout}")
    return output_xml_path


def load_score_tree(input_path, temp_dir=None):
    """
    Carga cualquier archivo (.musicxml, .xml, .mxl, .mscz) y retorna la raiz XML.
    """
    input_path = Path(input_path)
    if not input_path.exists():
        raise FileNotFoundError(f"Archivo no encontrado: {input_path}")

    ext = input_path.suffix.lower()

    # 1. Archivo comprimido MuseScore (.mscz)
    if ext == ".mscz":
        if temp_dir is None:
            temp_dir = input_path.parent
        temp_xml = Path(temp_dir) / f"_temp_{input_path.stem}.musicxml"
        try:
            convert_mscz_to_musicxml(input_path, temp_xml)
            tree = ET.parse(str(temp_xml))
            root = tree.getroot()
            return root
        finally:
            if temp_xml.exists():
                try:
                    temp_xml.unlink()
                except Exception:
                    pass

    # 2. Archivo comprimido MusicXML (.mxl o zip renombrado a .musicxml)
    elif ext == ".mxl" or zipfile.is_zipfile(str(input_path)):
        with zipfile.ZipFile(str(input_path), "r") as z:
            rootfile_path = None
            if "META-INF/container.xml" in z.namelist():
                container_data = z.read("META-INF/container.xml")
                c_root = ET.fromstring(container_data)
                rf = c_root.find(".//rootfile")
                if rf is not None and "full-path" in rf.attrib:
                    rootfile_path = rf.attrib["full-path"]
            
            if not rootfile_path:
                candidates = [f for f in z.namelist() if f.endswith(".xml") or f.endswith(".musicxml")]
                if candidates:
                    rootfile_path = candidates[0]
                else:
                    raise ValueError("No se encontro archivo XML dentro del archivo comprimido")

            xml_data = z.read(rootfile_path)
            return ET.fromstring(xml_data)

    # 3. Archivo MusicXML estandar en texto plano (.musicxml o .xml)
    else:
        tree = ET.parse(str(input_path))
        return tree.getroot()


def detect_initial_bpm(root, fallback_bpm=71):
    """Detecta el BPM inicial a partir de <sound tempo='...'> o <metronome> en la partitura."""
    for sound in root.findall(".//sound[@tempo]"):
        try:
            tempo_val = float(sound.get("tempo"))
            if tempo_val > 0:
                return round(tempo_val)
        except (ValueError, TypeError):
            continue

    for metro in root.findall(".//metronome"):
        pm = metro.findtext("per-minute")
        if pm:
            try:
                pm_val = float(re.sub(r"[^\d.]", "", pm))
                if pm_val > 0:
                    return round(pm_val)
            except (ValueError, TypeError):
                continue

    return fallback_bpm


def extract_mscz_title(mscz_path):
    """Extrae el workTitle directamente del archivo interno .mscx dentro del .mscz."""
    try:
        with zipfile.ZipFile(str(mscz_path), "r") as z:
            for name in z.namelist():
                if name.endswith(".mscx") and not name.startswith("Excerpts/"):
                    xml_data = z.read(name)
                    root = ET.fromstring(xml_data)
                    for meta in root.findall(".//metaTag"):
                        if meta.get("name") in ["workTitle", "movementTitle"] and meta.text:
                            return meta.text.strip()
    except Exception:
        pass
    return None


def find_mscz_for_score(input_path):
    """
    Busca la partitura nativa de MuseScore (.mscz) asociada al archivo MusicXML:
    1. Si input_path ya es .mscz y existe, la retorna directamente.
    2. Busca en la misma carpeta con extension .mscz.
    3. Busca en la carpeta cloud_scores de MuseScore 4 por titulo o nombre coincidente.
    """
    p = Path(input_path)
    if p.suffix.lower() == ".mscz" and p.exists():
        return p

    clean_stem = re.sub(r"[-_](?:Arreglo|Vocal|Cantamus|coral|para).*$", "", p.stem, flags=re.I).strip().lower()

    # 1. Misma carpeta
    same_dir_mscz = p.parent / f"{p.stem}.mscz"
    if same_dir_mscz.exists():
        return same_dir_mscz
    same_dir_clean = p.parent / f"{clean_stem}.mscz"
    if same_dir_clean.exists():
        return same_dir_clean

    # 2. Repositorios de MuseScore y colecciones personales
    for score_dir in KNOWN_SCORE_DIRS:
        if not score_dir.exists():
            continue
        try:
            for mscz in score_dir.rglob("*.mscz"):
                mscz_stem = mscz.stem.lower()
                if clean_stem == mscz_stem or clean_stem in mscz_stem or mscz_stem in clean_stem:
                    return mscz

                # Si es un ID numerico o hash largo (como en cloud_scores), leer titulo interno
                if mscz_stem.isdigit() or len(mscz_stem) > 20:
                    try:
                        with zipfile.ZipFile(str(mscz), "r") as z:
                            for name in z.namelist():
                                if name.endswith(".mscx") and not name.startswith("Excerpts/"):
                                    root = ET.fromstring(z.read(name))
                                    for meta in root.findall(".//metaTag"):
                                        if meta.get("name") in ["workTitle", "movementTitle"] and meta.text:
                                            t = meta.text.strip().lower()
                                            if clean_stem in t or t in clean_stem or p.stem.lower() in t:
                                                return mscz
                    except Exception:
                        pass
        except Exception:
            continue
    return None


def extract_mscz_playback_data(mscz_path):
    """
    Lee las propiedades nativas de reproduccion directamente del .mscx dentro del .mscz:
    - Tempos base y de metronomo (<Tempo>)
    - Ritardandos / Accelerandos (<GradualTempoChange>): inicio, fin, curva (ease-out, ease-in, linear), factor
    - Cesuras (<Breath>): compas, tipo de simbolo y pausa en segundos
    - Calderones (<Fermata>): compas, subtipo y factor de alargamiento (timeStretch)
    """
    data = {
        "tempos": {},          # {m_num: bpm}
        "gradual_tempos": [],  # [{start_m, end_m, type, method, factor, text}]
        "breaths": [],         # [{m_num, symbol, pause}]
        "fermatas": []         # [{m_num, subtype, time_stretch}]
    }

    with zipfile.ZipFile(str(mscz_path), "r") as z:
        for name in z.namelist():
            if name.endswith(".mscx") and not name.startswith("Excerpts/"):
                root = ET.fromstring(z.read(name))
                break

    staff1 = root.find('.//Staff[@id="1"]')
    if staff1 is None:
        staff1 = root.find(".//Staff")
    if staff1 is None:
        return data

    measures = staff1.findall("Measure")
    total_m = len(measures)

    for idx, m in enumerate(measures):
        m_num = idx + 1
        for t in m.findall(".//Tempo"):
            val = t.findtext("tempo")
            if val:
                try:
                    data["tempos"][m_num] = round(float(val) * 60)
                except (ValueError, TypeError):
                    pass

    gtc_starts = []
    for staff in root.findall(".//Staff"):
        for idx, m in enumerate(staff.findall("Measure")):
            m_num = idx + 1
            for gtc in m.findall(".//GradualTempoChange"):
                ttype = gtc.findtext("tempoChangeType") or "ritardando"
                method = gtc.findtext("tempoEasingMethod") or "linear"
                factor_str = gtc.findtext("tempoChangeFactor")
                factor = float(factor_str) if factor_str else 0.75
                text = gtc.findtext("beginText") or "rit."

                delta_m = 2
                end_frac = None
                sp = m.find('.//Spanner[@type="GradualTempoChange"]')
                if sp is not None:
                    next_loc_m = sp.find(".//next/location/measures")
                    if next_loc_m is not None and next_loc_m.text:
                        try:
                            delta_m = int(next_loc_m.text)
                        except ValueError:
                            pass
                    next_loc_f = sp.find(".//next/location/fractions")
                    if next_loc_f is not None and next_loc_f.text:
                        f_text = next_loc_f.text.strip()
                        try:
                            from fractions import Fraction
                            f_val = float(Fraction(f_text))
                            if f_val < 0:
                                end_frac = max(0.0, min(1.0, 1.0 + f_val))
                            else:
                                end_frac = max(0.0, min(1.0, f_val))
                        except Exception:
                            end_frac = None
                    else:
                        if delta_m > 0:
                            end_frac = 0.0
                        else:
                            end_frac = 1.0
                else:
                    end_frac = 1.0

                if end_frac is None:
                    end_frac = 1.0

                end_m = min(total_m, m_num + delta_m)

                gtc_starts.append({
                    "start_m": m_num,
                    "end_m": max(m_num, end_m),
                    "end_fraction": end_frac,
                    "type": ttype,
                    "method": method,
                    "factor": factor,
                    "text": text
                })

            for b in m.findall(".//Breath"):
                pause_s = float(b.findtext("pause", "1.0") or "1.0")
                sym = b.findtext("symbol", "caesura")
                data["breaths"].append({
                    "m_num": m_num,
                    "symbol": sym,
                    "pause": pause_s
                })

            for f in m.findall(".//Fermata"):
                ts_str = f.findtext("timeStretch")
                ts = float(ts_str) if ts_str else 2.0
                data["fermatas"].append({
                    "m_num": m_num,
                    "subtype": f.findtext("subtype"),
                    "time_stretch": ts
                })

    unique_gtc = []
    seen_gtc = set()
    for g in gtc_starts:
        k = (g["start_m"], g["end_m"], g.get("end_fraction", 1.0), g["type"])
        if k not in seen_gtc:
            seen_gtc.add(k)
            unique_gtc.append(g)
    data["gradual_tempos"] = unique_gtc

    unique_b = []
    seen_b = set()
    for b in data["breaths"]:
        if b["m_num"] not in seen_b:
            seen_b.add(b["m_num"])
            unique_b.append(b)
    data["breaths"] = unique_b

    unique_f = []
    seen_f = set()
    for f in data["fermatas"]:
        if f["m_num"] not in seen_f:
            seen_f.add(f["m_num"])
            unique_f.append(f)
    data["fermatas"] = unique_f

    return data


def split_caesura_notes_in_tree(root, caesuras_info):
    """
    Para cada compas con cesura, divide la nota con cesura:
    - 75% de duracion para la fonacion de la nota (evita corte abrupto prematuro).
    - 25% de duracion restante como silencio fisico invisible (<rest print-object="no"/>).
    - Conserva la figura visual original (ej. 'half') y el signo <caesura/> con barras '//'.
    - Permite que Cantamus corte fonacion y respire durante el silencio calibrado.
    caesuras_info: dict {(m_num, note_offset): pause_seconds}
    """
    caesura_m_set = {m_k for (m_k, _) in caesuras_info.keys()}
    if not caesura_m_set:
        return

    div_elem = root.find(".//divisions")
    divisions = int(div_elem.text) if div_elem is not None and div_elem.text else 4

    for part in root.findall(".//part"):
        for measure in part.findall("measure"):
            m_num = int(measure.get("number", 0))
            if m_num not in caesura_m_set:
                continue

            curr_offset = 0
            notes = list(measure.findall("note"))
            for n in notes:
                if n.find("chord") is not None:
                    continue
                try:
                    dur = int(n.findtext("duration", "0"))
                except ValueError:
                    dur = 0

                has_caesura = bool(n.findall(".//caesura"))
                is_target = (m_num, curr_offset) in caesuras_info or has_caesura

                if is_target and n.find("rest") is None and dur > 0:
                    if dur >= 4:
                        split_dur = round(dur * 0.75)
                        rest_dur = dur - split_dur
                    elif dur >= 2:
                        split_dur = dur - 1
                        rest_dur = 1
                    else:
                        split_dur = dur
                        rest_dur = 0

                    if rest_dur > 0:
                        n.find("duration").text = str(split_dur)

                        # Crear el silencio fisico marcado como invisible para MuseScore
                        rest_note = ET.Element("note", attrib={"print-object": "no"})
                        ET.SubElement(rest_note, "rest")
                        d_sub = ET.SubElement(rest_note, "duration")
                        d_sub.text = str(rest_dur)
                        v_sub = ET.SubElement(rest_note, "voice")
                        v_sub.text = n.findtext("voice", "1")

                        rest_beats = rest_dur / max(1, divisions)
                        if rest_beats >= 1.0:
                            r_type = "quarter"
                        elif rest_beats >= 0.5:
                            r_type = "eighth"
                        elif rest_beats >= 0.25:
                            r_type = "16th"
                        else:
                            r_type = "32nd"
                        t_sub = ET.SubElement(rest_note, "type")
                        t_sub.text = r_type

                        # Insertar silencio inmediatamente despues de la nota acortada
                        idx_in_m = list(measure).index(n)
                        measure.insert(idx_in_m + 1, rest_note)
                        break

                curr_offset += dur


def inspect_score_info(input_path):
    """Extrae metadatos rapidos de la partitura (titulo, bpm, compases, partes)."""
    p = Path(input_path)
    info = {
        "filename": p.name,
        "path": str(p),
        "title": p.stem,
        "bpm": 71,
        "measures": 0,
        "parts": []
    }
    
    if p.suffix.lower() == ".mscz":
        t = extract_mscz_title(p)
        if t:
            info["title"] = t
            
    try:
        root = load_score_tree(p)
        wt = root.findtext(".//work/work-title")
        if wt:
            info["title"] = wt.strip()
        info["bpm"] = detect_initial_bpm(root, 71)
        
        parts = []
        for sp in root.findall(".//score-part"):
            pname = sp.findtext("part-name") or sp.get("id")
            parts.append(pname.strip())
        info["parts"] = parts
        
        p1 = root.find('.//part')
        if p1 is not None:
            info["measures"] = len(p1.findall("measure"))
    except Exception as e:
        info["error"] = str(e)
        
    return info


def sanitize_lyric_text(text):
    """
    Aplica las reglas foneticas estrictas de Cantamus:
    - Fusion de sinalefas (elimina espacios y NBSP intra-nota: 'te i' -> 'tei', 'to Es' -> 'toes')
    - Conversion a minusculas para evitar divisiones de tokens por CamelCase en el sintetizador G2P
    - Limpieza de numeros/letras de estrofa o coro al inicio: '1.', '2.', 'C.', 'A.'
    - Purga de signos de puntuacion y exclamacion
    - Purgado de acordes de guitarra (ej: 'Re/La', 'Sol/Si', 'Do#m', 'G7')
    - Vocalizacion de boca cerrada: 'mmm', 'mm', 'hm' -> 'u'
    """
    if not text:
        return ""

    # Reemplazar espacios invisibles / de no ruptura (NBSP \u00A0 a \u200B) por espacio normal
    clean = re.sub(r"[\u00A0\u2000-\u200B]", " ", text)

    # Remover prefijos de estrofa / coro al inicio (ej: '1.', '2.', '10.', 'C.', 'A.', 'V.')
    clean = re.sub(r"^\s*(?:[0-9]+|[A-Za-z])\.\s*", "", clean).strip()

    # Remover signos de puntuacion y no cantables
    clean = re.sub(r'[¡!¿?.,:;\-_"\'/\\()[\]{}~*^]', "", clean).strip()

    # Remover solo acordes con barra (ej: 'Re/La', 'Sol/Si', 'La/Do#') que no son texto lírico
    if re.match(r"^[A-Za-z#b]+/[A-Za-z#b]+$", clean):
        return ""

    # Vocalizacion para boca cerrada (Humming)
    if clean.lower() in ["mmm", "mm", "hm", "hmmm", "m"]:
        return "u"

    # Fusion estricta de sinalefas (remover todo espacio interno)
    clean = re.sub(r"\s+", "", clean)

    # Normalizacion a minusculas: evita que palabras fusionadas en sinalefa (ej. 'toEs')
    # se interpreten como dos palabras independientes por la mayuscula (CamelCase)
    clean = clean.lower()

    return clean


def build_master_tempo_map(root, mscz_data=None, rit_profile="ease-in", rit_drop=0.75, rit_measures=2, initial_bpm=None):
    """
    Construye un mapa maestro de tempos compas a compas y nota a nota:
    - Prioriza datos nativos de reproduccion de MuseScore si estan disponibles en mscz_data
      (factores exactos, curvas de aceleracion/desaceleracion, duraciones de pausa de cesuras).
    - Interpola y 'bakes' ritardandos intermedios y finales usando perfiles (ease-in, ease-out, linear).
    - Tras finalizar un ritardando, mantiene el BPM de llegada en toda la continuacion de la partitura
      sin reiniciarse al tempo previo a menos que haya una indicacion explicita de tempo.
    - Emula cesuras (<caesura>): inyecta el tempo calibrado a los segundos de pausa sobre el silencio fisico.
    - Emula calderones (<fermata>): en calderones intermedios dilata la duracion segun timeStretch.
    Retorna: dict {(m_num, offset_in_divisions): bpm}
    """
    p1 = root.find('.//part[1]')
    if p1 is None:
        return {}
    measures = p1.findall('measure')
    total_measures = len(measures)

    # 1. Medir duraciones de compases en divisiones
    measure_durations = {}
    for m in measures:
        m_num = int(m.get('number', 0))
        dur = 0
        for n in m.findall('note'):
            if n.find('chord') is None:
                try:
                    dur += int(n.findtext('duration', '0'))
                except ValueError:
                    pass
        measure_durations[m_num] = max(1, dur)

    divisions = 1
    div_elem = root.find('.//divisions')
    if div_elem is not None:
        try:
            divisions = max(1, int(div_elem.text))
        except (ValueError, TypeError):
            pass

    # 2. Detectar cambios de tempo explicitos (mscz_data tiene maxima prioridad)
    explicit_tempos = {}
    if mscz_data and mscz_data.get('tempos'):
        explicit_tempos.update(mscz_data['tempos'])

    for m in measures:
        m_num = int(m.get('number', 0))
        for s in m.findall('.//sound[@tempo]'):
            try:
                v = round(float(s.get('tempo')))
                if v > 0 and m_num not in explicit_tempos:
                    explicit_tempos[m_num] = v
            except (ValueError, TypeError):
                pass

    if initial_bpm is None or initial_bpm <= 0:
        initial_bpm = explicit_tempos.get(1, 71)

    # 3. Ritardandos / Accelerandos graduales
    gradual_tempos = []
    if mscz_data and mscz_data.get('gradual_tempos'):
        gradual_tempos = mscz_data['gradual_tempos']
    else:
        # Fallback a marcas visuales de MusicXML si no hay datos de MuseScore
        visual_rits = []
        for m in measures:
            m_num = int(m.get('number', 0))
            for w in m.findall('.//direction/direction-type/words'):
                if w.text and any(k in w.text.lower() for k in ['rit', 'rall']):
                    if m_num not in visual_rits:
                        visual_rits.append(m_num)

        for r_start in visual_rits:
            next_exp = min([x for x in explicit_tempos if x > r_start], default=None)
            end_m = (next_exp - 1) if next_exp else min(total_measures, r_start + (rit_measures or 2))
            gradual_tempos.append({
                'start_m': r_start,
                'end_m': max(r_start, end_m),
                'type': 'ritardando',
                'method': rit_profile,
                'factor': rit_drop
            })

    # 4. Cesuras (pausas de respiracion): {(m_num, offset): pause_seconds}
    caesuras = {}
    mscz_pauses = {b['m_num']: b.get('pause', 1.0) for b in mscz_data.get('breaths', [])} if mscz_data else {}

    for m in measures:
        m_num = int(m.get('number', 0))
        curr = 0
        found_in_m = False
        notes = [n for n in m.findall('note') if n.find('chord') is None]
        for n in notes:
            dur = int(n.findtext('duration', '0')) if n.findtext('duration') else 0
            has_caesura = bool(n.findall('.//caesura') or m.findall('.//direction/direction-type/caesura'))
            if has_caesura:
                pause_s = mscz_pauses.get(m_num, 1.0)
                caesuras[(m_num, curr)] = pause_s
                found_in_m = True
                break
            curr += dur

        if not found_in_m and m_num in mscz_pauses and notes:
            caesuras[(m_num, 0)] = mscz_pauses[m_num]

    # 5. Calderones / Fermatas: {(m_num, offset): time_stretch}
    fermatas = {}
    mscz_fermatas = {f['m_num']: f.get('time_stretch', 2.0) for f in mscz_data.get('fermatas', [])} if mscz_data else {}

    for m in measures:
        m_num = int(m.get('number', 0))
        curr = 0
        notes = [n for n in m.findall('note') if n.find('chord') is None]
        for n in notes:
            dur = int(n.findtext('duration', '0')) if n.findtext('duration') else 0
            has_ferm = bool(n.findall('.//fermata'))
            if has_ferm or m_num in mscz_fermatas:
                ts = mscz_fermatas.get(m_num, 2.0)
                fermatas[(m_num, curr)] = ts
            curr += dur

    def calc_curve(t, profile):
        if profile == 'ease-out':
            return 1.0 - (1.0 - t)**2
        elif profile == 'ease-in':
            return t**2
        return t

    tempo_map = {}
    tempo_map[(1, 0)] = initial_bpm
    current_bpm = initial_bpm

    gtc_by_start = {g['start_m']: g for g in gradual_tempos}

    m = 1
    while m <= total_measures:
        if m in explicit_tempos and m > 1:
            current_bpm = explicit_tempos[m]
            tempo_map[(m, 0)] = current_bpm

        if m in gtc_by_start:
            gtc = gtc_by_start[m]
            r_start = gtc['start_m']
            r_end = max(r_start, gtc.get('end_m', r_start + (rit_measures or 2)))
            g_method = gtc.get('method') or 'linear'
            g_factor = gtc.get('factor') or rit_drop

            if r_end in explicit_tempos:
                target_bpm = explicit_tempos[r_end]
            else:
                target_bpm = round(current_bpm * g_factor)

            start_bpm = current_bpm
            r_end_frac = gtc.get("end_fraction", 1.0)
            if r_end > r_start:
                dur_prior = sum(measure_durations.get(k, 1) for k in range(r_start, r_end))
                dur_end = measure_durations.get(r_end, 1)
                end_off_in_r_end = round(dur_end * r_end_frac)
                span_dur = max(1, dur_prior + end_off_in_r_end)
            else:
                dur_start = measure_durations.get(r_start, 1)
                span_dur = max(1, round(dur_start * r_end_frac))

            for r_m in range(r_start, r_end + 1):
                if r_m == r_end and r_end_frac == 0.0 and r_m in explicit_tempos:
                    tempo_map[(r_m, 0)] = explicit_tempos[r_m]
                    current_bpm = explicit_tempos[r_end]
                    continue

                off_base = sum(measure_durations.get(k, 1) for k in range(r_start, r_m))

                # Recolectar notas y cesuras a lo largo de TODAS las partes vocales para este compas
                all_meas_notes = []
                for part in root.findall('.//part'):
                    m_el = part.find(f'.//measure[@number="{r_m}"]')
                    if m_el is not None:
                        curr = 0
                        m_notes = list(m_el.findall('note'))
                        for n_idx, n in enumerate(m_notes):
                            if n.find('chord') is not None:
                                continue
                            dur = int(n.findtext('duration', '0')) if n.findtext('duration') else 0
                            if n.find('rest') is None and dur > 0:
                                next_rest_dur = 0
                                if n_idx + 1 < len(m_notes) and m_notes[n_idx + 1].find('rest') is not None:
                                    next_rest_dur = int(m_notes[n_idx + 1].findtext('duration', '0'))
                                all_meas_notes.append((curr, dur, next_rest_dur))
                            curr += dur

                # Extraer todos los offsets unicos donde inicia una nota
                note_offsets = sorted(set([0] + [off for off, _, _ in all_meas_notes]))

                applied_caesuras = set()
                for off in note_offsets:
                    t = min(1.0, max(0.0, (off_base + off) / span_dur))
                    n_bpm = round(start_bpm - (start_bpm - target_bpm) * calc_curve(t, g_method))
                    tempo_map[(r_m, off)] = max(20, n_bpm)

                    # Si hay cesura en este compas y offset
                    if (r_m, off) in caesuras and (r_m, off) not in applied_caesuras:
                        applied_caesuras.add((r_m, off))
                        pause_s = caesuras[(r_m, off)]
                        matching = [entry for entry in all_meas_notes if entry[0] == off]
                        note_dur = matching[0][1] if matching else max(1, round(divisions))
                        next_rest_dur = matching[0][2] if matching and matching[0][2] > 0 else max(1, round(divisions * 0.5))
                        rest_beats = next_rest_dur / divisions
                        rest_bpm = max(20, min(240, round(rest_beats * 60.0 / max(0.2, pause_s))))
                        tempo_map[(r_m, off + note_dur)] = rest_bpm
                        t_resume = min(1.0, max(0.0, (off_base + off + note_dur + next_rest_dur) / span_dur))
                        resume_bpm = round(start_bpm - (start_bpm - target_bpm) * calc_curve(t_resume, g_method))
                        tempo_map[(r_m, off + note_dur + next_rest_dur)] = max(20, resume_bpm)

            if r_end not in explicit_tempos:
                current_bpm = target_bpm
            else:
                current_bpm = explicit_tempos[r_end]

            m = r_end + 1
            continue

        # Cesuras intermedias fuera de ritardandos
        meas_el = p1.find(f'.//measure[@number="{m}"]')
        if meas_el is not None:
            curr_off = 0
            m_notes = list(meas_el.findall('note'))
            for n_idx, note in enumerate(m_notes):
                dur = int(note.findtext('duration', '0')) if note.findtext('duration') else 0
                if note.find('chord') is not None:
                    continue
                if (m, curr_off) in caesuras:
                    pause_s = caesuras[(m, curr_off)]
                    note_dur = dur
                    next_rest_dur = 0
                    if n_idx + 1 < len(m_notes) and m_notes[n_idx + 1].find('rest') is not None:
                        next_rest_dur = int(m_notes[n_idx + 1].findtext('duration', '0'))
                    if next_rest_dur == 0:
                        next_rest_dur = max(1, round(divisions * 0.5))
                    rest_beats = next_rest_dur / divisions
                    rest_bpm = max(20, min(240, round(rest_beats * 60.0 / max(0.2, pause_s))))
                    tempo_map[(m, curr_off)] = current_bpm
                    tempo_map[(m, curr_off + note_dur)] = rest_bpm
                    tempo_map[(m, curr_off + note_dur + next_rest_dur)] = current_bpm
                curr_off += dur

        # Calderones / Fermatas intermedios: duplicar duracion (timeStretch) solo si m < total_measures
        if meas_el is not None and m < total_measures:
            curr_off = 0
            for note in meas_el.findall('note'):
                dur = int(note.findtext('duration', '0')) if note.findtext('duration') else 0
                if note.find('chord') is not None:
                    continue
                if (m, curr_off) in fermatas:
                    ts = fermatas[(m, curr_off)]
                    tempo_map[(m, curr_off)] = max(20, round(current_bpm / ts))
                    tempo_map[(m, curr_off + dur)] = current_bpm
                curr_off += dur

        m += 1

    # Asegurar que el tempo actual prevalezca en todos los compases subsiguientes hasta el final de la obra
    for trail_m in range(1, total_measures + 1):
        if (trail_m, 0) not in tempo_map:
            prev_bpms = [tempo_map[(mk, off)] for (mk, off) in sorted(tempo_map.keys()) if mk < trail_m]
            if prev_bpms:
                tempo_map[(trail_m, 0)] = prev_bpms[-1]

    return tempo_map


def process_cantamus(
    input_path,
    output_path=None,
    initial_bpm=None,
    rit_profile="ease-in",
    rit_drop=0.75,
    rit_measures=2,
    keep_accompaniment=False,
    fix_tenor_breathing=True,
    mscz_path=None,
):
    """
    Ejecuta el pipeline completo de Cantamus sobre la partitura de entrada.
    
    Parametros:
      input_path: Ruta al archivo (.musicxml, .xml, .mxl, .mscz)
      output_path: Ruta del archivo resultante (si es None, añade '_Cantamus.musicxml')
      initial_bpm: BPM inicial (si es None, lo auto-detecta de la partitura)
      rit_profile: 'ease-in', 'ease-out', 'linear', o 'none'
      rit_drop: Factor de velocidad final del ritardando (ej. 0.75 = frenar al 75% del tempo)
      rit_measures: Cantidad de compases finales donde aplicar el ritardando (por defecto 2)
      keep_accompaniment: Si True, conserva pistas de instrumentos asignando programa MIDI
      fix_tenor_breathing: Si True, divide notas largas al final de frase en nota + silencio
      mscz_path: Ruta opcional explicita a la partitura .mscz correspondiente
    """
    input_path = Path(input_path)
    if output_path is None:
        clean_stem = re.sub(r'_Cantamus.*$', '', input_path.stem)
        output_path = input_path.parent / f"{clean_stem}_Cantamus.musicxml"
    else:
        output_path = Path(output_path)

    # 1. Detectar o vincular archivo .mscz correspondiente para heredar propiedades exactas
    if mscz_path is None:
        mscz_path = find_mscz_for_score(input_path)

    mscz_data = None
    if mscz_path and Path(mscz_path).exists():
        try:
            mscz_data = extract_mscz_playback_data(mscz_path)
            print(f"[INFO] Partitura MuseScore vinculada: {Path(mscz_path).name}")
            if mscz_data.get('gradual_tempos'):
                for g in mscz_data['gradual_tempos']:
                    print(f"       -> Ritardando MuseScore: m.{g['start_m']} a m.{g['end_m']}, curva={g['method']}, factor={g['factor']}")
            if mscz_data.get('breaths'):
                print(f"       -> Cesuras MuseScore: {[b['m_num'] for b in mscz_data['breaths']]}")
            if mscz_data.get('fermatas'):
                print(f"       -> Calderones MuseScore: {[f['m_num'] for f in mscz_data['fermatas']]}")
        except Exception as e:
            print(f"[WARN] No se pudieron extraer datos de reproduccion del .mscz: {e}")

    # Cargar arbol XML
    root = load_score_tree(input_path)

    # Detectar BPM inicial si no fue provisto
    if initial_bpm is None or initial_bpm <= 0:
        if mscz_data and mscz_data.get('tempos'):
            initial_bpm = mscz_data['tempos'].get(1, detect_initial_bpm(root, fallback_bpm=71))
        else:
            initial_bpm = detect_initial_bpm(root, fallback_bpm=71)

    # -------------------------------------------------------------
    # 2. Filtrado y Reindexacion Correlativa Estricta (P1..Pn)
    # -------------------------------------------------------------
    part_list = root.find("part-list")
    if part_list is None:
        raise ValueError("La partitura no contiene etiqueta <part-list>")

    score_parts = part_list.findall("score-part")
    voice_keywords = [
        "soprano", "alto", "tenor", "bajo", "bass", "vocal", "coro", "choir",
        "voz", "voces", "mujeres", "hombres", "canto", "solista"
    ]
    non_vocal_instruments = [
        "contrabajo", "bajo electrico", "bajo eléctrico", "bajo acustico",
        "bajo acústico", "guitar", "piano", "organ", "órgano", "violin",
        "viola", "violonchelo", "cello", "flauta", "oboe", "clarinete",
        "trompeta", "trompa", "timbal", "percusion", "pandero", "bateria"
    ]

    retained_parts = []
    for sp in score_parts:
        pid = sp.get("id")
        pname = (sp.findtext("part-name") or "").lower()
        
        is_instrument = any(ik in pname for ik in non_vocal_instruments)
        is_vocal = any(vk in pname for vk in voice_keywords) and not is_instrument

        if is_vocal or keep_accompaniment or len(score_parts) <= 4:
            retained_parts.append((pid, sp, is_vocal))
        else:
            part_list.remove(sp)

    id_map = {}
    for idx, (old_id, sp, is_vocal) in enumerate(retained_parts):
        new_id = f"P{idx + 1}"
        id_map[old_id] = new_id
        sp.set("id", new_id)

        if not is_vocal and keep_accompaniment:
            midi_inst = sp.find("midi-instrument")
            if midi_inst is None:
                midi_inst = ET.SubElement(sp, "midi-instrument", id=f"{new_id}-I1")
                prog = ET.SubElement(midi_inst, "midi-program")
                prog.text = "49"
        else:
            for child in list(sp):
                if child.tag not in ["part-name", "part-abbreviation"]:
                    sp.remove(child)

    for part in list(root.findall("part")):
        old_id = part.get("id")
        if old_id in id_map:
            part.set("id", id_map[old_id])
        else:
            root.remove(part)

    # -------------------------------------------------------------
    # 3. Tratamiento Fisico de Cesuras (Corte Real con <rest/>)
    # -------------------------------------------------------------
    # Asegurar resolucion de duracion suficiente (minimo divisions >= 4)
    div_elem = root.find(".//divisions")
    divisions = 1
    if div_elem is not None and div_elem.text:
        try:
            divisions = int(div_elem.text)
        except ValueError:
            divisions = 1
    if divisions < 4:
        mult = 4 // divisions
        for d in root.findall(".//divisions"):
            try:
                d.text = str(int(d.text) * mult)
            except ValueError:
                pass
        for dur_elem in root.findall(".//duration"):
            if dur_elem.text:
                try:
                    dur_elem.text = str(int(dur_elem.text) * mult)
                except ValueError:
                    pass

    caesuras_info = {}
    mscz_pauses = {b['m_num']: b.get('pause', 1.0) for b in mscz_data.get('breaths', [])} if mscz_data else {}
    for part in root.findall(".//part"):
        for measure in part.findall("measure"):
            m_num = int(measure.get("number", 0))
            curr = 0
            for n in measure.findall("note"):
                if n.find("chord") is not None:
                    continue
                dur = int(n.findtext("duration", "0")) if n.findtext("duration") else 0
                has_caesura = bool(n.findall(".//caesura") or measure.findall(".//direction/direction-type/caesura"))
                if has_caesura and (m_num, curr) not in caesuras_info:
                    pause_s = mscz_pauses.get(m_num, 1.0)
                    caesuras_info[(m_num, curr)] = pause_s
                    break
                curr += dur

            if (m_num, 0) not in caesuras_info and m_num in mscz_pauses:
                caesuras_info[(m_num, 0)] = mscz_pauses[m_num]

    split_caesura_notes_in_tree(root, caesuras_info)

    # -------------------------------------------------------------
    # 4. Construccion del Mapa Maestro de Tempos Multicuerda
    # -------------------------------------------------------------
    tempo_map = build_master_tempo_map(
        root=root,
        mscz_data=mscz_data,
        rit_profile=rit_profile,
        rit_drop=rit_drop,
        rit_measures=rit_measures,
        initial_bpm=initial_bpm
    )

    # -------------------------------------------------------------
    # 3. Procesamiento por Parte (Monofonía Estricta y Tempo Baking)
    # -------------------------------------------------------------
    for part in root.findall("part"):
        pid = part.get("id")
        measures = part.findall("measure")
        last_applied_bpm = None

        for m_idx, measure in enumerate(measures):
            m_num = m_idx + 1

            # A. MONOFONIA ESTRICTA: Eliminar notas de acordes (divisi), voces secundarias y purgar estrofas multiples
            notes_in_measure = list(measure.findall("note"))
            has_voice_1 = any(n.findtext("voice") in [None, "", "1"] for n in notes_in_measure)

            for note in notes_in_measure:
                # Si es nota de acorde (divisi), eliminarla del compas
                if note.find("chord") is not None:
                    measure.remove(note)
                    continue

                # Si es voz secundaria y el pentagrama ya tiene voz principal, eliminarla
                v_text = note.findtext("voice")
                if v_text and v_text.strip() not in ["", "1"] and has_voice_1:
                    measure.remove(note)
                    continue

                # Purgar estrofas multiples: conservar solo la primera <lyric>
                lyrics = note.findall("lyric")
                if len(lyrics) > 1:
                    for sec_lyric in lyrics[1:]:
                        note.remove(sec_lyric)

            # B. LIMPIEZA DE DIRECTIVAS PREVIAS DE TEMPO EN ESTA PARTE
            for d in list(measure.findall("direction")):
                if d.find(".//sound[@tempo]") is not None or d.find(".//metronome") is not None:
                    measure.remove(d)

            # C. INYECCION DE TEMPOS MAESTROS SINCRONIZADOS (INVISIBLES Y DEDUPLICADOS)
            # Obtener todos los eventos planificados para este compas ordenados por offset
            m_events = [(off, bpm) for (m_k, off), bpm in tempo_map.items() if m_k == m_num]
            m_events.sort(key=lambda x: x[0])

            curr_offset = 0
            applied_offsets = set()

            for note in list(measure.findall("note")):
                if note.find("chord") is not None:
                    continue
                try:
                    dur = int(note.findtext("duration", "0"))
                except ValueError:
                    dur = 0

                # Si hay eventos de tempo planificados en o antes del offset de esta nota
                pending_events = [ev for ev in m_events if ev[0] not in applied_offsets and curr_offset >= ev[0]]
                if pending_events:
                    target_off, target_bpm = pending_events[-1]
                    if last_applied_bpm is None or target_bpm != last_applied_bpm:
                        dir_elem = ET.Element("direction", placement="above", attrib={"print-object": "no"})
                        dt = ET.SubElement(dir_elem, "direction-type")
                        w = ET.SubElement(dt, "words", attrib={"print-object": "no"})
                        ET.SubElement(dir_elem, "sound", tempo=str(target_bpm))

                        idx_in_m = list(measure).index(note)
                        measure.insert(idx_in_m, dir_elem)
                        last_applied_bpm = target_bpm
                    for ev in pending_events:
                        applied_offsets.add(ev[0])

                curr_offset += dur

            # Para cualquier evento restante (ej. compas de silencio o notas que terminaron antes del final del compas)
            for target_off, target_bpm in m_events:
                if target_off not in applied_offsets:
                    if target_off == 0:
                        if last_applied_bpm is None or target_bpm != last_applied_bpm:
                            dir_elem = ET.Element("direction", placement="above", attrib={"print-object": "no"})
                            dt = ET.SubElement(dir_elem, "direction-type")
                            w = ET.SubElement(dt, "words", attrib={"print-object": "no"})
                            ET.SubElement(dir_elem, "sound", tempo=str(target_bpm))
                            measure.insert(0, dir_elem)
                            last_applied_bpm = target_bpm
                        applied_offsets.add(target_off)
                    else:
                        # Si es target_off > 0 y este pentagrama ya terminó sus notas antes,
                        # se agrega al final del compas (NUNCA al inicio en indice 0)
                        if last_applied_bpm is None or target_bpm != last_applied_bpm:
                            dir_elem = ET.Element("direction", placement="above", attrib={"print-object": "no"})
                            dt = ET.SubElement(dir_elem, "direction-type")
                            w = ET.SubElement(dt, "words", attrib={"print-object": "no"})
                            ET.SubElement(dir_elem, "sound", tempo=str(target_bpm))
                            measure.append(dir_elem)
                            last_applied_bpm = target_bpm
                        applied_offsets.add(target_off)

    # -------------------------------------------------------------
    # 4. Procesamiento Fonetico de Lyrics (Regla 1-Nota = 1-Silaba)
    # -------------------------------------------------------------
    parent_map = {c: p for p in root.iter() for c in p}

    for lyric in list(root.findall(".//lyric")):
        text_nodes = lyric.findall("text")
        combined_text = "".join([t.text or "" for t in text_nodes])

        clean = sanitize_lyric_text(combined_text)

        if not clean:
            # Si no quedo texto cantable, eliminar <lyric>
            parent = parent_map.get(lyric)
            if parent is not None and lyric in list(parent):
                parent.remove(lyric)
        else:
            # Limpiar atributos visuales de estilo (evitar que quede negrita heredada de estrofas)
            lyric.attrib.pop("font-weight", None)
            lyric.attrib.pop("font-style", None)

            # Consolidar en un solo nodo <text>
            if text_nodes:
                text_nodes[0].text = clean
                text_nodes[0].attrib.pop("font-weight", None)
                text_nodes[0].attrib.pop("font-style", None)
                for t in text_nodes[1:]:
                    lyric.remove(t)
            else:
                tn = ET.SubElement(lyric, "text")
                tn.text = clean

    # -------------------------------------------------------------
    # 5. Purga de Metadatos y Elementos Graficos Incompatibles
    # -------------------------------------------------------------
    tags_to_remove = [
        "defaults", "credit", "print", "midi-device",
        "part-group", "multiple-rest", "offset"
    ]
    parent_map = {c: p for p in root.iter() for c in p}
    for tag in tags_to_remove:
        for elem in list(root.findall(f".//{tag}")):
            parent = parent_map.get(elem)
            if parent is not None and elem in list(parent):
                parent.remove(elem)

    # -------------------------------------------------------------
    # 6. Serializacion a MusicXML 3.1 Estandar con Cabecera DTD
    # -------------------------------------------------------------
    root.set("version", "3.1")
    xml_str = ET.tostring(root, encoding="utf-8")
    dtd_header = (
        b'<?xml version="1.0" encoding="UTF-8"?>\n'
        b'<!DOCTYPE score-partwise PUBLIC "-//Recordare//DTD MusicXML 3.1 Partwise//EN" '
        b'"http://www.musicxml.org/dtds/partwise.dtd">\n'
    )

    with open(output_path, "wb") as f:
        f.write(dtd_header + xml_str)

    print(f"OK: Generado con exito: {output_path}")
    return output_path


def get_recent_scores(limit=15):
    """Encuentra las partituras mas recientes en Downloads y en MuseScore Cloud Cache."""
    downloads = Path.home() / "Downloads"
    cloud_dir = Path.home() / "AppData" / "Local" / "MuseScore" / "MuseScore4" / "cloud_scores"
    valid_exts = [".musicxml", ".xml", ".mxl", ".mscz"]
    items = []

    if downloads.exists():
        for f in downloads.iterdir():
            if f.is_file() and f.suffix.lower() in valid_exts and not f.name.endswith("_Cantamus.musicxml"):
                items.append({
                    "name": f.name,
                    "title": f.stem,
                    "path": str(f),
                    "ext": f.suffix.lower(),
                    "source": "Downloads",
                    "mtime": f.stat().st_mtime,
                    "mtime_str": datetime.datetime.fromtimestamp(f.stat().st_mtime).strftime("%d/%m %H:%M")
                })

    if cloud_dir.exists():
        for f in cloud_dir.glob("*.mscz"):
            title = extract_mscz_title(f) or f.stem
            items.append({
                "name": f"{title} ({f.name})" if title != f.stem else f.name,
                "title": title,
                "path": str(f),
                "ext": ".mscz",
                "source": "MuseScore Cloud",
                "mtime": f.stat().st_mtime,
                "mtime_str": datetime.datetime.fromtimestamp(f.stat().st_mtime).strftime("%d/%m %H:%M")
            })

    items.sort(key=lambda x: x["mtime"], reverse=True)
    return items[:limit]


def get_latest_downloads_score():
    """Encuentra la partitura mas reciente en la carpeta Downloads."""
    downloads = Path.home() / "Downloads"
    if not downloads.exists():
        return None
    valid_exts = [".musicxml", ".xml", ".mxl", ".mscz"]
    candidates = []
    for f in downloads.iterdir():
        if f.is_file() and f.suffix.lower() in valid_exts and not f.name.endswith("_Cantamus.musicxml"):
            candidates.append(f)
    if not candidates:
        return None
    candidates.sort(key=lambda x: x.stat().st_mtime, reverse=True)
    return candidates[0]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso:")
        print("  python cantamus_pipeline.py <archivo_entrada> [archivo_salida] [BPM] [rit_profile] [rit_drop]")
        print("  python cantamus_pipeline.py --auto  (Procesa la partitura mas reciente en Downloads)")
        sys.exit(1)

    first_arg = sys.argv[1]
    if first_arg == "--auto":
        recent = get_latest_downloads_score()
        if not recent:
            print("No se encontraron partituras recientes en Downloads.")
            sys.exit(1)
        print(f"Procesando automaticamente: {recent}")
        process_cantamus(recent)
        sys.exit(0)

    inp = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 and not sys.argv[2].isdigit() else None
    
    args_rest = sys.argv[2:] if out is None else sys.argv[3:]
    bpm = int(args_rest[0]) if len(args_rest) > 0 and args_rest[0].isdigit() else None
    profile = args_rest[1] if len(args_rest) > 1 and not args_rest[1].replace(".", "").isdigit() else "ease-in"
    drop = float(args_rest[2]) if len(args_rest) > 2 else 0.75

    process_cantamus(inp, out, bpm, profile, drop)
