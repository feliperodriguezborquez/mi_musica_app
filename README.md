# 🎶 Catálogo Musical Personal

Un portafolio musical personal creado con Python y Flask para organizar y mostrar composiciones y arreglos.

### ➡️ [Ver Demo en Vivo](https://mis-canciones.onrender.com/)

## ✨ Características

- **Catálogo Unificado:** Muestra composiciones y arreglos en una sola lista principal.
- **Vistas Dedicadas:** Secciones separadas para `Composiciones` y `Arreglos`.
- **Reproducción Multimedia:** Soporte para audio local y reproductores de Audio/Video seleccionables desde YouTube.
- **Visualizador Interactivo de Partituras (MusicXML):**
    - Renderizado de partituras MusicXML usando **OpenSheetMusicDisplay (OSMD)**.
    - Controles de **zoom**, cambio de vista (paginada/horizontal) y modo **pantalla completa**.
    - **Selección de Instrumentos:** Filtra y muestra solo las voces o instrumentos que desees ver.
    - Carga diferida para un rendimiento óptimo.
- **Ordenamiento Avanzado:**
    - **Orden Canónico:** Ordena automáticamente las listas litúrgicas (Tiempos, partes de la Misa) y los cantos bíblicos (por libro, capítulo y versículo).
    - **Orden Alfabético:** Opción para ordenar las listas alfabéticamente.
    - El orden se actualiza dinámicamente sin recargar la página.
- **Navegación Persistente:**
    - Un **menú lateral** en la vista de canción mantiene el contexto de la lista de reproducción actual.
    - Navegación entre la canción **anterior y siguiente** dentro de la lista filtrada y ordenada.
- **Sistema de Comentarios:** Permite a los visitantes dejar comentarios en cada obra.
- **Autenticación de Administrador:** Área protegida por contraseña para editar o borrar contenido.
- **Scripts de Sincronización:** Utilidades para migrar la base de datos desde un `JSON` y sincronizar archivos PDF automáticamente.

## 🛠️ Tecnologías

- **Backend:** Python, Flask, Flask-SQLAlchemy
- **Base de Datos:** SQLite
- **Frontend:** HTML, CSS, JavaScript, OpenSheetMusicDisplay (OSMD)
- **Despliegue:** Render

## 🚀 Instalación Local

Para ejecutar este proyecto en tu propia máquina, sigue estos pasos:

```bash
# 1. Clona el repositorio
git clone https://github.com/f-rod/mi_musica_app.git
cd mi_musica_app

# 2. Crea y activa el entorno virtual
python -m venv venv
# En Windows: .\\venv\\Scripts\\activate
# En macOS/Linux: source venv/bin/activate

# 3. Instala las dependencias desde requirements.txt
pip install -r requirements.txt

# 4. (Opcional) Crea un archivo .env para las variables de entorno
# SECRET_KEY='una_clave_secreta_muy_larga_y_dificil'
# ADMIN_PASSWORD='tu_contraseña_de_admin'

# 5. (Opcional) Si es la primera vez, migra los datos desde data.json
python migrar_db.py

# 6. Ejecuta la aplicación
flask run
```

La aplicación estará disponible en `http://127.0.0.1:5000`.

## 📂 Estructura del Proyecto

```
mi_musica_app/
├── static/
│   ├── media/
│   └── style.css
├── templates/
│   ├── base.html
│   └── ... (otros archivos .html)
├── app.py
├── comentarios.db
└── README.md
```