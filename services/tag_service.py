"""
Servicio para la gestión y navegación de etiquetas jerárquicas multinivel.
"""

from collections import defaultdict
from typing import List, Dict, Tuple, Any, Set
from constants import ORDENES_PERSONALIZADOS, MAPEO_LIBROS_BIBLIA


def tag_matches(tag_pattern: str, song_tags: List[str]) -> bool:
    """
    Determina si una canción coincide con una etiqueta o categoría padre.
    
    Soporta coincidencia exacta (ej: 'Cantos Bíblicos: Salmos') o por prefijo jerárquico
    (ej: una canción con 'Cantos Bíblicos: Salmos: Salmos Penitenciales' coincide tanto
    con 'Cantos Bíblicos' como con 'Cantos Bíblicos: Salmos').
    """
    if not tag_pattern or not song_tags:
        return False

    normalized_pattern = tag_pattern.replace(" ", "").lower()
    prefix_pattern = normalized_pattern + ":"

    for t in song_tags:
        if not t:
            continue
        norm_t = t.replace(" ", "").lower()
        if norm_t == normalized_pattern or norm_t.startswith(prefix_pattern):
            return True

    return False


def build_hierarchical_tags(tags_set: Set[str]) -> Tuple[List[str], Dict[str, List[Dict[str, Any]]]]:
    """
    Construye la estructura de etiquetas para la página /listas.
    
    Retorna:
      - simple_tags: Lista de etiquetas planas (sin ':' en su nombre).
      - hierarchical_tags: Diccionario de categorías principales hacia una lista de subcategorías
        ordenadas, donde cada subcategoría puede contener hijos (sub-subcategorías).
    """
    simple_tags = sorted([t for t in tags_set if ':' not in t])

    cat_tree = defaultdict(dict)
    for tag in tags_set:
        if ':' not in tag:
            continue
        parts = [p.strip() for p in tag.split(':')]
        cat = parts[0]
        if len(parts) > 1:
            sub = parts[1]
            if sub not in cat_tree[cat]:
                cat_tree[cat][sub] = {
                    'name': sub,
                    'full_tag': f"{cat}: {sub}",
                    'children': {}
                }
            if len(parts) > 2:
                subsub = parts[2]
                subsub_full = f"{cat}: {sub}: {subsub}"
                if subsub not in cat_tree[cat][sub]['children']:
                    cat_tree[cat][sub]['children'][subsub] = {
                        'name': subsub,
                        'full_tag': subsub_full
                    }

    hierarchical_tags = {}
    for cat in sorted(cat_tree.keys()):
        subs_dict = cat_tree[cat]
        if cat in ORDENES_PERSONALIZADOS:
            orden = ORDENES_PERSONALIZADOS[cat]
            if cat == "Cantos Bíblicos":
                sorted_subs = sorted(
                    subs_dict.values(),
                    key=lambda item: orden.get(MAPEO_LIBROS_BIBLIA.get(item['name'].lower(), item['name']), 999)
                )
            else:
                sorted_subs = sorted(
                    subs_dict.values(),
                    key=lambda item: orden.get(item['name'], 999)
                )
        else:
            sorted_subs = sorted(subs_dict.values(), key=lambda item: item['name'])

        for sub_item in sorted_subs:
            sub_item['children'] = sorted(sub_item['children'].values(), key=lambda c: c['name'])

        hierarchical_tags[cat] = sorted_subs

    return simple_tags, hierarchical_tags


def build_breadcrumbs(tag_name: str) -> List[Dict[str, str]]:
    """
    Genera la secuencia de migas de pan para una etiqueta jerárquica.
    Ejemplo: 'Cantos Bíblicos: Salmos: Salmos Penitenciales' ->
    [
        {'name': 'Cantos Bíblicos', 'tag_name': 'Cantos Bíblicos'},
        {'name': 'Salmos', 'tag_name': 'Cantos Bíblicos: Salmos'},
        {'name': 'Salmos Penitenciales', 'tag_name': 'Cantos Bíblicos: Salmos: Salmos Penitenciales'}
    ]
    """
    if not tag_name:
        return []

    breadcrumbs = []
    crumbs_accum = []
    for part in [p.strip() for p in tag_name.split(':')]:
        crumbs_accum.append(part)
        breadcrumbs.append({
            'name': part,
            'tag_name': ": ".join(crumbs_accum)
        })

    return breadcrumbs


def get_child_tags(tag_name: str, all_songs: list) -> List[Dict[str, str]]:
    """
    Obtiene las subetiquetas hijas inmediatas de la etiqueta actual para mostrarlas
    como filtros directos en la cabecera de la vista de tag.
    """
    if not tag_name:
        return []

    child_tags = []
    seen_child_tags = set()
    normalized_tag_name = tag_name.replace(" ", "").lower()
    norm_prefix = normalized_tag_name + ":"
    cur_parts_count = len([p.strip() for p in tag_name.split(':')])

    for song in all_songs:
        for t in (song.tags or []):
            if not t:
                continue
            norm_t = t.replace(" ", "").lower()
            if norm_t.startswith(norm_prefix):
                t_parts = [p.strip() for p in t.split(':')]
                if len(t_parts) > cur_parts_count:
                    child_full_tag = ": ".join(t_parts[:cur_parts_count + 1])
                    child_name = t_parts[cur_parts_count]
                    if child_full_tag not in seen_child_tags:
                        seen_child_tags.add(child_full_tag)
                        child_tags.append({
                            'name': child_name,
                            'full_tag': child_full_tag
                        })

    return child_tags


def process_song_tags(tags: List[str]) -> List[Dict[str, Any]]:
    """
    Desglosa las etiquetas de una canción para generar los botones de navegación
    en la ficha de la obra, evitando duplicar categorías padres.
    """
    if not tags:
        return []

    processed_tags = []
    seen_tags = set()

    for tag in tags:
        if not tag or not tag.strip():
            continue
        parts = [p.strip() for p in tag.split(':')]
        accum = []
        for idx, p in enumerate(parts):
            accum.append(p)
            tag_path = ": ".join(accum)
            if tag_path not in seen_tags:
                seen_tags.add(tag_path)
                processed_tags.append({
                    'tag_name': tag_path,
                    'label': p,
                    'is_root': (idx == 0 and len(parts) > 1)
                })

    return processed_tags
