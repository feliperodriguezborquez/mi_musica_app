from flask import Flask, render_template, abort, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import datetime

# ... tus otras importaciones ...
from werkzeug.middleware.proxy_fix import ProxyFix # <-- AÑADE ESTA LÍNEA

app = Flask(__name__)
# --- AÑADE ESTA LÍNEA JUSTO DESPUÉS DE INICIALIZAR LA APP ---
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)

# --- Configuración de la Base de Datos ---
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comentarios.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# --- Modelo de la Base de Datos para los Comentarios ---
class Comentario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    obra_id = db.Column(db.Integer, nullable=False)
    autor = db.Column(db.String(80), nullable=False)
    contenido = db.Column(db.Text, nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f'<Comentario {self.autor}>'

# --- Tu lista de composiciones ---
composiciones = [
    {
        'id': 1,
        'titulo': '¡Oh Bienvenido Seas!',
        'musica': 'Felipe Rodríguez',
        'letra': 'Liturgia de las Horas',
        'idioma': 'Español',
        'anio': 2024,
        'descripcion': 'Canto de entrada para el tiempo de Adviento.',
        'audio': 'media/¡Oh Bienvenido Seas!.mp3',
        'partitura': 'media/¡Oh Bienvenido Seas!.pdf',
        'tags': ['Liturgia de las Horas', 'Cantos Bíblicos'],
        'tipo': 'local',
        'categorias': ['Composición']
    },
    {
        'id': 2,
        'titulo': 'De Profundis',
        'musica': 'Felipe Rodríguez',
        'letra': 'Salmo 130',
        'idioma': 'Español',
        'anio': 2024,
        'descripcion': 'Musicalización del Salmo 130 (129).',
        'audio': 'media/De Profundis.mp3',
        'partitura': 'media/De Profundis.pdf',
        'tags': ['Cantos Bíblicos'],
        'tipo': 'local',
        'categorias': ['Composición']
    },
    {
        'id': 3,
        'titulo': 'Kyrie',
        'musica': 'Felipe Rodríguez',
        'letra': 'Ordinario de la Misa',
        'idioma': 'Griego',
        'anio': 2024,
        'descripcion': 'Parte del ordinario de la Misa.',
        'audio': 'media/Kyrie.mp3',
        'partitura': 'media/Kyrie.pdf',
        'tags': ['Santa Misa', 'Kyrie'],
        'tipo': 'local',
        'categorias': ['Composición']
    },
    {
        'id': 4,
        'titulo': 'Santo',
        'musica': 'Felipe Rodríguez',
        'letra': 'Litúrgico',
        'idioma': 'Español',
        'anio': 2024,
        'descripcion': 'El Sanctus, parte del ordinario de la Misa.',
        'audio': 'media/Santo.mp3',
        'partitura': 'media/Santo.pdf',
        'tags': ['Santa Misa', 'Sanctus'],
        'tipo': 'local',
        'categorias': ['Composición']
    },
    {
        'id': 5,
        'titulo': 'Señor, ten Piedad',
        'musica': 'Felipe Rodríguez',
        'letra': 'Litúrgico',
        'idioma': 'Español',
        'anio': 2024,
        'descripcion': 'Versión en español del Kyrie eleison.',
        'audio': 'media/Señor, ten Piedad.mp3',
        'partitura': 'media/Señor, ten Piedad.pdf',
        'tags': ['Santa Misa', 'Kyrie'],
        'tipo': 'local',
        'categorias': ['Composición']
    },
    {
        'id': 6,
        'titulo': 'Pastores de Belén',
        'musica': 'Felipe Rodríguez',
        'letra': 'N/A',
        'idioma': 'Instrumental',
        'anio': 2024,
        'descripcion': 'Composición y arreglo de "Pastores de Belén".',
        'tags': ['Arreglos', 'Cantos Bíblicos', 'Grabaciones', 'YouTube'],
        'tipo': 'youtube_selectable',
        'youtube_video_embed': '<iframe width="560" height="315" src="https://www.youtube.com/embed/N-NbPumDRxA?si=rZMWWiTpZuCPNWV1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>',
        'youtube_audio_embed': '<iframe width="560" height="315" src="https://www.youtube.com/embed/v_kBycuLVTY?si=4bygFyP_lJmSoR6_" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>',
        'categorias': ['Composición', 'Arreglo']
    },
    {
        'id': 7,
        'titulo': 'Mi Buen Pastor',
        'musica': 'Hna. María Camila Chaparro',
        'letra': 'Hna. María Camila Chaparro',
        'idioma': 'Español',
        'anio': 2024,
        'descripcion': 'Arreglo del canto "Mi Buen Pastor" disponible en YouTube.',
        'tags': ['Arreglos', 'Cantos Bíblicos', 'YouTube'],
        'tipo': 'youtube_selectable',
        'youtube_video_embed': '<iframe width="560" height="315" src="https://www.youtube.com/embed/wqtjGwHt9Mg?si=WGlx-BeH5jehGpbG" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>',
        'youtube_audio_embed': '<iframe width="560" height="315" src="https://www.youtube.com/embed/wqtjGwHt9Mg?si=WGlx-BeH5jehGpbG" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>',
        'categorias': ['Arreglo']
    }
]

# --- Rutas de la Aplicación ---
@app.route('/')
def index():
    return render_template('index.html', composiciones=composiciones)

@app.route('/composiciones')
def ver_composiciones():
    obras_composiciones = [
        obra for obra in composiciones if 'Composición' in obra.get('categorias', [])
    ]
    return render_template('composiciones.html', obras=obras_composiciones)

# --- ESTA ES LA ÚNICA Y CORRECTA VERSIÓN DE 'ver_composicion' ---
@app.route('/composicion/<int:comp_id>')
def ver_composicion(comp_id):
    obra_encontrada = next((obra for obra in composiciones if obra['id'] == comp_id), None)
    if obra_encontrada is None:
        abort(404)
    
    # Buscamos los comentarios para esta obra en la base de datos
    comentarios_obra = Comentario.query.filter_by(obra_id=comp_id).order_by(Comentario.fecha_creacion.desc()).all()
    
    return render_template('composicion.html', obra=obra_encontrada, comentarios=comentarios_obra)

@app.route('/composicion/<int:comp_id>/add_comment', methods=['POST'])
def add_comment(comp_id):
    autor = request.form.get('autor')
    contenido = request.form.get('contenido')

    if autor and contenido:
        nuevo_comentario = Comentario(obra_id=comp_id, autor=autor, contenido=contenido)
        db.session.add(nuevo_comentario)
        db.session.commit()

    return redirect(url_for('ver_composicion', comp_id=comp_id))

@app.route('/tag/<tag_name>')
def ver_tag(tag_name):
    obras_con_tag = [obra for obra in composiciones if tag_name in obra.get('tags', [])]
    return render_template('vista_tag.html', obras=obras_con_tag, tag_nombre=tag_name)

@app.route('/listas')
def ver_listas():
    listas_principales = ['Cantos Bíblicos', 'Liturgia de las Horas', 'Santa Misa', 'Arreglos', 'Grabaciones', 'YouTube']
    momentos_liturgicos = ['Kyrie', 'Sanctus']
    return render_template('listas.html', 
                           listas_principales=listas_principales, 
                           momentos_liturgicos=momentos_liturgicos)

@app.route('/arreglos')
def ver_arreglos():
    obras_arreglos = [obra for obra in composiciones if 'Arreglos' in obra.get('tags', [])]
    return render_template('arreglos.html', obras=obras_arreglos)


# --- Comando para crear la base de datos ---
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)