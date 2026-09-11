"""
Constantes globales de la aplicación: Taxonomía litúrgica, libros bíblicos y flags de features.
"""

import re

# ============================================================
# FEATURE FLAGS
# ============================================================
FEATURES = {
    'floating_player': True,   # Reproductor flotante estilo Spotify
    'autoplay':        True,   # Opción de auto-reproducción en perfil
    'category_pills':  True,   # Pestañas Todas/Composiciones/Arreglos
    'ideas_admin':     True,   # Tablero Kanban para gestión de ideas
    'cantamus':        True,   # Herramienta de optimización y mezcla para Cantamus
}

# ============================================================
# ORDEN CANÓNICO DE LIBROS DE LA BIBLIA
# ============================================================
ORDEN_LIBROS_BIBLIA = {
    # Antiguo Testamento
    "Génesis": 1, "Éxodo": 2, "Levítico": 3, "Números": 4, "Deuteronomio": 5, "Josué": 6, "Jueces": 7, "Rut": 8,
    "1 Samuel": 9, "2 Samuel": 10, "1 Reyes": 11, "2 Reyes": 12, "1 Crónicas": 13, "2 Crónicas": 14, "Esdras": 15,
    "Nehemías": 16, "Tobías": 17, "Judit": 18, "Ester": 19, "1 Macabeos": 20, "2 Macabeos": 21, "Job": 22, "Salmos": 23,
    "Proverbios": 24, "Eclesiastés": 25, "Cantar de los Cantares": 26, "Sabiduría": 27, "Eclesiástico": 28,
    "Isaías": 29, "Jeremías": 30, "Lamentaciones": 31, "Baruc": 32, "Ezequiel": 33, "Daniel": 34, "Oseas": 35,
    "Joel": 36, "Amós": 37, "Abdías": 38, "Jonás": 39, "Miqueas": 40, "Nahúm": 41, "Habacuc": 42, "Sofonías": 43,
    "Hageo": 44, "Zacarías": 45, "Malaquías": 46,
    # Nuevo Testamento
    "Mateo": 47, "Marcos": 48, "Lucas": 49, "Juan": 50, "Hechos de los Apóstoles": 51, "Romanos": 52,
    "1 Corintios": 53, "2 Corintios": 54, "Gálatas": 55, "Efesios": 56, "Filipenses": 57, "Colosenses": 58,
    "1 Tesalonicenses": 59, "2 Tesalonicenses": 60, "1 Timoteo": 61, "2 Timoteo": 62, "Tito": 63, "Filemón": 64,
    "Hebreos": 65, "Santiago": 66, "1 Pedro": 67, "2 Pedro": 68, "1 Juan": 69, "2 Juan": 70, "3 Juan": 71,
    "Judas": 72, "Apocalipsis": 73
}

