from flask import Flask, render_template, abort

app = Flask(__name__)

# --- Base de Datos (en una lista de diccionarios por ahora) ---
# Cada diccionario es una de tus composiciones.
# Más adelante, esto podría venir de una base de datos real.
composiciones = [
    {
        'id': 1,
        'titulo': 'Nocturno en Eb Mayor',
        'compositor': 'F. Chopin',
        'anio': 1832,
        'descripcion': 'Una pieza melancólica y expresiva para piano solo, Op. 9 No. 2.',
        'audio': 'chopin_nocturne.mp3', # Nombre del archivo de audio
        'portada': 'chopin.jpg'        # Nombre de la imagen de portada
    },
    {
        'id': 2,
        'titulo': 'Claro de Luna',
        'compositor': 'L. van Beethoven',
        'anio': 1801,
        'descripcion': 'El primer movimiento de la Sonata para Piano No. 14, famoso por su atmósfera misteriosa.',
        'audio': 'moonlight_sonata.mp3',
        'portada': 'beethoven.jpg'
    },
    {
        'id': 3,
        'titulo': 'El Verano (Presto)',
        'compositor': 'A. Vivaldi',
        'anio': 1725,
        'descripcion': 'El enérgico tercer movimiento del concierto "Verano" de Las Cuatro Estaciones.',
        'audio': 'vivaldi_summer.mp3',
        'portada': 'vivaldi.jpg'
    }
]

# --- Rutas de la Aplicación ---

# Ruta para la página principal: Muestra la lista de todas las obras
@app.route('/')
def index():
    # 'render_template' busca en la carpeta 'templates' el archivo que le pidas.
    # Le pasamos la lista completa de composiciones para que la use en el HTML.
    return render_template('index.html', composiciones=composiciones)

# Ruta para ver una composición individual. Es una ruta dinámica.
@app.route('/composicion/<int:comp_id>')
def ver_composicion(comp_id):
    # Buscamos en nuestra lista la composición que tenga el 'id' correcto.
    obra_encontrada = next((obra for obra in composiciones if obra['id'] == comp_id), None)
    
    if obra_encontrada is None:
        # Si no se encuentra una obra con ese ID, muestra un error 404.
        abort(404)
        
    # Si la encontramos, le pasamos sus datos a la plantilla 'composicion.html'.
    return render_template('composicion.html', obra=obra_encontrada)

if __name__ == '__main__':
    app.run(debug=True) # debug=True te ayuda a ver errores mientras desarrollas