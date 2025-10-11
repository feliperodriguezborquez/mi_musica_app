import os
from app import app, db, Cancion

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
        pdfs_disponibles = {f for f in os.listdir(media_path) if f.endswith('.pdf')}
        
        print("Iniciando sincronización de partituras PDF...")
        contador_actualizados = 0

        # Recorremos cada canción para verificar y corregir
        for cancion in canciones:
            # Solo actuamos si el campo de partitura está vacío
            if not cancion.partitura:
                # Construimos el nombre de archivo PDF que esperamos encontrar
                nombre_pdf_esperado = f"{cancion.titulo}.pdf"
                
                # Verificamos si ese archivo PDF realmente existe en nuestra carpeta
                if nombre_pdf_esperado in pdfs_disponibles:
                    ruta_completa_pdf = f"media/{nombre_pdf_esperado}"
                    cancion.partitura = ruta_completa_pdf
                    print(f"  - ACTUALIZANDO '{cancion.titulo}': Se asignó la partitura '{ruta_completa_pdf}'")
                    contador_actualizados += 1
                else:
                    print(f"  - AVISO: No se encontró '{nombre_pdf_esperado}' para la canción '{cancion.titulo}'.")
        
        # Si hicimos cambios, los guardamos en la base de datos
        if contador_actualizados > 0:
            db.session.commit()
            print(f"\n¡Sincronización completada! Se actualizaron {contador_actualizados} canciones.")
        else:
            print("\nNo se necesitaron actualizaciones. Todos los registros ya estaban correctos.")

if __name__ == '__main__':
    sincronizar()