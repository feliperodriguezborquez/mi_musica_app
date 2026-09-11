"""
Servicio para búsqueda, filtrado, armado de playlists y ordenamiento del catálogo de obras.
"""

from typing import List, Tuple, Optional
from unidecode import unidecode
from constants import (
    CITA_REGEX,
    MAPEO_LIBROS_BIBLIA,
    ORDEN_LIBROS_BIBLIA,
    ORDENES_PERSONALIZADOS,
)
from models import Cancion
from services.tag_service import tag_matches


def parse_cita_biblica(texto: Optional[str]) -> Optional[Tuple[int, int, int]]:
    """
    Busca una cita bíblica en un texto y devuelve una tupla para ordenamiento.
    Retorna (orden_libro, capítulo, versículo) o None si no encuentra una cita válida.
    """
    if not texto:
        return None

    match = CITA_REGEX.search(texto)
    if not match:
        return None

    nombre_libro_raw, capitulo_str, versiculo_str = match.groups()
    nombre_libro_limpio = unidecode(nombre_libro_raw.strip().lower())

    nombre_canonico = MAPEO_LIBROS_BIBLIA.get(nombre_libro_limpio)
    if not nombre_canonico:
        return None

    orden_libro = ORDEN_LIBROS_BIBLIA.get(nombre_canonico, 999)
    capitulo = int(capitulo_str)
    versiculo = int(versiculo_str) if versiculo_str else 0

    return (orden_libro, capitulo, versiculo)


def normalize_for_sorting(titulo: Optional[str]) -> str:
    """
    Normaliza el título de una obra para ordenación alfabética ignorando
    acentos, mayúsculas, signos de puntuación e interrogaciones/exclamaciones.
    """
    if not titulo:
        return ""
    titulo_normalizado = unidecode(titulo.lower())
    return "".join(c for c in titulo_normalizado if c.isalnum() or c.isspace()).strip()


def normalize_category_name(cat_name: Optional[str]) -> str:
    """
    Normaliza variaciones tipográficas de categorías principales ('Composición', 'Arreglo').
    """
    if not cat_name:
        return ""
    c = unidecode(cat_name.lower().strip())
    if c.startswith('arreglo'):
        return 'Arreglo'
    if c.startswith('composic'):
        return 'Composición'
    return cat_name


def search_songs(base_songs: List[Cancion], search_query: Optional[str]) -> Tuple[List[Cancion], str]:
    """
    Filtra una lista de canciones buscando coincidencias en título, música, letra,
    descripción o adaptación de forma insensible a mayúsculas y acentos.
    """
    if not search_query:
        return base_songs, ""

    normalized_search = unidecode(search_query.lower())
    filtered_songs = []

    for song in base_songs:
        full_text = ' '.join(filter(None, [
            song.titulo, song.musica, song.letra, song.descripcion, song.adaptacion
        ]))
        if normalized_search in unidecode(full_text.lower()):
            filtered_songs.append(song)

    return filtered_songs, search_query


def search_by_category(category_name: str) -> List[Cancion]:
    """
    Retorna todas las canciones asociadas a una categoría específica.
    """
    all_songs = Cancion.query.all()
    target_norm = unidecode(normalize_category_name(category_name).lower())
    result = []

    for song in all_songs:
        song_cats = [unidecode(normalize_category_name(cat).lower()) for cat in song.categorias]
        if target_norm in song_cats or any(target_norm in c for c in song_cats):
            result.append(song)

    return result


def sort_songs(songs: List[Cancion], sort_by: str = 'cronologico', main_category: Optional[str] = None) -> List[Cancion]:
    """
    Aplica el criterio de ordenación unificado sobre una lista de canciones (in-place y retorna lista):
    - 'canonico': Orden bíblico o litúrgico personalizado según main_category.
    - 'cronologico': Orden descendente por (año, mes, día), con desempate alfabético.
    - 'alfabetico': Orden alfabético estándar por título normalizado.
    """
    if main_category == "Cantos Bíblicos" and sort_by == 'canonico':
        def get_song_order_biblico(song: Cancion):
            cita_orden = parse_cita_biblica(song.letra)
            if cita_orden:
                return (cita_orden[0], cita_orden[1], cita_orden[2])
            for tag in song.tags:
                if tag.startswith(main_category + ':'):
                    parts = [p.strip() for p in tag.split(':')]
                    sub_tag = parts[1] if len(parts) > 1 else ''
                    orden_libro = ORDENES_PERSONALIZADOS[main_category].get(sub_tag, 999)
                    return (orden_libro, 0, 0)
            return (999, 0, 0)

        songs.sort(key=lambda s: (get_song_order_biblico(s), normalize_for_sorting(s.titulo)))

    elif main_category in ORDENES_PERSONALIZADOS and sort_by == 'canonico':
        orden_categoria = ORDENES_PERSONALIZADOS[main_category]

        def get_song_order(song: Cancion):
            min_order = 999
            for tag in song.tags:
                if tag.startswith(main_category + ':'):
                    parts = [p.strip() for p in tag.split(':')]
                    sub_tag = parts[1] if len(parts) > 1 else ''
                    order = orden_categoria.get(sub_tag, 999)
                    if order < min_order:
                        min_order = order
            return min_order

        songs.sort(key=lambda s: (get_song_order(s), normalize_for_sorting(s.titulo)))

    elif sort_by == 'cronologico':
        def get_song_order_cronologico(song: Cancion):
            anio = song.anio if song.anio is not None else 0
            mes = song.mes if song.mes is not None else 0
            dia = song.dia if song.dia is not None else 0
            return (anio, mes, dia)

        songs.sort(key=lambda s: (get_song_order_cronologico(s), normalize_for_sorting(s.titulo)), reverse=True)

    else:
        songs.sort(key=lambda s: normalize_for_sorting(s.titulo))

    return songs


def get_playlist_songs(
    context: str,
    tag_name: Optional[str] = None,
    search_query: Optional[str] = None,
    sort_by: str = 'cronologico',
    categoria: Optional[str] = None
) -> List[Cancion]:
    """
    Reconstruye la lista ordenada de canciones (playlist) según el contexto de navegación y filtros.
    """
    norm_cat = normalize_category_name(categoria) if categoria else None

    # 1. Conjunto base según contexto
    if norm_cat:
        base_songs = search_by_category(norm_cat)
    elif context == 'composiciones':
        base_songs = search_by_category("Composición")
    elif context == 'arreglos':
        base_songs = search_by_category("Arreglo")
    elif context == 'tag' and tag_name:
        all_songs = Cancion.query.all()
        base_songs = [s for s in all_songs if tag_matches(tag_name, s.tags)]
    else:
        base_songs = Cancion.query.all()

    # 2. Búsqueda de texto si aplica
    if search_query:
        base_songs, _ = search_songs(base_songs, search_query)

    # 3. Ordenamiento
    main_category = tag_name.split(':')[0].strip() if tag_name else None
    return sort_songs(base_songs, sort_by=sort_by, main_category=main_category)
