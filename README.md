# 🎶 Catálogo Musical Personal

Un portafolio musical completo y extensible creado con Python y Flask para catalogar, reproducir y visualizar partituras y composiciones musicales.

### ➡️ [Ver Demo en Vivo en Render](https://mis-canciones.onrender.com/)

---

## ✨ Características Principales

- **Catálogo Unificado y Filtros:** 
  - Muestra composiciones y arreglos juntos o en vistas dedicadas (`/composiciones`, `/arreglos`).
  - Navegación jerárquica por etiquetas multinivel (`Categoría: Subcategoría: Subsubcategoría`).
- **Visualizador Interactivo de Partituras (MusicXML):**
  - Renderizado dinámico en el navegador usando **OpenSheetMusicDisplay (OSMD)**.
  - Zoom interactivo, cambio de orientación (paginada vs. horizontal) y modo pantalla completa.
  - **Selector de Instrumentos / Voces:** Permite silenciar o visualizar únicamente voces específicas (Soprano, Contralto, Tenor, Bajo, etc.).
  - Carga diferida y soporte para partituras y hojas de acordes en PDF.
- **Reproducción Multimedia Completa:**
  - Audio local directo (archivos MP3).
  - Reproductor embebido de YouTube (modo video o modo solo audio).
  - Integración para pistas corales y stems (*Cantāmus*).
- **Ordenamiento Inteligente y Canónico:**
  - **Canónico Bíblico:** Ordena automáticamente libros de la Biblia por su secuencia canónica (Génesis a Apocalipsis) seguido de capítulo y versículo.
  - **Canónico Litúrgico:** Secuencia litúrgica estándar (Adviento, Navidad, Cuaresma, Pascua, etc.) y partes fijas de la Santa Misa.
  - **Alfabético y Cronológico:** Ordenamiento instantáneo en cliente y servidor.
- **Navegación Persistente en Listas:**
  - Menú lateral en la ficha de cada obra que preserva el contexto de la lista filtrada.
  - Botones de "Anterior" y "Siguiente" sincronizados con el orden de búsqueda activo.
- **Interacción y Administración:**
  - Sistema de comentarios en cada obra.
  - Panel administrativo protegido por contraseña.
  - Tablero Kanban de ideas y proyectos musicales.

---

## 🏗️ Arquitectura Modular del Backend

La aplicación sigue una arquitectura modular en capas para facilitar el mantenimiento y la extensibilidad:

```
mi_musica_app/
├── app.py                     # Controlador Flask principal (rutas, endpoints y lifecycle)
├── models.py                  # Modelos SQLAlchemy (Cancion, Comentario, IdeaCancion)
├── constants.py               # Feature flags, mapeos canónicos de la Biblia y liturgias
├── services/                  # Capa de lógica de negocio y utilidades desacopladas
│   ├── __init__.py
│   ├── tag_service.py         # Procesamiento, jerarquización (:) y breadcrumbs de tags
│   └── catalog_service.py     # Búsquedas, ordenamiento canónico y listas de reproducción
├── data.json                  # Catálogo canónico serializado (fuente de verdad portable)
├── sincronizar_canciones.py   # Sincronización automática o manual data.json -> DB
├── export_to_json.py          # Exportación DB -> data.json
├── scripts/                   # Pipelines de procesamiento de audio y partituras
│   ├── cantamus_pipeline.py   # Procesamiento de stems corales
│   ├── mezclar_audio.py       # Mezclador automatizado
│   └── audit_scores.py        # Auditoría de archivos MusicXML
├── static/                    # Recursos estáticos (media MP3/MusicXML/PDF, CSS, JS)
├── templates/                 # Plantillas Jinja2 HTML
└── requirements.txt           # Dependencias de producción
```

---

## 🚀 Instalación y Ejecución Local

### Prerrequisitos
- Python 3.11 o superior.
- Git.

### Pasos

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/feliperodriguezborquez/mi_musica_app.git
   cd mi_musica_app
   ```

2. **Crear y activar un entorno virtual:**
   ```bash
   python -m venv .venv
   # En Windows:
   .venv\Scripts\activate
   # En macOS / Linux:
   source .venv/bin/activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno (opcional):**
   Crea un archivo `.env` en la raíz:
   ```ini
   SECRET_KEY=clave_secreta_para_sesiones
   ADMIN_PASSWORD=contraseña_para_panel_admin
   # DATABASE_URL=sqlite:///comentarios.db  (por defecto usa SQLite local)
   ```

5. **Iniciar la aplicación:**
   ```bash
   python app.py
   ```
   > Al iniciar, la aplicación crea las tablas en SQLite y ejecuta `sincronizar_canciones.py` para cargar automáticamente todas las obras desde `data.json`.

6. Abre tu navegador en **`http://127.0.0.1:5000`**.

---

## 🏷️ Sistema de Etiquetas (Taxonomía)

Las etiquetas de las canciones admiten jerarquías ilimitadas separadas por dos puntos (`:`). Esto permite navegación por carpetas y migas de pan automáticas en la interfaz:

- `Cantos Bíblicos: Salmos: Salmos Penitenciales`
- `Tiempos Litúrgicos: Cuaresma`
- `Santa Misa: Comunión`
- `Liturgia de las Horas: Laudes`

Al seleccionar una categoría padre (ej. `Cantos Bíblicos`), se muestran tanto los cantos directos como las subcategorías navegables en botones interactivos.

---

## 🛠️ Tecnologías

- **Backend:** Python, Flask, Flask-SQLAlchemy
- **Base de Datos:** SQLite (desarrollo local) / PostgreSQL (producción en Render)
- **Frontend:** HTML5, CSS3 moderno, JavaScript Vanilla, [OpenSheetMusicDisplay (OSMD)](https://opensheetmusicDisplay.org/)
- **Despliegue:** Render con Gunicorn