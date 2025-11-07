import json
from app import app, db, Cancion

def sincronizar_canciones_desde_json():
    """
    Sincroniza la base de datos con data.json.
    - Agrega canciones nuevas que no existen en la base de datos.
    - Actualiza las canciones existentes si sus datos en el JSON han cambiado.
    """
    with app.app_context():
        # 1. Cargar datos desde el archivo JSON
        try:
            with open('data.json', 'r', encoding='utf-8') as f:
                canciones_json = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            print("Error: No se pudo encontrar o leer el archivo 'data.json'.")
            return

        # 2. Obtener todas las canciones de la DB y ponerlas en un diccionario para acceso rápido
        canciones_en_db = {cancion.id: cancion for cancion in Cancion.query.all()}
        
        canciones_agregadas = 0
        canciones_actualizadas = 0
        
        # 3. Iterar sobre las canciones del JSON para agregar o actualizar
        for cancion_data in canciones_json:
            cancion_id = cancion_data.get('id')

            # Omitir si la canción no tiene ID en el JSON
            if cancion_id is None:
                print(f"ADVERTENCIA: Omitiendo registro sin ID: {cancion_data.get('titulo', '(título no encontrado)')}")
                continue

            # Procesar y normalizar datos del JSON
            dia = cancion_data.get('dia')
            mes = cancion_data.get('mes')
            anio = cancion_data.get('anio')
            
            # Campos que se compararán y asignarán
            datos_a_sincronizar = {
                'titulo': cancion_data.get('titulo'),
                'musica': cancion_data.get('musica'),
                'letra': cancion_data.get('letra'),
                'adaptacion': cancion_data.get('adaptacion'),
                'idioma': cancion_data.get('idioma'),
                'dia': int(dia) if dia else None,
                'mes': int(mes) if mes else None,
                'anio': int(anio) if anio else None,
                'descripcion': cancion_data.get('descripcion'),
                'audio': cancion_data.get('audio'),
                'letras_acordes': cancion_data.get('letras_acordes'),
                'partitura': cancion_data.get('partitura'),
                'tags_json': json.dumps(cancion_data.get('tags', [])),
                'tipo': cancion_data.get('tipo', 'local'),
                'categorias_json': json.dumps(cancion_data.get('categorias', [])),
                'youtube_video_embed': cancion_data.get('youtube_video_embed'),
                'youtube_audio_embed': cancion_data.get('youtube_audio_embed')
            }

            cancion_existente = canciones_en_db.get(cancion_id)

            if not cancion_existente:
                # La canción no existe en la DB, la agregamos
                nueva_cancion = Cancion(id=cancion_id, **datos_a_sincronizar)
                db.session.add(nueva_cancion)
                print(f"Agregando nueva canción: '{cancion_data.get('titulo')}' (ID: {cancion_id})")
                canciones_agregadas += 1
            else:
                # La canción existe, verificamos si hay cambios
                ha_cambiado = False
                for campo, valor_json in datos_a_sincronizar.items():
                    valor_db = getattr(cancion_existente, campo)
                    if valor_db != valor_json:
                        setattr(cancion_existente, campo, valor_json)
                        ha_cambiado = True
                
                if ha_cambiado:
                    print(f"Actualizando canción existente: '{cancion_data.get('titulo')}' (ID: {cancion_id})")
                    canciones_actualizadas += 1

        # 4. Si se agregaron o actualizaron canciones, guardar los cambios
        if canciones_agregadas > 0 or canciones_actualizadas > 0:
            db.session.commit()
            print(f"\n¡Sincronización completada! Se agregaron {canciones_agregadas} canciones nuevas y se actualizaron {canciones_actualizadas}.")
        else:
            print("\nNo se encontraron canciones nuevas o cambios para aplicar. La base de datos ya está actualizada.")

if __name__ == '__main__':
    sincronizar_canciones_desde_json()
