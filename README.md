# 🎶 Catálogo Musical Personal

Un portafolio musical personal creado con Python y Flask para organizar y mostrar composiciones y arreglos, con reproducción de audio/video y partituras en PDF.

## ✨ Características

- **Catálogo Unificado:** Muestra composiciones y arreglos en una sola lista principal.
- **Vistas Dedicadas:** Secciones separadas para `Composiciones` y `Arreglos`.
- **Reproducción Multimedia:** Soporte para archivos de audio locales y videos incrustados de YouTube.
- **Visualizador de Partituras:** Muestra partituras en formato PDF directamente en la página.
- **Sistema de Comentarios:** Permite a los visitantes dejar comentarios en cada obra.
- **Organización Inteligente:** Usa etiquetas y categorías para filtrar y crear listas de reproducción.

## 🛠️ Tecnologías

- **Backend:** Python, Flask, Flask-SQLAlchemy
- **Base de Datos:** SQLite
- **Frontend:** HTML, CSS, JavaScript

## 🚀 Instalación Local

Para ejecutar este proyecto en tu propia máquina, sigue estos pasos:

```bash
# 1. Clona el repositorio (reemplaza con tu URL de GitHub)
git clone [https://github.com/TuUsuario/tu-repositorio.git](https://github.com/TuUsuario/tu-repositorio.git)
cd tu-repositorio

# 2. Crea y activa el entorno virtual
python -m venv venv
# En Windows: .\\venv\\Scripts\\activate
# En macOS/Linux: source venv/bin/activate

# 3. Instala las dependencias
pip install Flask Flask-SQLAlchemy

# 4. Ejecuta la aplicación
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