import json
from app import app, db, Cancion

def migrar_datos():
    with app.app_context():
        # Cargar datos desde el archivo JSON
        try:
            with open('data.json', 'r', encoding='utf-8') as f:
                composiciones = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            print("Error: No se pudo encontrar o leer el archivo 'data.json'.")
            return

        # Borra todas las tablas y las vuelve a crear para asegurar consistencia
        db.drop_all()
        db.create_all()
        
        for cancion_data in composiciones:
            nueva_cancion = Cancion(
                id=cancion_data.get('id'),
                titulo=cancion_data.get('titulo'),
                musica=cancion_data.get('musica'),
                letra=cancion_data.get('letra'),
                adaptacion=cancion_data.get('adaptacion'),
                idioma=cancion_data.get('idioma'),
                anio=cancion_data.get('anio'),
                descripcion=cancion_data.get('descripcion'),
                audio=cancion_data.get('audio'),
                letras_acordes=cancion_data.get('letras_acordes'),
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