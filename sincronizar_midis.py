# c:\Users\felip\OneDrive - uc.cl\Yo\IA\GitHub\mi_musica_app\sincronizar_midis.py
import os
from app import app, db, Cancion
import music21

def sincronizar_archivos_midi():
    """
    Revisa las canciones en la BD. Si una canción tiene un archivo MusicXML ('partitura')
    pero no un archivo MIDI ('midi'), lo convierte y actualiza la BD.
    """
    with app.app_context():
        canciones = Cancion.query.filter(Cancion.partitura != None, Cancion.partitura != '').all()
        
        media_path = os.path.join('static', 'media')
        if not os.path.exists(media_path):
            os.makedirs(media_path)
            
        print("Iniciando sincronización de archivos MIDI...")
        contador_actualizados = 0

        for cancion in canciones:
            # Solo actuar si el campo de midi está vacío pero el de partitura no
            if cancion.partitura and not cancion.midi:
                nombre_base, _ = os.path.splitext(os.path.basename(cancion.partitura))
                ruta_musicxml = os.path.join('static', cancion.partitura)
                
                nombre_midi = f"{nombre_base}.mid"
                ruta_midi_salida = os.path.join(media_path, nombre_midi)
                ruta_midi_db = f"media/{nombre_midi}"

                if not os.path.exists(ruta_musicxml):
                    print(f"  - ADVERTENCIA: No se encontró el archivo MusicXML '{ruta_musicxml}' para '{cancion.titulo}'. Saltando.")
                    continue

                try:
                    print(f"  - Convirtiendo '{ruta_musicxml}' a MIDI...")
                    # Cargar la partitura desde el archivo MusicXML
                    score = music21.converter.parse(ruta_musicxml)
                    # Escribir la partitura como un archivo MIDI
                    score.write('midi', fp=ruta_midi_salida)
                    
                    # Actualizar el registro en la base de datos
                    cancion.midi = ruta_midi_db
                    print(f"  - ÉXITO: Se creó '{ruta_midi_salida}' y se actualizó la BD para '{cancion.titulo}'.")
                    contador_actualizados += 1
                except Exception as e:
                    print(f"  - ERROR al procesar '{cancion.titulo}': {e}")
        
        if contador_actualizados > 0:
            db.session.commit()
            print(f"\n¡Sincronización MIDI completada! Se crearon y vincularon {contador_actualizados} archivos MIDI.")
        else:
            print("\nNo se necesitaron actualizaciones de MIDI. Todos los registros con partitura ya tenían un MIDI asociado.")

if __name__ == '__main__':
    print("Asegúrate de haber instalado 'music21' con: pip install music21")
    sincronizar_archivos_midi()
