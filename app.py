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
    idioma = db.Column(db.String(50))
    anio = db.Column(db.Integer)
    descripcion = db.Column(db.Text)
    audio = db.Column(db.String(150))
    partitura = db.Column(db.String(150))
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
        return json.loads(self.categorias_json) if self.categorias_json else []


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
        full_text = ' '.join(filter(None, [song.titulo, song.musica, song.letra, song.descripcion]))
        normalized_song_text = unidecode(full_text.lower())
        if normalized_search in normalized_song_text:
            filtered_songs.append(song)
    return filtered_songs, search_query

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
    base_songs = Cancion.query.all()
    filtered_songs, search_query = search_songs(base_songs)
    # CORRECCIÓN: Regla de ordenamiento personalizada
    filtered_songs.sort(key=lambda x: (0, x.titulo) if x.titulo.startswith('¡') else (1, x.titulo))
    return render_template('index.html', composiciones=filtered_songs, search_query=search_query)

@app.route('/composiciones')
def ver_composiciones():
    todas_las_canciones = Cancion.query.all()
    base_songs = [obra for obra in todas_las_canciones if 'Composición' in obra.categorias]
    filtered_songs, search_query = search_songs(base_songs)
    # CORRECCIÓN: Regla de ordenamiento personalizada
    filtered_songs.sort(key=lambda x: (0, x.titulo) if x.titulo.startswith('¡') else (1, x.titulo))
    return render_template('composiciones.html', composiciones=filtered_songs, search_query=search_query)

@app.route('/arreglos')
def ver_arreglos():
    todas_las_canciones = Cancion.query.all()
    base_songs = [obra for obra in todas_las_canciones if 'Arreglo' in obra.categorias]
    filtered_songs, search_query = search_songs(base_songs)
    # CORRECCIÓN: Regla de ordenamiento personalizada
    filtered_songs.sort(key=lambda x: (0, x.titulo) if x.titulo.startswith('¡') else (1, x.titulo))
    return render_template('arreglos.html', composiciones=filtered_songs, search_query=search_query)

@app.route('/tag/<tag_name>')
def ver_tag(tag_name):
    todas_las_canciones = Cancion.query.all()
    obras_con_tag = []
    if ':' not in tag_name:
        for obra in todas_las_canciones:
            for tag in obra.tags:
                if tag == tag_name or tag.startswith(tag_name + ':'):
                    obras_con_tag.append(obra)
                    break
    else:
        obras_con_tag = [obra for obra in todas_las_canciones if tag_name in obra.tags]
    filtered_songs, search_query = search_songs(obras_con_tag)
    # CORRECCIÓN: Regla de ordenamiento personalizada
    filtered_songs.sort(key=lambda x: (0, x.titulo) if x.titulo.startswith('¡') else (1, x.titulo))
    return render_template('vista_tag.html', composiciones=filtered_songs, tag_nombre=tag_name, search_query=search_query)

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
    obra_encontrada = Cancion.query.get_or_404(comp_id)
    comentarios_obra = Comentario.query.filter_by(obra_id=comp_id).order_by(Comentario.fecha_creacion.desc()).all()
    return render_template('composicion.html', obra=obra_encontrada, comentarios=comentarios_obra)

@app.route('/composicion/<int:comp_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_cancion(comp_id):
    cancion_a_editar = Cancion.query.get_or_404(comp_id)
    if request.method == 'POST':
        cancion_a_editar.titulo = request.form['titulo']
        cancion_a_editar.musica = request.form['musica']
        cancion_a_editar.letra = request.form['letra']
        cancion_a_editar.idioma = request.form['idioma']
        cancion_a_editar.anio = request.form['anio']
        cancion_a_editar.descripcion = request.form['descripcion']
        cancion_a_editar.audio = request.form['audio']
        cancion_a_editar.partitura = request.form['partitura']
        cancion_a_editar.tags_json = json.dumps([tag.strip() for tag in request.form['tags'].split(',') if tag.strip()])
        cancion_a_editar.categorias_json = json.dumps([cat.strip() for cat in request.form['categorias'].split(',') if cat.strip()])
        db.session.commit()
        return redirect(url_for('ver_composicion', comp_id=cancion_a_editar.id))
    return render_template('edit_cancion.html', cancion=cancion_a_editar)

@app.route('/composicion/<int:comp_id>/delete', methods=['POST'])
@login_required
def delete_cancion(comp_id):
    cancion_a_borrar = Cancion.query.get_or_404(comp_id)
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