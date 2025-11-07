from flask import Flask, render_template, abort, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
import datetime
import json
from functools import wraps
from collections import defaultdict
from unidecode import unidecode
import os # <-- Importamos la librería 'os'
from dotenv import load_dotenv # <-- Importamos la nueva librería

load_dotenv() # <-- Esto carga las variables del archivo .env

app = Flask(__name__)
# --- CONFIGURACIÓN DE SEGURIDAD ACTUALIZADA ---
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['ADMIN_PASSWORD'] = os.environ.get('ADMIN_PASSWORD')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comentarios.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# --- Modelos de la Base de Datos (sin cambios) ---
class Comentario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    obra_id = db.Column(db.Integer, nullable=False)
    autor = db.Column(db.String(80), nullable=False)
    contenido = db.Column(db.Text, nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.datetime.utcnow)

class Cancion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    musica = db.Column(db.String(100))
    letra = db.Column(db.String(100))
    adaptacion = db.Column(db.String(100))
    idioma = db.Column(db.String(50))
    dia = db.Column(db.Integer, nullable=True)
    mes = db.Column(db.Integer, nullable=True)
    anio = db.Column(db.Integer)
    descripcion = db.Column(db.Text)
    audio = db.Column(db.String(150))
    letras_acordes = db.Column(db.String(150)) # Antes 'partitura' (PDF)
    partitura = db.Column(db.String(150))      # Antes 'partitura_xml' (MusicXML)
    tags_json = db.Column(db.String(500))
    tipo = db.Column(db.String(50), nullable=False, default='local')
    categorias_json = db.Column(db.String(200))
    youtube_video_embed = db.Column(db.Text)
    youtube_audio_embed = db.Column(db.Text)
    @property
    def tags(self):
        return json.loads(self.tags_json) if self.tags_json else []
    @property
    def categorias(self):
        # Carga las categorías desde el JSON
        return json.loads(self.categorias_json) if self.categorias_json else []

@app.template_filter('sort_categories_for_page')
def sort_categories_for_page(categories, page_context='default'):
    """Filtro de Jinja para ordenar las categorías según la página."""
    sorted_cats = list(categories) # Crear una copia para no modificar la original
    if page_context == 'arreglos':
        # En la página de arreglos: Composición a la izquierda, Arreglo a la derecha
        sorted_cats.sort(key=lambda x: (x != 'Composición', x != 'Arreglo'))
    else:
        # Orden por defecto (index, composiciones, etc.): Arreglo a la izquierda, Composición a la derecha
        sorted_cats.sort(key=lambda x: (x != 'Arreglo', x != 'Composición'))
    return sorted_cats

# --- LÓGICA DE ORDENAMIENTO BÍBLICO AVANZADO ---
import re

# 1. Orden canónico completo de los libros de la Biblia.
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

# 2. Mapeo de abreviaturas y nombres alternativos al nombre canónico.
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

# 3. Expresión regular para encontrar citas bíblicas.
CITA_REGEX = re.compile(
    r'((?:\d\s)?[A-Za-zÀ-ÿ\s]+?)\s*(\d+)(?:,\s*(\d+))?', 
    re.IGNORECASE
)