# Mapeo de abreviaturas y variantes textuales al nombre canónico
MAPEO_LIBROS_BIBLIA = {
    # Antiguo Testamento
    'génesis': 'Génesis', 'gen': 'Génesis', 'gn': 'Génesis', 'éxodo': 'Éxodo', 'ex': 'Éxodo', 'levítico': 'Levítico', 'lv': 'Levítico',
    'números': 'Números', 'num': 'Números', 'nm': 'Números', 'deuteronomio': 'Deuteronomio', 'dt': 'Deuteronomio', 'josué': 'Josué', 'jos': 'Josué',
    'jueces': 'Jueces', 'jue': 'Jueces', 'rut': 'Rut', 'rt': 'Rut', '1 samuel': '1 Samuel', '1 sam': '1 Samuel', '1 sa': '1 Samuel',
    '2 samuel': '2 Samuel', '2 sam': '2 Samuel', '2 sa': '2 Samuel', '1 reyes': '1 Reyes', '1 re': '1 Reyes', '2 reyes': '2 Reyes', '2 re': '2 Reyes',
    '1 crónicas': '1 Crónicas', '1 cro': '1 Crónicas', '1 cr': '1 Crónicas', '2 crónicas': '2 Crónicas', '2 cro': '2 Crónicas', '2 cr': '2 Crónicas',
    'esdras': 'Esdras', 'esd': 'Esdras', 'nehemías': 'Nehemías', 'neh': 'Nehemías', 'tobías': 'Tobías', 'tob': 'Tobías', 'judit': 'Judit', 'jdt': 'Judit',
    'ester': 'Ester', 'est': 'Ester', '1 macabeos': '1 Macabeos', '1 mac': '1 Macabeos', '2 macabeos': '2 Macabeos', '2 mac': '2 Macabeos',
    'job': 'Job', 'jb': 'Job', 'salmos': 'Salmos', 'salmo': 'Salmos', 'Sal': 'Salmos', 'sal': 'Salmos', 'proverbios': 'Proverbios', 'prov': 'Proverbios', 'pr': 'Proverbios',
    'eclesiastés': 'Eclesiastés', 'ecl': 'Eclesiastés', 'qo': 'Eclesiastés', 'cantar de los cantares': 'Cantar de los Cantares', 'cant': 'Cantar de los Cantares',
    'sabiduría': 'Sabiduría', 'sab': 'Sabiduría', 'eclesiástico': 'Eclesiástico', 'eclo': 'Eclesiástico', 'si': 'Eclesiástico', 'isaías': 'Isaías', 'is': 'Isaías',
    'jeremías': 'Jeremías', 'jer': 'Jeremías', 'lamentaciones': 'Lamentaciones', 'lam': 'Lamentaciones', 'baruc': 'Baruc', 'bar': 'Baruc',
    'ezequiel': 'Ezequiel', 'ez': 'Ezequiel', 'daniel': 'Daniel', 'dan': 'Daniel', 'dn': 'Daniel', 'oseas': 'Oseas', 'os': 'Oseas', 'joel': 'Joel', 'jl': 'Joel',
    'amós': 'Amós', 'am': 'Amós', 'abdías': 'Abdías', 'abd': 'Abdías', 'jonás': 'Jonás', 'jon': 'Jonás', 'miqueas': 'Miqueas', 'miq': 'Miqueas',
    'nahúm': 'Nahúm', 'nah': 'Nahúm', 'habacuc': 'Habacuc', 'hab': 'Habacuc', 'sofonías': 'Sofonías', 'sof': 'Sofonías', 'hageo': 'Hageo', 'hag': 'Hageo',
    'zacarías': 'Zacarías', 'zac': 'Zacarías', 'malaquías': 'Malaquías', 'mal': 'Malaquías',
    # Nuevo Testamento
    'mateo': 'Mateo', 'mt': 'Mateo', 'marcos': 'Marcos', 'mc': 'Marcos', 'lucas': 'Lucas', 'lc': 'Lucas', 'juan': 'Juan', 'jn': 'Juan',
    'evangelios': 'Evangelios', 'hechos de los apóstoles': 'Hechos de los Apóstoles', 'hechos': 'Hechos de los Apóstoles', 'hch': 'Hechos de los Apóstoles',
    'romanos': 'Romanos', 'rom': 'Romanos', '1 corintios': '1 Corintios', '1 cor': '1 Corintios', '2 corintios': '2 Corintios', '2 cor': '2 Corintios',
    'gálatas': 'Gálatas', 'gal': 'Gálatas', 'efesios': 'Efesios', 'ef': 'Efesios', 'filipenses': 'Filipenses', 'flp': 'Filipenses',
    'colosenses': 'Colosenses', 'col': 'Colosenses', '1 tesalonicenses': '1 Tesalonicenses', '1 tes': '1 Tesalonicenses',
    '2 tesalonicenses': '2 Tesalonicenses', '2 tes': '2 Tesalonicenses', '1 timoteo': '1 Timoteo', '1 tim': '1 Timoteo',
    '2 timoteo': '2 Timoteo', '2 tim': '2 Timoteo', 'tito': 'Tito', 'tit': 'Tito', 'filemón': 'Filemón', 'flm': 'Filemón',
    'hebreos': 'Hebreos', 'heb': 'Hebreos', 'santiago': 'Santiago', 'stgo': 'Santiago', '1 pedro': '1 Pedro', '1 pe': '1 Pedro',
    '2 pedro': '2 Pedro', '2 pe': '2 Pedro', '1 juan': '1 Juan', '1 jn': '1 Juan', '2 juan': '2 Juan', '2 jn': '2 Juan',
    '3 juan': '3 Juan', '3 jn': '3 Juan', 'judas': 'Judas', 'jud': 'Judas', 'apocalipsis': 'Apocalipsis', 'ap': 'Apocalipsis'
}

# Expresión regular para detectar citas bíblicas (Ej: "Mt 13, 3 - 23", "Salmo 51 (50)")
CITA_REGEX = re.compile(
    r'((?:\d\s)?[A-Za-zÀ-ÿ\s]+?)\s*(\d+)(?:,\s*(\d+))?', 
    re.IGNORECASE
)

# ============================================================
# ORDENES LITÚRGICOS PERSONALIZADOS
# ============================================================
ORDEN_TIEMPOS_LITURGICOS = {
    "Adviento": 0, "Navidad": 1, "Cuaresma": 2, "Semana Santa": 3, 
    "Pascua": 4, "Pentecostés": 5, "Tiempo Ordinario": 6
}

ORDEN_SANTA_MISA = {
    "Entrada": 0, "Señor ten Piedad": 1, "Gloria": 2, "Salmo": 3, 
    "Aleluya": 4, "Ofertorio": 5, "Santo": 6, "Aclamación Memorial": 7,
    "Amén": 8, "Padre Nuestro": 9, "Cordero de Dios": 10, "Comunión": 11, "Salida": 12
}

ORDENES_PERSONALIZADOS = {
    "Tiempos Litúrgicos": ORDEN_TIEMPOS_LITURGICOS,
    "Santa Misa": ORDEN_SANTA_MISA,
    "Cantos Bíblicos": ORDEN_LIBROS_BIBLIA
}
