# Instrucciones del Proyecto: mi_musica_app

## Pipeline de Producción Musical
El flujo completo de exportación y producción está documentado detalladamente en [PIPELINE_PRODUCCION.md](file:///c:/Users/felip/OneDrive%20-%20uc.cl/Yo/IA/GitHub/mi_musica_app/PIPELINE_PRODUCCION.md).

### Reglas Clave:
1. **Exportación Cantamus**:
   - Cuando el usuario pida exportar una partitura para Cantamus o diga que guardó una en MuseScore, ejecutar directamente:
     ```powershell
     .\.venv\Scripts\python.exe scripts\procesar_cantamus_one_shot.py
     ```
   - El script detecta la partitura más reciente en la nube de MuseScore (`cloud_scores`) o en `Downloads`, filtra cuerdas vocales, normaliza fonética/sinalefas, bakea curvas de tempo/ritardando y genera el archivo `*_Cantamus.musicxml`.
   - Copiar el archivo generado a `C:\Users\felip\Downloads\<Nombre>_Cantamus.musicxml` para fácil acceso.

2. **Mezcla Master (Cantamus + MuseSounds)**:
   - Combinar el audio vocal de Cantamus con el instrumental de MuseSounds usando:
     ```powershell
     .\.venv\Scripts\python.exe scripts\mezclar_audio.py --vocal "<vocal.wav>" --instrumental "<instrumental.wav>"
     ```
   - Ganancia recomendada: `+2.5 dB` vocal, con ganancia fija a `-1.0 dBFS` (evitar limitadores dinámicos que distorsionan).
   - Para alinear con el video MP4 exportado directamente de MuseScore:
     - El video tiene un silencio inicial de `~3.04 s`. El instrumental debe demorarse `+3.04 s`.
     - Cantāmus tiene retraso de articulación de consonantes; debe adelantarse `~50 ms` respecto a la alineación matemática (típicamente `+2.20 s` de delay frente al inicio del video).

3. **Video para YouTube**:
   - Se exporta el video de la partitura directamente desde MuseScore (`Archivo > Exportar > Video MP4`).
   - Muxear siempre a **QuickTime MOV con PCM sin comprimir (`.mov`)** para evitar artefactos del encoder AAC de FFmpeg (ruidos de "saliva / chasquidos"):
     ```powershell
     ffmpeg -i "<score.mp4>" -i "<master.wav>" -map 0:v -map 1:a -c:v copy -c:a pcm_s16le -af apad -shortest "<output>_Cantamus_final_pcm.mov"
     ```

4. **Archivos para el Catálogo Web**:
   - Partitura completa OSMD: `static/media/<Titulo>.musicxml`
   - Partitura imprimible: `static/media/<Titulo>.pdf`
   - Audio final: `static/media/<Titulo>.mp3`
   - Sincronización de letras: `scripts/extract_lyrics.py "static/media/<Titulo>.musicxml" --part auto --apply <ID>`
   - Incrustación YouTube: guardar `<iframe>` en `data.json` y sincronizar DB: `.\.venv\Scripts\python.exe sincronizar_canciones.py`