def parse_cita_biblica(texto):
    """
    Busca una cita bíblica en un texto y devuelve una tupla para ordenar.
    Devuelve (orden_libro, capítulo, versículo) o None si no encuentra nada.
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

# --- LÓGICA DE ORDENAMIENTO PERSONALIZADO (CONSTANTES GLOBALES) ---
# Se mueven aquí para ser accesibles desde múltiples rutas.
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
    "Cantos Bíblicos": ORDEN_LIBROS_BIBLIA # Usamos el diccionario completo
}

# --- Lógica de Autenticación y Búsqueda (sin cambios) ---
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function

def search_songs(base_songs):
    search_query = request.args.get('search', '').strip()
    if not search_query:
        return base_songs, search_query
    normalized_search = unidecode(search_query.lower())
    filtered_songs = []
    for song in base_songs:
        full_text = ' '.join(filter(None, [song.titulo, song.musica, song.letra, song.descripcion, song.adaptacion]))
        normalized_song_text = unidecode(full_text.lower())
        if normalized_search in normalized_song_text:
            filtered_songs.append(song)
    return filtered_songs, search_query

def get_filtered_and_sorted_songs(base_query):
    """Aplica el filtro de búsqueda y el ordenamiento a una consulta de canciones."""
    all_songs = base_query.all()
    filtered_songs, search_query = search_songs(all_songs)
    filtered_songs.sort(key=lambda x: (0, x.titulo) if x.titulo.startswith('¡') else (1, x.titulo))
    return filtered_songs, search_query

def search_by_category(category_name):
    """
    Busca canciones por categoría de forma robusta, ignorando tildes.
    Devuelve una lista de canciones que coinciden.
    """
    all_songs = Cancion.query.all()
    normalized_category = unidecode(category_name.lower())
    return [
        song for song in all_songs if normalized_category in unidecode(str(song.categorias).lower())
    ]

def get_playlist_songs(context, tag_name=None, search_query=None, sort_by='canonico'):
    """
    Reconstruye la lista de canciones (playlist) basada en el contexto y los filtros.
    Devuelve una lista ordenada de objetos Cancion.
    """
    base_songs = []
    # 1. Obtener la lista base de canciones según el contexto
    if context == 'index':
        base_songs = Cancion.query.all()
    elif context == 'composiciones':
        base_songs = search_by_category("Composición")
    elif context == 'arreglos':
        base_songs = search_by_category("Arreglo")
    elif context == 'tag' and tag_name:
        all_songs = Cancion.query.all()
        if ':' not in tag_name:
            for song in all_songs:
                if any(tag.startswith(tag_name) for tag in song.tags):
                    base_songs.append(song)
        else:
            normalized_tag_name = tag_name.replace(" ", "").lower()
            for song in all_songs:
                if any(t.replace(" ", "").lower() == normalized_tag_name for t in song.tags):
                    base_songs.append(song)
    
    # 2. Aplicar filtro de búsqueda de texto si existe
    if search_query:
        normalized_search = unidecode(search_query.lower())
        songs_after_search = []
        for song in base_songs:
            full_text = ' '.join(filter(None, [song.titulo, song.musica, song.letra, song.descripcion, song.adaptacion]))
            if normalized_search in unidecode(full_text.lower()):
                songs_after_search.append(song)
        base_songs = songs_after_search

    # Extraemos la categoría principal para la lógica de ordenamiento
    main_category = tag_name.split(':')[0].strip() if tag_name else None

    # 3. Aplicar el ordenamiento solicitado
    if main_category == "Cantos Bíblicos" and sort_by == 'canonico':
        def get_song_order_biblico(song):
            cita_orden = parse_cita_biblica(song.letra)
            if cita_orden: return (cita_orden[0], cita_orden[1], cita_orden[2])
            for tag in song.tags:
                if tag.startswith(main_category + ':'):
                    sub_tag = tag.split(':', 1)[1].strip()
                    orden_libro = ORDENES_PERSONALIZADOS[main_category].get(sub_tag, 999)
                    return (orden_libro, 0, 0)
            return (999, 0, 0)
        base_songs.sort(key=lambda song: (get_song_order_biblico(song), (0, song.titulo) if song.titulo.startswith('¡') else (1, song.titulo)))

    elif main_category in ORDENES_PERSONALIZADOS and sort_by == 'canonico':
        orden_categoria = ORDENES_PERSONALIZADOS[main_category]
        def get_song_order(song):
            min_order = 999
            for tag in song.tags:
                if tag.startswith(main_category + ':'):
                    sub_tag = tag.split(':', 1)[1].strip()
                    order = orden_categoria.get(sub_tag, 999)
                    if order < min_order:
                        min_order = order
            return min_order
        base_songs.sort(key=lambda song: (get_song_order(song), (0, song.titulo) if song.titulo.startswith('¡') else (1, song.titulo)))
    
    else: # Orden alfabético por defecto para el resto
        base_songs.sort(key=lambda x: (0, x.titulo) if x.titulo.startswith('¡') else (1, x.titulo))
    
    return base_songs

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['password'] == app.config['ADMIN_PASSWORD']:
            session['logged_in'] = True
            flash('¡Has iniciado sesión correctamente!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Contraseña incorrecta.', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('Has cerrado sesión.', 'info')
    return redirect(url_for('index'))

# --- RUTAS PRINCIPALES (CON ORDENAMIENTO CORREGIDO) ---

@app.route('/')
def index():
    # 1. Obtener canciones y aplicar filtro de búsqueda de texto
    all_songs = Cancion.query.all()
    filtered_songs, search_query = search_songs(all_songs)
    
    # 2. Obtener el método de ordenamiento y aplicarlo
    sort_by = request.args.get('sort_by', 'alfabetico') # Por defecto, alfabético

    if sort_by == 'cronologico':
        def get_song_order_cronologico(song):
            anio = song.anio if song.anio is not None else float('inf')
            mes = song.mes if song.mes is not None else float('inf')
            dia = song.dia if song.dia is not None else float('inf')
            return (anio, mes, dia)
        filtered_songs.sort(key=lambda song: (get_song_order_cronologico(song), (0, song.titulo) if song.titulo.startswith('¡') else (1, song.titulo)))
    else: # 'alfabetico' o cualquier otro caso
        filtered_songs.sort(key=lambda x: (0, x.titulo) if x.titulo.startswith('¡') else (1, x.titulo))

    return render_template('index.html', composiciones=filtered_songs, search_query=search_query, page_context='index', sort_by=sort_by)

@app.route('/composiciones')
def ver_composiciones():
    # Usamos la nueva función de búsqueda por categoría
    base_songs = search_by_category("Composición")
    filtered_songs, search_query = search_songs(base_songs)
    filtered_songs.sort(key=lambda x: (0, x.titulo) if x.titulo.startswith('¡') else (1, x.titulo))
    return render_template('composiciones.html', composiciones=filtered_songs, search_query=search_query, page_context='composiciones')

@app.route('/arreglos')
def ver_arreglos():
    base_songs = search_by_category("Arreglo")
    filtered_songs, search_query = search_songs(base_songs)
    filtered_songs.sort(key=lambda x: (0, x.titulo) if x.titulo.startswith('¡') else (1, x.titulo))
    return render_template('arreglos.html', composiciones=filtered_songs, search_query=search_query, page_context='arreglos')

@app.route('/tag/<tag_name>')
def ver_tag(tag_name):
    all_songs = Cancion.query.all()
    matching_songs = []

    if ':' not in tag_name:
        # Si es una categoría principal (ej: "Tiempos Litúrgicos"), busca todas las canciones
        # que tengan cualquier tag que comience con ese nombre.
        for song in all_songs:
            if any(tag.startswith(tag_name) for tag in song.tags):
                matching_songs.append(song)
    else:
        # Si es una sub-etiqueta (ej: "Tiempos Litúrgicos:Pentecostés"), busca la coincidencia exacta.
        for song in all_songs:
            # Normalizamos ambas cadenas eliminando todos los espacios y convirtiendo a minúsculas
            # para una comparación a prueba de errores.
            normalized_tag_name = tag_name.replace(" ", "").lower()
            if any(t.replace(" ", "").lower() == normalized_tag_name for t in song.tags):
                 matching_songs.append(song)
    
    # Aplicamos el filtro de búsqueda de texto y el ordenamiento sobre las canciones encontradas
    filtered_songs, search_query = search_songs(matching_songs)
    
    # Obtenemos el método de ordenamiento desde la URL, por defecto 'canonico'
    sort_by = request.args.get('sort_by', 'canonico')
    
    # Extraemos la categoría principal para la lógica de ordenamiento
    main_category = tag_name.split(':')[0].strip()

    # --- LÓGICA DE ORDENAMIENTO DE CANCIONES DENTRO DE LA LISTA ---
    # Solo aplicamos la lógica si la categoría tiene un orden personalizado y el usuario lo ha elegido.
    if main_category == "Cantos Bíblicos" and sort_by == 'canonico':
        def get_song_order_biblico(song):
            # 1. Prioridad: Intentar parsear la cita desde el campo 'letra'.
            cita_orden = parse_cita_biblica(song.letra)
            if cita_orden:
                # Devuelve una tupla de orden muy específica: (orden_libro, capítulo, versículo)
                return (cita_orden[0], cita_orden[1], cita_orden[2])

            # 2. Fallback: Si no hay cita, usar el tag de la canción.
            for tag in song.tags:
                if tag.startswith(main_category + ':'):
                    sub_tag = tag.split(':', 1)[1].strip()
                    # Usamos el orden del libro, pero capítulo y versículo en 0.
                    orden_libro = ORDENES_PERSONALIZADOS[main_category].get(sub_tag, 999)
                    return (orden_libro, 0, 0)
            
            # 3. Último recurso: Si no tiene ni cita ni tag, va al final.
            return (999, 0, 0)

        # Ordena por la tupla de orden y luego por título
        filtered_songs.sort(key=lambda song: (get_song_order_biblico(song), (0, song.titulo) if song.titulo.startswith('¡') else (1, song.titulo)))

    elif main_category in ORDENES_PERSONALIZADOS and sort_by == 'canonico':
        orden_categoria = ORDENES_PERSONALIZADOS[main_category]
        
        def get_song_order(song):
            """
            Encuentra el valor de orden más bajo para una canción dentro de una categoría.
            Ej: Si una canción es de 'Adviento' y 'Navidad', usará el orden de 'Adviento'.
            """
            min_order = 999
            for tag in song.tags:
                if tag.startswith(main_category + ':'):
                    sub_tag = tag.split(':', 1)[1].strip()
                    order = orden_categoria.get(sub_tag, 999)
                    if order < min_order:
                        min_order = order
            return min_order

        # Ordena primero por el orden canónico y luego por título
        filtered_songs.sort(key=lambda song: (get_song_order(song), (0, song.titulo) if song.titulo.startswith('¡') else (1, song.titulo)))
    elif sort_by == 'cronologico':
        # Ordenamiento cronológico: año, mes, día. Los que no tienen fecha van al final.
        # El desempate final es por título.
        def get_song_order_cronologico(song):
            # Usamos un número muy grande para los valores nulos para que se vayan al final
            anio = song.anio if song.anio is not None else float('inf')
            mes = song.mes if song.mes is not None else float('inf')
            dia = song.dia if song.dia is not None else float('inf')
            return (anio, mes, dia)
        filtered_songs.sort(key=lambda song: (get_song_order_cronologico(song), (0, song.titulo) if song.titulo.startswith('¡') else (1, song.titulo)))
    else:
        # Ordenamiento alfabético estándar para el resto de las listas
        # o si el usuario eligió explícitamente 'alfabetico'.
        filtered_songs.sort(key=lambda x: (0, x.titulo) if x.titulo.startswith('¡') else (1, x.titulo))

    # Pasamos el método de ordenamiento actual a la plantilla
    return render_template('vista_tag.html', composiciones=filtered_songs, tag_nombre=tag_name, search_query=search_query, page_context='tag', sort_by=sort_by, ordenes_personalizados=ORDENES_PERSONALIZADOS.keys(), main_category=main_category)

@app.route('/get_playlist')
def get_playlist_partial():
    """
    Devuelve solo el HTML de la lista de canciones para ser cargado con AJAX.
    """
    context = request.args.get('context', 'index')
    tag_name = request.args.get('tag_name')
    search_query = request.args.get('search')
    sort_by = request.args.get('sort_by', 'canonico')
    playlist = get_playlist_songs(context, tag_name, search_query, sort_by)
    
    # Pasamos todos los parámetros de contexto a la plantilla parcial
    # para que los enlaces url_for() se generen correctamente.
    return render_template(
        '_song_list.html', 
        composiciones=playlist, 
        page_context=context, 
        tag_nombre=tag_name, 
        search_query=search_query, 
        sort_by=sort_by
    )

# --- Ruta para la búsqueda en vivo (con ordenamiento corregido) ---
@app.route('/filter')
def filter_songs():
    base_songs = Cancion.query.all()
    filtered_songs, _ = search_songs(base_songs)
    # CORRECCIÓN: Regla de ordenamiento personalizada
    filtered_songs.sort(key=lambda x: (0, x.titulo) if x.titulo.startswith('¡') else (1, x.titulo))
    return render_template('_song_list.html', composiciones=filtered_songs)

# --- Rutas de detalle, edición, etc. (sin cambios) ---
@app.route('/composicion/<int:comp_id>')
def ver_composicion(comp_id):
    # Obtenemos el contexto de la playlist desde los argumentos de la URL
    context = request.args.get('context', 'index')
    tag_name = request.args.get('tag_name')
    search_query = request.args.get('search')
    
    # Obtenemos el ordenamiento de la URL. Si no viene, usamos 'canonico' como default.
    sort_by = request.args.get('sort_by', 'canonico')

    # Reconstruimos la playlist
    playlist = get_playlist_songs(context, tag_name, search_query, sort_by)
    playlist_ids = [song.id for song in playlist]

    # Encontramos la posición de la canción actual
    try:
        current_index = playlist_ids.index(comp_id)
    except ValueError:
        current_index = -1

    # Determinamos las URLs de la canción anterior y siguiente
    prev_song_url = None
    if current_index > 0:
        prev_id = playlist_ids[current_index - 1]
        prev_song_url = url_for('ver_composicion', comp_id=prev_id, context=context, tag_name=tag_name, search=search_query, sort_by=sort_by)
    next_song_url = None
    if current_index != -1 and current_index < len(playlist_ids) - 1:
        next_id = playlist_ids[current_index + 1]
        next_song_url = url_for('ver_composicion', comp_id=next_id, context=context, tag_name=tag_name, search=search_query, sort_by=sort_by)

    # Generar un título dinámico para la playlist
    playlist_title = "Catálogo Completo"
    if context == 'composiciones':
        playlist_title = "Composiciones"
    elif context == 'arreglos':
        playlist_title = "Arreglos"
    elif context == 'tag' and tag_name:
        if ':' in tag_name:
            playlist_title = tag_name.split(':', 1)[1].strip()
        else:
            playlist_title = tag_name

    # Generar la URL para volver a la lista de reproducción
    playlist_url = url_for('index') # URL por defecto
    if context == 'composiciones':
        playlist_url = url_for('ver_composiciones', search=search_query, sort_by=sort_by)
    elif context == 'arreglos':
        playlist_url = url_for('ver_arreglos', search=search_query, sort_by=sort_by)
    elif context == 'tag' and tag_name:
        playlist_url = url_for('ver_tag', tag_name=tag_name, search=search_query, sort_by=sort_by)
    elif context == 'index':
         playlist_url = url_for('index', search=search_query, sort_by=sort_by)

    obra_encontrada = Cancion.query.get_or_404(comp_id)
    partitura_path = obra_encontrada.partitura

    comentarios_obra = Comentario.query.filter_by(obra_id=comp_id).order_by(Comentario.fecha_creacion.desc()).all()
    return render_template('composicion.html', obra=obra_encontrada, partitura_path=partitura_path, comentarios=comentarios_obra, prev_song_url=prev_song_url, next_song_url=next_song_url, playlist=playlist, playlist_title=playlist_title, playlist_url=playlist_url)

@app.route('/composicion/<int:comp_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_cancion(comp_id):
    cancion_a_editar = Cancion.query.get_or_404(comp_id)
    if request.method == 'POST':
        # Convertir campos vacíos a None para consistencia en la DB y JSON
        cancion_a_editar.titulo = request.form['titulo']
        cancion_a_editar.musica = request.form.get('musica') or None
        cancion_a_editar.letra = request.form.get('letra') or None
        cancion_a_editar.adaptacion = request.form.get('adaptacion') or None
        cancion_a_editar.idioma = request.form.get('idioma') or None
        anio_str = request.form.get('anio')
        cancion_a_editar.anio = int(anio_str) if anio_str else None
        cancion_a_editar.descripcion = request.form.get('descripcion') or None
        cancion_a_editar.audio = request.form.get('audio') or None
        cancion_a_editar.letras_acordes = request.form.get('letras_acordes') or None
        cancion_a_editar.partitura = request.form.get('partitura') or None

        cancion_a_editar.tags_json = json.dumps([tag.strip() for tag in request.form['tags'].split(',') if tag.strip()])
        processed_categorias = [cat.strip() for cat in request.form['categorias'].split(',') if cat.strip()]
        cancion_a_editar.categorias_json = json.dumps(processed_categorias)
        
        # 1. Guardar en la base de datos para reflejar el cambio inmediatamente
        db.session.commit()

        # 2. Actualizar el archivo data.json para persistir el cambio
        try:
            with open('data.json', 'r+', encoding='utf-8') as f:
                data = json.load(f)
                
                # Buscar la canción por ID y actualizarla
                for i, cancion_json in enumerate(data):
                    if cancion_json.get('id') == comp_id:
                        data[i]['titulo'] = cancion_a_editar.titulo
                        data[i]['musica'] = cancion_a_editar.musica
                        data[i]['letra'] = cancion_a_editar.letra
                        data[i]['adaptacion'] = cancion_a_editar.adaptacion
                        data[i]['idioma'] = cancion_a_editar.idioma
                        data[i]['anio'] = cancion_a_editar.anio
                        data[i]['descripcion'] = cancion_a_editar.descripcion
                        data[i]['audio'] = cancion_a_editar.audio
                        data[i]['letras_acordes'] = cancion_a_editar.letras_acordes
                        data[i]['partitura'] = cancion_a_editar.partitura
                        data[i]['tags'] = cancion_a_editar.tags # Usa la property que decodifica el JSON
                        data[i]['categorias'] = processed_categorias # Usa la lista procesada del formulario
                        break
                
                # Volver al inicio del archivo para sobrescribirlo
                f.seek(0)
                json.dump(data, f, ensure_ascii=False, indent=4)
                f.truncate()
        except (FileNotFoundError, json.JSONDecodeError) as e:
            flash(f'Error al guardar en data.json: {e}', 'danger')

        return redirect(url_for('ver_composicion', comp_id=cancion_a_editar.id))
    return render_template('edit_cancion.html', cancion=cancion_a_editar)

@app.route('/composicion/<int:comp_id>/delete', methods=['POST'])
@login_required
def delete_cancion(comp_id):
    cancion_a_borrar = Cancion.query.get_or_404(comp_id)

    # Borrar también del archivo JSON
    try:
        with open('data.json', 'r+', encoding='utf-8') as f:
            data = json.load(f)
            data_filtrada = [c for c in data if c.get('id') != comp_id]
            f.seek(0)
            json.dump(data_filtrada, f, ensure_ascii=False, indent=4)
            f.truncate()
    except (FileNotFoundError, json.JSONDecodeError) as e:
        flash(f'Error al borrar de data.json: {e}', 'danger')

    db.session.delete(cancion_a_borrar)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/listas')
def ver_listas():
    todas_las_canciones = Cancion.query.all()
    set_de_tags = set()
    for cancion in todas_las_canciones:
        for tag in cancion.tags:
            if tag and tag.strip():
                set_de_tags.add(tag)
    simple_tags = sorted([tag for tag in set_de_tags if ':' not in tag])
    hierarchical_tags = defaultdict(list)
    for tag in set_de_tags:
        if ':' in tag:
            categoria, sub_etiqueta = tag.split(':', 1)
            # Nos aseguramos de que la sub-etiqueta no esté vacía antes de añadirla
            sub_etiqueta_limpia = sub_etiqueta.strip()
            if sub_etiqueta_limpia:
                hierarchical_tags[categoria.strip()].append(sub_etiqueta_limpia)

    # Ordena las sub-etiquetas dentro de cada categoría
    for categoria in hierarchical_tags:
        if categoria in ORDENES_PERSONALIZADOS:
            orden = ORDENES_PERSONALIZADOS[categoria]
            # Para Cantos Bíblicos, las sub-etiquetas son los libros.
            # Usamos el nombre canónico para obtener el orden numérico.
            if categoria == "Cantos Bíblicos":
                 hierarchical_tags[categoria].sort(key=lambda libro: orden.get(MAPEO_LIBROS_BIBLIA.get(libro.lower(), libro), 999))
            else:
                hierarchical_tags[categoria].sort(key=lambda sub: orden.get(sub, 999))
        else:
            hierarchical_tags[categoria].sort() # Orden alfabético para el resto

    return render_template('listas.html', 
                           simple_tags=simple_tags, 
                           hierarchical_tags=dict(sorted(hierarchical_tags.items())))

@app.route('/composicion/<int:comp_id>/add_comment', methods=['POST'])
def add_comment(comp_id):
    autor = request.form.get('autor')
    contenido = request.form.get('contenido')
    if autor and contenido:
        nuevo_comentario = Comentario(obra_id=comp_id, autor=autor, contenido=contenido)
        db.session.add(nuevo_comentario)
        db.session.commit()
    return redirect(url_for('ver_composicion', comp_id=comp_id))

@app.route('/comment/<int:comment_id>/delete', methods=['POST'])
@login_required
def delete_comment(comment_id):
    # Busca el comentario por su ID o muestra un error 404 si no lo encuentra
    comentario_a_borrar = Comentario.query.get_or_404(comment_id)
    
    # Guardamos el ID de la canción para saber a dónde volver
    obra_id = comentario_a_borrar.obra_id
    
    # Borramos el comentario de la base de datos
    db.session.delete(comentario_a_borrar)
    db.session.commit()
    
    flash('Comentario borrado con éxito.', 'success')
    return redirect(url_for('ver_composicion', comp_id=obra_id))


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)