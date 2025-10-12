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

def get_playlist_songs(context, tag_name=None, search_query=None):
    """
    Reconstruye la lista de canciones (playlist) basada en el contexto y los filtros.
    Devuelve una lista ordenada de objetos Cancion.
    """
    base_songs = []
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
    
    # Aplicar filtro de búsqueda si existe
    if search_query:
        normalized_search = unidecode(search_query.lower())
        songs_after_search = []
        for song in base_songs:
            full_text = ' '.join(filter(None, [song.titulo, song.musica, song.letra, song.descripcion, song.adaptacion]))
            if normalized_search in unidecode(full_text.lower()):
                songs_after_search.append(song)
        base_songs = songs_after_search

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
    filtered_songs, search_query = get_filtered_and_sorted_songs(Cancion.query)
    return render_template('index.html', composiciones=filtered_songs, search_query=search_query, page_context='index')

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
    filtered_songs.sort(key=lambda x: (0, x.titulo) if x.titulo.startswith('¡') else (1, x.titulo))
    return render_template('vista_tag.html', composiciones=filtered_songs, tag_nombre=tag_name, search_query=search_query, page_context='tag')

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

    # Reconstruimos la playlist
    playlist = get_playlist_songs(context, tag_name, search_query)
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
        prev_song_url = url_for('ver_composicion', comp_id=prev_id, context=context, tag_name=tag_name, search=search_query)
    next_song_url = None
    if current_index != -1 and current_index < len(playlist_ids) - 1:
        next_id = playlist_ids[current_index + 1]
        next_song_url = url_for('ver_composicion', comp_id=next_id, context=context, tag_name=tag_name, search=search_query)

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
        playlist_url = url_for('ver_composiciones', search=search_query)
    elif context == 'arreglos':
        playlist_url = url_for('ver_arreglos', search=search_query)
    elif context == 'tag' and tag_name:
        playlist_url = url_for('ver_tag', tag_name=tag_name, search=search_query)
    elif context == 'index':
         playlist_url = url_for('index', search=search_query)

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
            hierarchical_tags[categoria.strip()].append(sub_etiqueta.strip())
    for categoria in hierarchical_tags:
        hierarchical_tags[categoria].sort()
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