"""
Utilidades para letras del reproductor.

Formato interno (data.json / columna letras_json):
    {"sincronizada": bool, "lineas": [{"t": segundos | null, "text": "..."}]}

Formato de edición para el admin: LRC estándar, una línea por verso.
    [01:23.45] Texto sincronizado
    Texto sin tiempo (letra no sincronizada)
"""
import re

_LRC_TAG = re.compile(r'^\s*\[(\d{1,3}):(\d{2})(?:[.:](\d{1,3}))?\]\s*(.*)$')


def lrc_to_letras(texto):
    """Convierte texto LRC (o texto plano) al formato interno. Devuelve None si está vacío."""
    lineas = []
    sincronizada = False
    for raw in (texto or '').splitlines():
        if not raw.strip():
            continue
        m = _LRC_TAG.match(raw)
        if m:
            mins, secs, frac, txt = m.groups()
            t = int(mins) * 60 + int(secs) + (int(frac) / (10 ** len(frac)) if frac else 0)
            lineas.append({'t': round(t, 2), 'text': txt.strip()})
            sincronizada = True
        else:
            lineas.append({'t': None, 'text': raw.strip()})
    if not lineas:
        return None
    if sincronizada:
        # Si solo algunas líneas tienen tiempo no se puede sincronizar de forma fiable
        sincronizada = all(l['t'] is not None for l in lineas)
    return {'sincronizada': sincronizada, 'lineas': lineas}


def letras_to_lrc(letras):
    """Convierte el formato interno a texto LRC editable."""
    if not letras:
        return ''
    out = []
    for l in letras.get('lineas', []):
        t = l.get('t')
        if t is None:
            out.append(l['text'])
        else:
            m, s = divmod(t, 60)
            out.append('[%02d:%05.2f] %s' % (int(m), s, l['text']))
    return '\n'.join(out)
