# 🎼 Pipeline de Producción Musical: De MuseScore a YouTube y Catálogo Web

Este documento define el flujo estándar, automatizado y repetible para producir y publicar cada composición/arreglo coral e instrumental: desde la partitura en **MuseScore 4**, pasando por la síntesis coral con **Cantāmus AI**, la mezcla con **MuseSounds**, hasta la creación del video para **YouTube** y la incorporación en el catálogo web **mi_musica_app**.

---

## 🧭 Resumen Rápido del Flujo

```
[ MuseScore 4 ]
   ├── (1) Script Cantamus One-Shot ────> .musicxml vocal ───> [ Cantāmus Web ] ───> Audio Voces (MP3/WAV)
   ├── (2) Exportar Audio Instrumental (MuseSounds, voces silenciadas) ──────────────┐
   │                                                                                 │
   │                                                                      [ scripts/mezclar_audio.py ]
   │                                                                                 │
   │                                                                                 ▼
   ├── (3) Exportar MusicXML completo (visor web) ──────────────────────> [ Audio Master Final ]
   ├── (4) Exportar PDF (descarga partitura)                                         │
   └── (5) Captura/Video de partitura (reproducción) ─────────────────────────┐       │
                                                                              ▼       ▼
                                                                     [ Editor de Video (YouTube) ]
                                                                              │
                                                                              ▼
                                                                     [ Subir a YouTube ]
                                                                              │
                                                                              ▼
                                                          [ Catálogo Web (mi_musica_app / data.json) ]
```

---

## 📋 Paso a Paso Detallado

### Fase 1: Síntesis Coral con Cantāmus AI

