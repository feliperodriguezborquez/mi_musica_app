import os
from app import app, db, Cancion
from unidecode import unidecode

def sincronizar():
    """
    Este script revisa todas las canciones locales en la base de datos.
    Si una canción no tiene una partitura asignada, busca un PDF con el mismo
    nombre que el título de la canción en la carpeta static/media y actualiza el registro.
    """
    with app.app_context():
        # Obtenemos todas las canciones de la base de datos
        canciones = Cancion.query.filter_by(tipo='local').all()
        
        # Obtenemos la lista de todos los archivos PDF que realmente existen en la carpeta
        media_path = os.path.join('static', 'media')
        # Normalizamos los nombres de archivo para una comparación más robusta
        pdfs_disponibles = {
            unidecode(f.lower()): f for f in os.listdir(media_path) if f.lower().endswith('.pdf')
        }
        
        print("Iniciando sincronización de 'Letras y Acordes' (PDF)...")
        contador_actualizados = 0

        # Recorremos cada canción para verificar y corregir
        for cancion in canciones:
            # Solo actuamos si el campo de letras_acordes (PDF) está vacío
            if not cancion.letras_acordes:
                # Construimos el nombre de archivo PDF que esperamos encontrar
                # Normalizamos también el título para la búsqueda
                nombre_pdf_esperado_normalizado = unidecode(f"{cancion.titulo}.pdf".lower())
                
                # Verificamos si ese archivo PDF realmente existe en nuestra carpeta
                if nombre_pdf_esperado_normalizado in pdfs_disponibles:
                    nombre_real_archivo = pdfs_disponibles[nombre_pdf_esperado_normalizado]
                    ruta_completa_pdf = f"media/{nombre_real_archivo}"
                    cancion.letras_acordes = ruta_completa_pdf
                    print(f"  - ACTUALIZANDO '{cancion.titulo}': Se asignó el PDF '{ruta_completa_pdf}'")
                    contador_actualizados += 1
        
        # Si hicimos cambios, los guardamos en la base de datos
        if contador_actualizados > 0:
            db.session.commit()
            print(f"\n¡Sincronización completada! Se actualizaron {contador_actualizados} canciones.")
        else:
            print("\nNo se necesitaron actualizaciones. Todos los registros ya estaban correctos.")

if __name__ == '__main__':
    sincronizar()