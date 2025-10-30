import json
from app import app, db, Cancion

def sincronizar_canciones_nuevas():
    """
    Sincroniza la base de datos con data.json, pero solo agrega las canciones que no existen.
    No borra ningún dato existente.
    """
    with app.app_context():
        # 1. Cargar datos desde el archivo JSON
        try:
            with open('data.json', 'r', encoding='utf-8') as f:
                canciones_json = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            print("Error: No se pudo encontrar o leer el archivo 'data.json'.")
            return

        # 2. Obtener todos los IDs de las canciones que ya están en la base de datos
        ids_en_db = {cancion.id for cancion in Cancion.query.all()}
        
        canciones_agregadas = 0
        
        # 3. Iterar sobre las canciones del JSON y agregar solo las nuevas
        for cancion_data in canciones_json:
            cancion_id = cancion_data.get('id')

            # --> NUEVA VERIFICACIÓN: Omitir si la canción no tiene ID en el JSON
            if cancion_id is None:
                print(f"ADVERTENCIA: Omitiendo registro sin ID: {cancion_data.get('titulo', '(título no encontrado)')}")
                continue

            # --> NUEVA VERIFICACIÓN: Convertir año vacío a None para evitar errores de tipo
            anio = cancion_data.get('anio')

            if cancion_id not in ids_en_db:
                nueva_cancion = Cancion(
                    id=cancion_data.get('id'),
                    titulo=cancion_data.get('titulo'),
                    musica=cancion_data.get('musica'),
                    letra=cancion_data.get('letra'),
                    adaptacion=cancion_data.get('adaptacion'),
                    idioma=cancion_data.get('idioma'),
                    anio=int(anio) if anio else None,
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
                print(f"Agregando nueva canción: '{cancion_data.get('titulo')}' (ID: {cancion_id})")
                canciones_agregadas += 1

        # 4. Si se agregaron canciones, guardar los cambios
        if canciones_agregadas > 0:
            db.session.commit()
            print(f"\n¡Sincronización completada! Se agregaron {canciones_agregadas} canciones nuevas.")
        else:
            print("\nNo se encontraron canciones nuevas para agregar. La base de datos ya está actualizada.")

if __name__ == '__main__':
    sincronizar_canciones_nuevas()
