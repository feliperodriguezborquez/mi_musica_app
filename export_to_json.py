import json
from app import app, db, Cancion

def export_data_to_json():
    """
    Lee todas las canciones de la base de datos y las exporta a data.json.
    Esto es útil para inicializar el archivo JSON con los datos existentes
    que fueron modificados a través de la interfaz web.
    """
    with app.app_context():
        print("Iniciando exportación de la base de datos a data.json...")
        
        # 1. Obtener todas las canciones de la base de datos, ordenadas por ID
        todas_las_canciones = Cancion.query.order_by(Cancion.id).all()
        
        if not todas_las_canciones:
            print("La base de datos está vacía. No hay nada que exportar.")
            return

        lista_de_datos = []
        
        # 2. Convertir cada objeto Cancion a un diccionario con el formato correcto
        for cancion in todas_las_canciones:
            cancion_dict = {
                "id": cancion.id,
                "titulo": cancion.titulo,
                "musica": cancion.musica,
                "letra": cancion.letra,
                "adaptacion": cancion.adaptacion,
                "idioma": cancion.idioma,
                "anio": cancion.anio,
                "descripcion": cancion.descripcion,
                "audio": cancion.audio,
                "letras_acordes": cancion.letras_acordes,
                "partitura": cancion.partitura,
                "tags": cancion.tags,  # Usamos la property que ya convierte el JSON a lista
                "tipo": cancion.tipo,
                "categorias": cancion.categorias, # Usamos la property
                "youtube_video_embed": cancion.youtube_video_embed,
                "youtube_audio_embed": cancion.youtube_audio_embed
            }
            lista_de_datos.append(cancion_dict)
        
        # 3. Escribir la lista de diccionarios en el archivo data.json
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(lista_de_datos, f, ensure_ascii=False, indent=4)
            
        print(f"¡Éxito! Se han exportado {len(lista_de_datos)} canciones a data.json.")

if __name__ == '__main__':
    export_data_to_json()