1. **Guardar la partitura en MuseScore 4** (local o en la nube de MuseScore).
2. **Ejecutar el preprocesador para Cantamus**:
   - Doble clic en `Procesar_Cantamus.bat` (o pedirlo en el chat / terminal):
     ```powershell
     .\.venv\Scripts\python.exe scripts\procesar_cantamus_one_shot.py
     ```
   - **Qué hace automáticamente:**
     - Detecta la partitura más reciente en la nube de MuseScore (`cloud_scores`) o en `Downloads`.
     - Extrae solo las cuerdas vocales (Soprano, Alto, Tenor, Bajo, Solistas), excluyendo instrumentos (guitarras, vientos, chelo, etc.).
     - Convierte a monofonía estricta (voz 1, elimina divisi que confunden a Cantamus).
     - Calibra el tempo real con el MIDI de MuseScore: aplica curvas de ritardando, cesuras y calderones.
     - Normaliza sinalefas y fusiona vocales en español.
     - Genera el archivo listo con sufijo `_Cantamus.musicxml` y lo copia a `Downloads\`.
3. **Subir a Cantāmus:**
   - Entra en [cantamus.app](https://cantamus.app/) y sube el archivo generado (`Nombre_Cantamus.musicxml`).
   - Elige el idioma (Español) y el ensamble.
   - Renderiza y descarga la pista de audio con todas las voces activas (ej. `Santo_Voces_Cantamus.mp3` o `.wav`).

---

### Fase 2: Instrumental MuseSounds en MuseScore 4

Para lograr la máxima calidad acústica y orquestal:
1. En **MuseScore 4**, abre el Mezclador pulsando `F10`.
2. **Silencia (Mute)** todas las pistas vocales (Soprano, Contralto, Tenor, Bajo, Solista).
3. Asegúrate de que las pistas instrumentales (flautas, cuerdas, guitarras, percusión) tengan asignadas las librerías **MuseSounds** (o SoundFonts preferidos).
4. Ve a **Archivo > Exportar...**:
   - Formato: **Audio MP3 (320 kbps)** o **WAV (48 kHz / 24-bit)**.
   - Guarda el archivo, ej.: `Santo_Instrumental.mp3`.

---

### Fase 3: Mezcla y Masterización Automática

Combina las voces hiperrealistas de Cantamus con el instrumental de MuseSounds:

1. **Parámetros acústicos clave aprendidos**:
   - **Realce vocal**: `+2.5 dB` (para que el texto litúrgico sea nítido frente al acompañamiento).
   - **Ganancia fija (evitar limitadores con release dinámico)**: Usar normalización de ganancia fija a `-1.0 dBFS` en lugar de compresores/limitadores automáticos agresivos que puedan amplificar ruido o distorsionar pasajes suaves.
   - **Ataque / Articulación de Cantāmus**: Cantāmus suele tener un pequeño retardo de articulación fonética (ataque de consonantes). Adelantar las voces unos **~50 ms** (o retrasar ~50 ms menos que el instrumental si se alinea a un video) hace que la dicción caiga justo sobre el pulso.

2. **Ejecutar mezcla directa**:
```powershell
.\.venv\Scripts\python.exe scripts\mezclar_audio.py --vocal "ruta\a\Santo_Voces_Cantamus.wav" --instrumental "ruta\a\Santo_Instrumental.wav"
```

---

### Fase 4: Creación del Video para YouTube (¡Exportación Directa MP4!)

> [!IMPORTANT]
> **No es necesario grabar pantalla con OBS ni armar diapositivas manuales**:
> MuseScore 4 permite exportar directamente el video con la partitura avanzando automáticamente.

1. **Exportar Video desde MuseScore 4**:
   - Ve a **Archivo > Exportar... > Video MP4 (`.mp4`)**.
   - Guarda el video en `Downloads` (ej. `Santo.mp4`).

2. **Diferencias de sincronización críticas a tener en cuenta**:
   - **El MP4 de MuseScore agrega ~3.04 segundos de silencio/cabecera inicial** antes del compás 1. En cambio, la exportación de audio instrumental (`.wav`/`.mp3`) suele iniciar casi de inmediato en $0.0\,\text{s}$.
   - Para que el audio instrumental calce perfecto con el video de MuseScore: **el instrumental requiere un delay de `+3.04 s`** (o ~`3040 ms`).
   - Para que las voces de Cantāmus sincronicen con el video: suelen requerir un retraso aproximado de **`+2.20 s` a `+2.25 s`** (los `+3.04 s` menos el desfase de silencio inicial de Cantāmus y el ajuste de articulación de ~50 ms).

3. **Muxing y Formato de Video (Evitar artefactos de compresión)**:
   - > [!WARNING]
     > **Cuidado con el codificador AAC nativo de FFmpeg**: Al comprimir mezclas vocales corales a AAC con bitrate estándar (128-320 kbps), el codificador suele generar artefactos audibles de chasquidos, siseos o sonido de "saliva / sólidos rozando" en frecuencias agudas (>6 kHz).
   - **Solución profesional recomendada**: Exportar el video final como **contenedor QuickTime MOV con audio PCM sin comprimir (`.mov`)**:
     ```powershell
     ffmpeg -i "Santo.mp4" -i "Santo_Master.wav" -map 0:v -map 1:a -c:v copy -c:a pcm_s16le -af apad -shortest "Santo_Cantamus_final_pcm.mov"
     ```
   - **YouTube acepta archivos `.mov` con audio PCM sin problemas** y los procesa con su propio transcodificador de alta gama sin generar esos ruidos extraños.

---

### Fase 5: Archivos para el Catálogo Web (`mi_musica_app`)

Para que la obra quede completa en el portafolio y visor interactivo:

1. **Exportar desde MuseScore (con todas las voces e instrumentos activos):**
   - **MusicXML sin comprimir**: Guardar en `static/media/Santo.musicxml` (para OpenSheetMusicDisplay).
   - **PDF de partitura general**: Guardar en `static/media/Santo.pdf` (para visor de descarga).
2. **Audio Master en la Web:**
   - Copiar el audio master a `static/media/Santo.mp3`.
3. **Sincronizar Letras Dinámicas (LRC / tiempos por compás):**
   ```powershell
   .\.venv\Scripts\python.exe scripts\extract_lyrics.py "static/media/Santo.musicxml" --part auto --apply <ID_CANCION>
   ```
4. **Registrar o Actualizar en `data.json`:**
   - Una vez subido el video a YouTube, añade el iframe o embed en `youtube_video_embed` (ej. `<iframe width="560" height="315" src="https://www.youtube.com/embed/VIDEO_ID" ...></iframe>`).
5. **Sincronizar Base de Datos:**
   ```powershell
   .\.venv\Scripts\python.exe sincronizar_canciones.py
   ```
