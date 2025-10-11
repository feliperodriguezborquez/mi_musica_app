import json
from app import app, db, Cancion # Importamos lo que necesitamos de nuestra app principal

# --- PEGA AQUÍ TU LISTA COMPLETA Y ANTIGUA DE 'composiciones' ---
composiciones = [
    {
        'id': 1, 'titulo': '¡Oh Bienvenido Seas!', 'musica': 'Felipe Rodríguez', 'letra': 'Liturgia de las Horas', 'idioma': 'Español', 'anio': 2024, 'descripcion': 'Canto de entrada para el tiempo de Adviento.', 'audio': 'media/¡Oh Bienvenido Seas!.mp3', 'partitura': 'media/¡Oh Bienvenido Seas!.pdf', 'tags': ['Liturgia de las Horas', 'Cantos Bíblicos'], 'tipo': 'local', 'categorias': ['Composición']
    },
    {
        'id': 2, 'titulo': 'De Profundis', 'musica': 'Felipe Rodríguez', 'letra': 'Salmo 130', 'idioma': 'Español', 'anio': 2024, 'descripcion': 'Musicalización del Salmo 130 (129).', 'audio': 'media/De Profundis.mp3', 'partitura': 'media/De Profundis.pdf', 'tags': ['Cantos Bíblicos'], 'tipo': 'local', 'categorias': ['Composición']
    },
    {
        'id': 3, 'titulo': 'Kyrie', 'musica': 'Felipe Rodríguez', 'letra': 'Ordinario de la Misa', 'idioma': 'Griego', 'anio': 2024, 'descripcion': 'Parte del ordinario de la Misa.', 'audio': 'media/Kyrie.mp3', 'partitura': 'media/Kyrie.pdf', 'tags': ['Santa Misa', 'Kyrie'], 'tipo': 'local', 'categorias': ['Composición']
    },
    {
        'id': 4, 'titulo': 'Santo', 'musica': 'Felipe Rodríguez', 'letra': 'Litúrgico', 'idioma': 'Español', 'anio': 2024, 'descripcion': 'El Sanctus, parte del ordinario de la Misa.', 'audio': 'media/Santo.mp3', 'partitura': 'media/Santo.pdf', 'tags': ['Santa Misa', 'Sanctus'], 'tipo': 'local', 'categorias': ['Composición']
    },
    {
        'id': 5, 'titulo': 'Señor, ten Piedad', 'musica': 'Felipe Rodríguez', 'letra': 'Litúrgico', 'idioma': 'Español', 'anio': 2024, 'descripcion': 'Versión en español del Kyrie eleison.', 'audio': 'media/Señor, ten Piedad.mp3', 'partitura': 'media/Señor, ten Piedad.pdf', 'tags': ['Santa Misa', 'Kyrie'], 'tipo': 'local', 'categorias': ['Composición']
    },
    {
        'id': 6, 'titulo': 'Pastores de Belén', 'musica': 'Felipe Rodríguez', 'letra': 'N/A', 'idioma': 'Instrumental', 'anio': 2024, 'descripcion': 'Composición y arreglo de "Pastores de Belén".', 'tags': ['Arreglos', 'Cantos Bíblicos', 'Grabaciones', 'YouTube'], 'tipo': 'youtube_selectable', 'youtube_video_embed': '<iframe width="560" height="315" src="https://www.youtube.com/embed/N-NbPumDRxA?si=rZMWWiTpZuCPNWV1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>', 'youtube_audio_embed': '<iframe width="560" height="315" src="https://www.youtube.com/embed/v_kBycuLVTY?si=4bygFyP_lJmSoR6_" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>', 'categorias': ['Composición', 'Arreglo']
    },
    {
        'id': 7, 'titulo': 'Mi Buen Pastor', 'musica': 'Hna. María Camila Chaparro', 'letra': 'Hna. María Camila Chaparro', 'idioma': 'Español', 'anio': 2024, 'descripcion': 'Arreglo del canto "Mi Buen Pastor" disponible en YouTube.', 'tags': ['Arreglos', 'Cantos Bíblicos', 'YouTube'], 'tipo': 'youtube_selectable', 'youtube_video_embed': '<iframe width="560" height="315" src="https://www.youtube.com/embed/wqtjGwHt9Mg?si=WGlx-BeH5jehGpbG" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>', 'youtube_audio_embed': '<iframe width="560" height="315" src="https://www.youtube.com/embed/wqtjGwHt9Mg?si=WGlx-BeH5jehGpbG" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>', 'categorias': ['Arreglo']
    },
    {
        'id': 8, 'titulo': 'Cristo en Todas las Almas', 'musica': 'Felipe Rodríguez', 'letra': 'Por definir', 'idioma': 'Español', 'anio': 2024, 'descripcion': 'Descripción de la obra.', 'audio': 'media/Cristo en Todas las Almas.mp3', 'partitura': None, 'tags': ['Por definir'], 'tipo': 'local', 'categorias': ['Composición']
    },
    {
        'id': 9, 'titulo': 'El Sembrador', 'musica': 'Felipe Rodríguez', 'letra': 'Por definir', 'idioma': 'Español', 'anio': 2024, 'descripcion': 'Descripción de la obra.', 'audio': 'media/El Sembrador.mp3', 'partitura': 'media/El Sembrador.pdf', 'tags': ['Por definir'], 'tipo': 'local', 'categorias': ['Composición']
    },
    {
        'id': 10, 'titulo': 'El Trigo y la Cizaña', 'musica': 'Felipe Rodríguez', 'letra': 'Por definir', 'idioma': 'Español', 'anio': 2024, 'descripcion': 'Descripción de la obra.', 'audio': 'media/El Trigo y la Cizaña.mp3', 'partitura': 'media/El Trigo y la Cizaña.pdf', 'tags': ['Por definir'], 'tipo': 'local', 'categorias': ['Composición']
    },
    {
        'id': 11, 'titulo': 'Emprenda la Esperanza Raudo Vuelo', 'musica': 'Felipe Rodríguez', 'letra': 'Por definir', 'idioma': 'Español', 'anio': 2024, 'descripcion': 'Descripción de la obra.', 'audio': 'media/Emprenda la Esperanza Raudo Vuelo.m4a', 'partitura': 'media/Emprenda la Esperanza Raudo Vuelo.pdf', 'tags': ['Por definir'], 'tipo': 'local', 'categorias': ['Composición']
    },
    {
        'id': 12, 'titulo': 'Esaú y Jacob', 'musica': 'Felipe Rodríguez', 'letra': 'Por definir', 'idioma': 'Español', 'anio': 2024, 'descripcion': 'Descripción de la obra.', 'audio': 'media/Esaú y Jacob.mp3', 'partitura': 'media/Esaú y Jacob.pdf', 'tags': ['Por definir'], 'tipo': 'local', 'categorias': ['Composición']
    },
    {
        'id': 13, 'titulo': 'Estate Señor Conmigo', 'musica': 'Felipe Rodríguez', 'letra': 'Por definir', 'idioma': 'Español', 'anio': 2024, 'descripcion': 'Descripción de la obra.', 'audio': 'media/Estate Señor Conmigo.m4a', 'partitura': 'media/Estate Señor Conmigo.pdf', 'tags': ['Por definir'], 'tipo': 'local', 'categorias': ['Composición']
    },
    {
        'id': 14, 'titulo': 'Invocación al Espíritu Santo', 'musica': 'Felipe Rodríguez', 'letra': 'Por definir', 'idioma': 'Español', 'anio': 2024, 'descripcion': 'Descripción de la obra.', 'audio': 'media/Invocación al Espíritu Santo.mp3', 'partitura': 'media/Invocación al Espíritu Santo.pdf', 'tags': ['Por definir'], 'tipo': 'local', 'categorias': ['Composición']
    },
    {
        'id': 15, 'titulo': 'La Esperanza', 'musica': 'Felipe Rodríguez', 'letra': 'Por definir', 'idioma': 'Español', 'anio': 2024, 'descripcion': 'Descripción de la obra.', 'audio': 'media/La Esperanza.m4a', 'partitura': 'media/La Esperanza.pdf', 'tags': ['Por definir'], 'tipo': 'local', 'categorias': ['Composición']
    },
    {
        'id': 16, 'titulo': 'La Palabra de Dios Crucificada', 'musica': 'Felipe Rodríguez', 'letra': 'Por definir', 'idioma': 'Español', 'anio': 2024, 'descripcion': 'Descripción de la obra.', 'audio': 'media/La Palabra de Dios Crucificada.mp3', 'partitura': 'media/La Palabra de Dios Crucificada.pdf', 'tags': ['Por definir'], 'tipo': 'local', 'categorias': ['Composición']
    },
    {
        'id': 17, 'titulo': 'Luz de Navidad', 'musica': 'Felipe Rodríguez', 'letra': 'Por definir', 'idioma': 'Español', 'anio': 2024, 'descripcion': 'Descripción de la obra.', 'audio': 'media/Luz de Navidad.mp3', 'partitura': None, 'tags': ['Por definir'], 'tipo': 'local', 'categorias': ['Composición']
    },
    {
        'id': 18, 'titulo': 'María', 'musica': 'Felipe Rodríguez', 'letra': 'Por definir', 'idioma': 'Español', 'anio': 2024, 'descripcion': 'Descripción de la obra.', 'audio': 'media/María.m4a', 'partitura': None, 'tags': ['Por definir'], 'tipo': 'local', 'categorias': ['Composición']
    },
    {
        'id': 19, 'titulo': 'Nos Apremia el Amor Vírgenes Santas', 'musica': 'Felipe Rodríguez', 'letra': 'Por definir', 'idioma': 'Español', 'anio': 2024, 'descripcion': 'Descripción de la obra.', 'audio': 'media/Nos Apremia el Amor Vírgenes Santas.mp3', 'partitura': 'media/Nos Apremia el Amor Vírgenes Santas.pdf', 'tags': ['Por definir'], 'tipo': 'local', 'categorias': ['Composición']
    },
    {
        'id': 20, 'titulo': 'Octavas de Pascua', 'musica': 'Felipe Rodríguez', 'letra': 'Por definir', 'idioma': 'Español', 'anio': 2024, 'descripcion': 'Descripción de la obra.', 'audio': 'media/Octavas de Pascua.mp3', 'partitura': 'media/Octavas de Pascua.pdf', 'tags': ['Por definir'], 'tipo': 'local', 'categorias': ['Composición']
    },
    {
        'id': 21, 'titulo': 'Oveja perdida Ven', 'musica': 'Felipe Rodríguez', 'letra': 'Por definir', 'idioma': 'Español', 'anio': 2024, 'descripcion': 'Descripción de la obra.', 'audio': 'media/Oveja perdida Ven.mp3', 'partitura': 'media/Oveja perdida Ven.pdf', 'tags': ['Por definir'], 'tipo': 'local', 'categorias': ['Composición']
    },
    {
        'id': 22, 'titulo': 'Rosa Mística', 'musica': 'Felipe Rodríguez', 'letra': 'Por definir', 'idioma': 'Español', 'anio': 2024, 'descripcion': 'Descripción de la obra.', 'audio': 'media/Rosa Mística.mp3', 'partitura': None, 'tags': ['Por definir'], 'tipo': 'local', 'categorias': ['Composición']
    },
    {
        'id': 23, 'titulo': 'Secuencia de Pascua', 'musica': 'Felipe Rodríguez', 'letra': 'Por definir', 'idioma': 'Español', 'anio': 2024, 'descripcion': 'Descripción de la obra.', 'audio': 'media/Secuencia de Pascua.mp3', 'partitura': 'media/Secuencia de Pascua.pdf', 'tags': ['Por definir'], 'tipo': 'local', 'categorias': ['Composición']
    },
    {
        'id': 24, 'titulo': 'Ven Señor Jesús', 'musica': 'Felipe Rodríguez', 'letra': 'Por definir', 'idioma': 'Español', 'anio': 2024, 'descripcion': 'Descripción de la obra.', 'audio': 'media/Ven Señor Jesús.mp3', 'partitura': 'media/Ven Señor Jesús.pdf', 'tags': ['Por definir'], 'tipo': 'local', 'categorias': ['Composición']
    }
]

def migrar_datos():
    with app.app_context():
        # Borramos los datos existentes para evitar duplicados si se corre de nuevo
        db.session.query(Cancion).delete()
        
        for cancion_data in composiciones:
            nueva_cancion = Cancion(
                id=cancion_data.get('id'),
                titulo=cancion_data.get('titulo'),
                musica=cancion_data.get('musica'),
                letra=cancion_data.get('letra'),
                idioma=cancion_data.get('idioma'),
                anio=cancion_data.get('anio'),
                descripcion=cancion_data.get('descripcion'),
                audio=cancion_data.get('audio'),
                partitura=cancion_data.get('partitura'),
                tags_json=json.dumps(cancion_data.get('tags', [])),
                tipo=cancion_data.get('tipo', 'local'),
                categorias_json=json.dumps(cancion_data.get('categorias', [])),
                youtube_video_embed=cancion_data.get('youtube_video_embed'),
                youtube_audio_embed=cancion_data.get('youtube_audio_embed')
            )
            db.session.add(nueva_cancion)
        
        db.session.commit()
        print("¡Migración de datos completada con éxito!")

if __name__ == '__main__':
    migrar_datos()