"""
Aplicación Web: Catálogo Musical de Felipe Rodríguez.
Módulo principal de Flask con configuración, rutas HTTP y ciclo de vida de la aplicación.
"""

import os
import re
import json
import datetime
from functools import wraps
from pathlib import Path
from dotenv import load_dotenv

from flask import (
    Flask, render_template, abort, request, redirect,
    url_for, session, flash, send_file, jsonify
)

# Cargar variables de entorno locales desde .env si existe
load_dotenv()

# ============================================================
# INICIALIZACIÓN Y CONFIGURACIÓN DE LA APLICACIÓN
# ============================================================
app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev_secret_key_default')
app.config['ADMIN_PASSWORD'] = os.environ.get('ADMIN_PASSWORD', 'admin')

# Normalizar URL de PostgreSQL para compatibilidad con SQLAlchemy 2.0 en Render
db_url = os.environ.get('DATABASE_URL', 'sqlite:///comentarios.db')
if db_url and db_url.startswith('postgres://'):
    db_url = db_url.replace('postgres://', 'postgresql://', 1)
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# ============================================================
# MODELOS Y CONSTANTES (IMPORTADOS Y RE-EXPORTADOS PARA COMPATIBILIDAD)
# ============================================================
from models import db, Cancion, Comentario, IdeaCancion
from constants import (
    FEATURES,
    ORDEN_LIBROS_BIBLIA,
    MAPEO_LIBROS_BIBLIA,
    CITA_REGEX,
    ORDEN_TIEMPOS_LITURGICOS,
    ORDEN_SANTA_MISA,
    ORDENES_PERSONALIZADOS,
)
from services.tag_service import (
    tag_matches,
    build_hierarchical_tags,
    build_breadcrumbs,
    get_child_tags,
    process_song_tags,
)
from services.catalog_service import (
    parse_cita_biblica,
    normalize_for_sorting,
    normalize_category_name,
    search_songs,
    search_by_category,
    sort_songs,
    get_playlist_songs,
)

# Inicializar SQLAlchemy con la app Flask
db.init_app(app)

# ============================================================
# FILTROS Y PROCESADORES DE CONTEXTO JINJA
# ============================================================
@app.template_filter('sort_categories_for_page')
def sort_categories_for_page(categories, page_context='default'):
    """Filtro de Jinja para ordenar las categorías de las obras según la página activa."""
    sorted_cats = list(categories)
    if page_context == 'arreglos':
        # En la página de arreglos: Composición a la izquierda, Arreglo a la derecha
        sorted_cats.sort(key=lambda x: (x != 'Composición', x != 'Arreglo'))
    else:
        # Por defecto (catálogo completo, composiciones): Arreglo a la izquierda, Composición a la derecha
        sorted_cats.sort(key=lambda x: (x != 'Arreglo', x != 'Composición'))
    return sorted_cats


@app.context_processor
def inject_globals():
    """Inyecta la fecha de compilación y feature flags en todas las plantillas."""
    try:
        with open('build_date.txt', 'r', encoding='utf-8') as f:
            date_str = f.read().strip()
    except Exception:
        date_str = "Desconocida"
    return dict(last_update=date_str, FEATURES=FEATURES)


# ============================================================
# DECORADORES DE SEGURIDAD
# ============================================================
def login_required(f):
    """Decorador para proteger rutas exclusivas de administración."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


# ============================================================
# RUTAS PÚBLICAS: CATÁLOGO DE OBRAS
# ============================================================
@app.route('/')
def index():
    """Página de inicio: Catálogo completo con buscador en vivo y opciones de orden."""
    base_songs = Cancion.query.all()
    filtered_songs, search_query = search_songs(base_songs, request.args.get('search', '').strip())
    sort_by = request.args.get('sort_by', 'cronologico')
    sorted_songs = sort_songs(filtered_songs, sort_by=sort_by)
    return render_template('index.html', composiciones=sorted_songs, search_query=search_query, page_context='index', sort_by=sort_by)


@app.route('/composiciones')
def ver_composiciones():
    """Vista filtrada por canciones con categoría 'Composición'."""
    base_songs = search_by_category("Composición")
    filtered_songs, search_query = search_songs(base_songs, request.args.get('search', '').strip())
    sort_by = request.args.get('sort_by', 'cronologico')
    sorted_songs = sort_songs(filtered_songs, sort_by=sort_by)
    return render_template('composiciones.html', composiciones=sorted_songs, search_query=search_query, page_context='composiciones', sort_by=sort_by)


@app.route('/arreglos')
def ver_arreglos():
    """Vista filtrada por canciones con categoría 'Arreglo'."""
    base_songs = search_by_category("Arreglo")
    filtered_songs, search_query = search_songs(base_songs, request.args.get('search', '').strip())
    sort_by = request.args.get('sort_by', 'cronologico')
    sorted_songs = sort_songs(filtered_songs, sort_by=sort_by)
    return render_template('arreglos.html', composiciones=sorted_songs, search_query=search_query, page_context='arreglos', sort_by=sort_by)


@app.route('/todos')
def ver_todos():
    """Vista alternativa del catálogo completo."""
    base_songs = Cancion.query.all()
    filtered_songs, search_query = search_songs(base_songs, request.args.get('search', '').strip())
    sort_by = request.args.get('sort_by', 'cronologico')
    sorted_songs = sort_songs(filtered_songs, sort_by=sort_by)
    return render_template('todos.html', composiciones=sorted_songs, search_query=search_query, page_context='todos', sort_by=sort_by)


@app.route('/tag/<tag_name>')
def ver_tag(tag_name):
    """Vista de obras filtradas por etiqueta o subetiqueta jerárquica."""
    all_songs = Cancion.query.all()
    matching_songs = [s for s in all_songs if tag_matches(tag_name, s.tags)]
    filtered_songs, search_query = search_songs(matching_songs, request.args.get('search', '').strip())

    sort_by = request.args.get('sort_by', 'canonico')
    main_category = tag_name.split(':')[0].strip()
    sorted_songs = sort_songs(filtered_songs, sort_by=sort_by, main_category=main_category)

    breadcrumbs = build_breadcrumbs(tag_name)
    child_tags = get_child_tags(tag_name, all_songs)

    return render_template(
        'vista_tag.html',
        composiciones=sorted_songs,
        tag_nombre=tag_name,
        search_query=search_query,
        page_context='tag',
        sort_by=sort_by,
        ordenes_personalizados=ORDENES_PERSONALIZADOS.keys(),
        main_category=main_category,
        breadcrumbs=breadcrumbs,
        child_tags=child_tags
    )


@app.route('/listas')
def ver_listas():
    """Directorio de listas de reproducción y taxonomía jerárquica de etiquetas."""
    todas_las_canciones = Cancion.query.all()
    set_de_tags = {tag.strip() for c in todas_las_canciones for tag in c.tags if tag and tag.strip()}
    simple_tags, hierarchical_tags = build_hierarchical_tags(set_de_tags)
    return render_template('listas.html', simple_tags=simple_tags, hierarchical_tags=hierarchical_tags)


@app.route('/get_playlist')
def get_playlist_partial():
    """Endpoint AJAX que retorna el partial HTML de la lista de canciones."""
    context = request.args.get('context', 'index')
    tag_name = request.args.get('tag_name')
    search_query = request.args.get('search')
    sort_by = request.args.get('sort_by', 'cronologico')
    categoria = request.args.get('categoria')

    playlist = get_playlist_songs(context, tag_name=tag_name, search_query=search_query, sort_by=sort_by, categoria=categoria)
    return render_template('_song_list.html', composiciones=playlist, page_context=context, tag_nombre=tag_name, search_query=search_query, sort_by=sort_by)


@app.route('/filter')
def filter_songs():
    """Endpoint de búsqueda en vivo y filtrado AJAX utilizado por base.html."""
    categoria = request.args.get('categoria', '').strip()
    search_query = request.args.get('search', '').strip()
    sort_by = request.args.get('sort_by', 'cronologico').strip()
    context = request.args.get('context', 'index').strip()
    tag_name = request.args.get('tag_name')

    playlist = get_playlist_songs(context, tag_name=tag_name, search_query=search_query, sort_by=sort_by, categoria=categoria)
    return render_template(
        '_song_list.html',
        composiciones=playlist,
        page_context=context,
        tag_nombre=tag_name,
        search_query=search_query,
        sort_by=sort_by
    )


@app.route('/composicion/<int:comp_id>')
def ver_composicion(comp_id):
    """Ficha detallada de una obra con reproductor, partitura, descargas y comentarios."""
    context = request.args.get('context', 'index')
    tag_name = request.args.get('tag_name')
    search_query = request.args.get('search')
    sort_by = request.args.get('sort_by', 'cronologico')
    categoria = request.args.get('categoria')

    playlist = get_playlist_songs(context, tag_name=tag_name, search_query=search_query, sort_by=sort_by, categoria=categoria)

    # Navegación anterior / siguiente en la playlist
    playlist_ids = [s.id for s in playlist]
    try:
        current_index = playlist_ids.index(comp_id)
    except ValueError:
        current_index = -1

    url_params = dict(context=context, tag_name=tag_name, search=search_query, sort_by=sort_by)
    prev_song_url = url_for('ver_composicion', comp_id=playlist_ids[current_index - 1], **url_params) if current_index > 0 else None
    next_song_url = url_for('ver_composicion', comp_id=playlist_ids[current_index + 1], **url_params) if (0 <= current_index < len(playlist_ids) - 1) else None

    # Título dinámico para el menú lateral
    playlist_title = "Catálogo Completo"
    if context == 'composiciones':
        playlist_title = "Composiciones"
    elif context == 'arreglos':
        playlist_title = "Arreglos"
    elif context == 'tag' and tag_name:
        playlist_title = tag_name.split(':')[-1].strip() if ':' in tag_name else tag_name

    # URL de retorno a la lista
    playlist_url = url_for('index')
    if context == 'composiciones':
        playlist_url = url_for('ver_composiciones', search=search_query, sort_by=sort_by)
    elif context == 'arreglos':
        playlist_url = url_for('ver_arreglos', search=search_query, sort_by=sort_by)
    elif context == 'tag' and tag_name:
        playlist_url = url_for('ver_tag', tag_name=tag_name, search=search_query, sort_by=sort_by)
    elif context == 'index':
        playlist_url = url_for('index', search=search_query, sort_by=sort_by)

    obra_encontrada = Cancion.query.get_or_404(comp_id)
    partitura_path = obra_encontrada.partitura
    processed_tags = process_song_tags(obra_encontrada.tags)
    comentarios_obra = Comentario.query.filter_by(obra_id=comp_id).order_by(Comentario.fecha_creacion.desc()).all()

    return render_template(
        'composicion.html',
        obra=obra_encontrada,
        partitura_path=partitura_path,
        comentarios=comentarios_obra,
        prev_song_url=prev_song_url,
        next_song_url=next_song_url,
        playlist=playlist,
        playlist_title=playlist_title,
        playlist_url=playlist_url,
        processed_tags=processed_tags
    )


# ============================================================
# AUTENTICACIÓN
# ============================================================
@app.route('/login', methods=['GET', 'POST'])
def login():
    """Inicio de sesión administrativo."""
    if request.method == 'POST':
        if request.form.get('password') == app.config['ADMIN_PASSWORD']:
            session['logged_in'] = True
            flash('¡Has iniciado sesión correctamente!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Contraseña incorrecta.', 'danger')
    return render_template('login.html')


@app.route('/logout')
def logout():
    """Cierre de sesión administrativo."""
    session.pop('logged_in', None)
    flash('Has cerrado sesión.', 'info')
    return redirect(url_for('index'))


# ============================================================
# COMENTARIOS
# ============================================================
@app.route('/composicion/<int:comp_id>/add_comment', methods=['POST'])
def add_comment(comp_id):
    """Registra un nuevo comentario en una obra."""
    autor = request.form.get('autor', '').strip()
    contenido = request.form.get('contenido', '').strip()
    if autor and contenido:
        nuevo_comentario = Comentario(obra_id=comp_id, autor=autor, contenido=contenido)
        db.session.add(nuevo_comentario)
        db.session.commit()
    return redirect(url_for('ver_composicion', comp_id=comp_id))


@app.route('/comment/<int:comment_id>/delete', methods=['POST'])
@login_required
def delete_comment(comment_id):
    """Elimina un comentario existente (requiere admin)."""
    comentario_a_borrar = Comentario.query.get_or_404(comment_id)
    obra_id = comentario_a_borrar.obra_id
    db.session.delete(comentario_a_borrar)
    db.session.commit()
    flash('Comentario borrado con éxito.', 'success')
    return redirect(url_for('ver_composicion', comp_id=obra_id))


# ============================================================
# ADMINISTRACIÓN DE OBRAS: EDICIÓN Y BORRADO
# ============================================================
@app.route('/composicion/<int:comp_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_cancion(comp_id):
    """Edición completa de metadatos de una canción."""
    cancion_a_editar = Cancion.query.get_or_404(comp_id)

    if request.method == 'POST':
        cancion_a_editar.titulo = request.form.get('titulo')
        cancion_a_editar.musica = request.form.get('musica')
        cancion_a_editar.letra = request.form.get('letra')
        cancion_a_editar.adaptacion = request.form.get('adaptacion')
        cancion_a_editar.arreglo = request.form.get('arreglo')
        cancion_a_editar.idioma = request.form.get('idioma')
        cancion_a_editar.descripcion = request.form.get('descripcion')
        cancion_a_editar.audio = request.form.get('audio')
        cancion_a_editar.letras_acordes = request.form.get('letras_acordes')
        cancion_a_editar.partitura = request.form.get('partitura')
        cancion_a_editar.midi = request.form.get('midi')
        cancion_a_editar.tipo = request.form.get('tipo', 'local')
        cancion_a_editar.youtube_video_embed = request.form.get('youtube_video_embed')
        cancion_a_editar.youtube_audio_embed = request.form.get('youtube_audio_embed')
        cancion_a_editar.interprete = request.form.get('interprete')
        cancion_a_editar.tipo_pdf = request.form.get('tipo_pdf')

        dia = request.form.get('dia')
        mes = request.form.get('mes')
        anio = request.form.get('anio')
        cancion_a_editar.dia = int(dia) if dia and dia.isdigit() else None
        cancion_a_editar.mes = int(mes) if mes and mes.isdigit() else None
        cancion_a_editar.anio = int(anio) if anio and anio.isdigit() else None

        processed_tags = [tag.strip() for tag in request.form.get('tags', '').split(',') if tag.strip()]
        cancion_a_editar.tags_json = json.dumps(processed_tags)

        processed_categorias = [cat.strip() for cat in request.form.get('categorias', '').split(',') if cat.strip()]
        cancion_a_editar.categorias_json = json.dumps(processed_categorias)

        # Sincronizar cambios también en data.json
        try:
            with open('data.json', 'r+', encoding='utf-8') as f:
                data = json.load(f)
                for i, c in enumerate(data):
                    if c.get('id') == comp_id:
                        data[i].update({
                            'titulo': cancion_a_editar.titulo,
                            'musica': cancion_a_editar.musica,
                            'letra': cancion_a_editar.letra,
                            'adaptacion': cancion_a_editar.adaptacion,
                            'arreglo': cancion_a_editar.arreglo,
                            'idioma': cancion_a_editar.idioma,
                            'dia': cancion_a_editar.dia,
                            'mes': cancion_a_editar.mes,
                            'anio': cancion_a_editar.anio,
                            'descripcion': cancion_a_editar.descripcion,
                            'audio': cancion_a_editar.audio,
                            'letras_acordes': cancion_a_editar.letras_acordes,
                            'partitura': cancion_a_editar.partitura,
                            'midi': cancion_a_editar.midi,
                            'tipo': cancion_a_editar.tipo,
                            'tags': processed_tags,
                            'categorias': processed_categorias,
                            'youtube_video_embed': cancion_a_editar.youtube_video_embed,
                            'youtube_audio_embed': cancion_a_editar.youtube_audio_embed,
                            'interprete': cancion_a_editar.interprete,
                            'tipo_pdf': cancion_a_editar.tipo_pdf,
                        })
                        break
                f.seek(0)
                json.dump(data, f, ensure_ascii=False, indent=4)
                f.truncate()
        except Exception as e:
            flash(f'Error al guardar en data.json: {e}', 'danger')

        db.session.commit()
        flash('Canción actualizada con éxito.', 'success')
        return redirect(url_for('ver_composicion', comp_id=cancion_a_editar.id))

    todas_las_canciones = Cancion.query.all()
    todos_los_tags = sorted(list({t.strip() for c in todas_las_canciones for t in c.tags if t and t.strip()}))
    todas_las_categorias = sorted(list({cat.strip() for c in todas_las_canciones for cat in c.categorias if cat and cat.strip()}))

    return render_template(
        'edit_cancion.html',
        cancion=cancion_a_editar,
        todos_los_tags=todos_los_tags,
        todas_las_categorias=todas_las_categorias
    )


@app.route('/composicion/<int:comp_id>/delete', methods=['POST'])
@login_required
def delete_cancion(comp_id):
    """Elimina una canción de la base de datos y de data.json."""
    cancion_a_borrar = Cancion.query.get_or_404(comp_id)

    try:
        with open('data.json', 'r+', encoding='utf-8') as f:
            data = json.load(f)
            data_filtrada = [c for c in data if c.get('id') != comp_id]
            f.seek(0)
            json.dump(data_filtrada, f, ensure_ascii=False, indent=4)
            f.truncate()
    except Exception as e:
        flash(f'Error al borrar de data.json: {e}', 'danger')

    db.session.delete(cancion_a_borrar)
    db.session.commit()
    flash('Canción eliminada correctamente.', 'success')
    return redirect(url_for('index'))


# ============================================================
# ADMINISTRACIÓN: TABLERO KANBAN DE IDEAS
# ============================================================
@app.route('/admin/ideas')
@login_required
def admin_ideas():
    """Tablero Kanban de ideas y estados de composición."""
    if not FEATURES['ideas_admin']:
        abort(404)
    ideas = {
        'idea':  IdeaCancion.query.filter_by(estado='idea').order_by(IdeaCancion.titulo).all(),
        'mitad': IdeaCancion.query.filter_by(estado='mitad').order_by(IdeaCancion.titulo).all(),
        'lista': IdeaCancion.query.filter_by(estado='lista').order_by(IdeaCancion.titulo).all(),
    }
    canciones = Cancion.query.order_by(Cancion.titulo).all()
    return render_template('admin/ideas.html', ideas=ideas, canciones=canciones)


@app.route('/admin/ideas/add', methods=['POST'])
@login_required
def admin_ideas_add():
    """Crea una nueva idea en la columna 'idea'."""
    titulo = request.form.get('titulo', '').strip()
    notas = request.form.get('notas', '').strip() or None
    if titulo:
        db.session.add(IdeaCancion(titulo=titulo, notas=notas, estado='idea'))
        db.session.commit()
    return redirect(url_for('admin_ideas'))


@app.route('/admin/ideas/<int:idea_id>/update', methods=['POST'])
@login_required
def admin_ideas_update(idea_id):
    """Actualiza el estado o metadatos de una idea."""
    idea = IdeaCancion.query.get_or_404(idea_id)
    idea.estado = request.form.get('estado', idea.estado)
    idea.titulo = request.form.get('titulo', idea.titulo).strip() or idea.titulo
    idea.notas = request.form.get('notas', idea.notas or '').strip() or None
    cid = request.form.get('cancion_id', '').strip()
    idea.cancion_id = int(cid) if cid else None
    db.session.commit()
    return redirect(url_for('admin_ideas'))


@app.route('/admin/ideas/<int:idea_id>/delete', methods=['POST'])
@login_required
def admin_ideas_delete(idea_id):
    """Elimina una idea del tablero Kanban."""
    idea = IdeaCancion.query.get_or_404(idea_id)
    db.session.delete(idea)
    db.session.commit()
    return redirect(url_for('admin_ideas'))


# ============================================================
# PIPELINE CANTAMUS: OPTIMIZACIÓN Y MEZCLA DE AUDIOS
# ============================================================
@app.route('/cantamus')
@login_required
def cantamus_view():
    """Panel de preprocesamiento de partituras para Cantamus."""
    from scripts.cantamus_pipeline import get_recent_scores
    recent = get_recent_scores(limit=15)
    return render_template('cantamus.html', recent_scores=recent)


@app.route('/cantamus/inspect', methods=['POST'])
@login_required
def cantamus_inspect():
    """Inspecciona metadatos y tempos de una partitura MusicXML/MXL."""
    from scripts.cantamus_pipeline import inspect_score_info
    data = request.get_json() or {}
    filepath = data.get('filepath')
    if not filepath or not os.path.exists(filepath):
        return jsonify({'error': 'Archivo no encontrado'}), 404
    info = inspect_score_info(filepath)
    return jsonify(info)


@app.route('/cantamus/process', methods=['POST'])
@login_required
def cantamus_process():
    """Procesa una partitura aplicando ritardando y optimizaciones vocales."""
    from scripts.cantamus_pipeline import process_cantamus

    filepath = request.form.get('filepath', '').strip()
    uploaded_file = request.files.get('score_file')
    action_type = request.form.get('action_type', 'download')

    target_path = None
    temp_upload = None

    if uploaded_file and uploaded_file.filename:
        temp_dir = Path.home() / 'Downloads'
        temp_upload = temp_dir / f"_upload_{uploaded_file.filename}"
        uploaded_file.save(str(temp_upload))
        target_path = temp_upload
    elif filepath and os.path.exists(filepath):
        target_path = Path(filepath)
    else:
        flash("No se proporcionó un archivo válido.", "error")
        return redirect(url_for('cantamus_view'))

    try:
        initial_bpm = int(request.form.get('initial_bpm', 71) or 71)
    except ValueError:
        initial_bpm = 71

    rit_profile = request.form.get('rit_profile', 'ease-in')
    try:
        rit_drop = float(request.form.get('rit_drop', 75)) / 100.0
    except ValueError:
        rit_drop = 0.75

    try:
        rit_measures = int(request.form.get('rit_measures', 2) or 2)
    except ValueError:
        rit_measures = 2

    solo_voces = request.form.get('solo_voces') == '1'
    fix_tenor = request.form.get('fix_tenor') == '1'

    downloads_dir = Path.home() / 'Downloads'
    clean_stem = re.sub(r'_Cantamus.*$', '', target_path.stem)
    out_file = downloads_dir / f"{clean_stem}_Cantamus.musicxml"

    try:
        process_cantamus(
            input_path=target_path,
            output_path=out_file,
            initial_bpm=initial_bpm,
            rit_profile=rit_profile,
            rit_drop=rit_drop,
            rit_measures=rit_measures,
            keep_accompaniment=not solo_voces,
            fix_tenor_breathing=fix_tenor
        )

        if action_type == 'download':
            return send_file(
                str(out_file),
                as_attachment=True,
                download_name=out_file.name,
                mimetype='application/vnd.recordare.musicxml+xml'
            )
        else:
            flash(f"✅ ¡Partitura procesada con éxito! Guardada en: {out_file}", "success")
            return redirect(url_for('cantamus_view'))

    except Exception as e:
        flash(f"Error al procesar la partitura: {e}", "error")
        return redirect(url_for('cantamus_view'))
    finally:
        if temp_upload and temp_upload.exists():
            try:
                temp_upload.unlink()
            except Exception:
                pass


@app.route('/cantamus/mix', methods=['POST'])
@login_required
def cantamus_mix():
    """Mezcla pista vocal de Cantamus con pista instrumental de MuseSounds."""
    vocal_file = request.files.get('vocal_file')
    inst_file = request.files.get('inst_file')

    if not vocal_file or not inst_file or not vocal_file.filename or not inst_file.filename:
        flash("Debes seleccionar ambos archivos de audio (voces e instrumental).", "error")
        return redirect(url_for('cantamus_view'))

    try:
        from scripts.mezclar_audio import mezclar_cantamus_musesounds
    except Exception as e:
        flash(f"Error al cargar módulo de mezcla de audio: {e}", "error")
        return redirect(url_for('cantamus_view'))

    try:
        gain = float(request.form.get('vocal_gain', 2.5) or 2.5)
    except ValueError:
        gain = 2.5

    try:
        delay = int(request.form.get('vocal_delay', 0) or 0)
    except ValueError:
        delay = 0

    temp_dir = Path.home() / 'Downloads'
    vocal_temp = temp_dir / f"_temp_voces_{vocal_file.filename}"
    inst_temp = temp_dir / f"_temp_inst_{inst_file.filename}"
    clean_stem = re.sub(r'(_Cantamus|_voces|_vocal).*$', '', Path(vocal_file.filename).stem, flags=re.IGNORECASE)
    out_master = temp_dir / f"{clean_stem}_Master_MuseSounds_Cantamus.mp3"

    try:
        vocal_file.save(str(vocal_temp))
        inst_file.save(str(inst_temp))

        mezclar_cantamus_musesounds(
            vocal_path=vocal_temp,
            instrumental_path=inst_temp,
            output_path=out_master,
            vocal_gain_db=gain,
            vocal_delay_ms=delay
        )

        return send_file(
            str(out_master),
            as_attachment=True,
            download_name=out_master.name,
            mimetype='audio/mpeg'
        )
    except Exception as e:
        flash(f"Error al mezclar audios: {e}", "error")
        return redirect(url_for('cantamus_view'))
    finally:
        for tmp in [vocal_temp, inst_temp]:
            if tmp.exists():
                try:
                    tmp.unlink()
                except Exception:
                    pass


# ============================================================
# INICIALIZACIÓN, MIGRACIONES Y SINCRONIZACIÓN AL ARRANQUE
# ============================================================
with app.app_context():
    db.create_all()

    # Verificar/migrar columnas adicionales en PostgreSQL / SQLite
    try:
        from add_midi_column import add_midi_column_to_db
        add_midi_column_to_db()
    except Exception as e:
        print(f"Nota columna midi/arreglo: {e}")

    # Sincronizar catálogo desde data.json automáticamente al iniciar
    try:
        from sincronizar_canciones import sincronizar_canciones_desde_json
        sincronizar_canciones_desde_json()
    except Exception as e:
        print(f"Error al sincronizar canciones automáticamente: {e}")

    # Semilla inicial para ideas si la tabla está vacía
    if FEATURES['ideas_admin'] and IdeaCancion.query.count() == 0:
        miserere = Cancion.query.filter(Cancion.titulo.ilike('%miserere%')).first()
        profundis = Cancion.query.filter(Cancion.titulo.ilike('%profundis%')).first()
        sembrador = Cancion.query.filter(Cancion.titulo.ilike('%sembrador%')).first()
        eripe = Cancion.query.filter(Cancion.titulo.ilike('%eripe%')).first()
        seeds = [
            IdeaCancion(titulo='El Sembrador', estado='lista', cancion_id=sembrador.id if sembrador else None),
            IdeaCancion(titulo='Miserere', estado='lista', cancion_id=miserere.id if miserere else None),
            IdeaCancion(titulo='De Profundis', estado='lista', cancion_id=profundis.id if profundis else None),
            IdeaCancion(titulo='Salmo 6 (Señor, no me reprendas en tu enojo)', estado='idea'),
            IdeaCancion(titulo='Salmo 32 (Dichoso el que es absuelto)', estado='idea'),
            IdeaCancion(titulo='Salmo 38 (Señor, no me reprendas enojado)', estado='idea'),
            IdeaCancion(titulo='Salmo 102 (Bendice, alma mía, al Señor)', estado='idea'),
            IdeaCancion(titulo='Salmo 143 (Señor, escucha mi oración)', estado='lista', cancion_id=eripe.id if eripe else None),
        ]
        for s in seeds:
            db.session.add(s)
        db.session.commit()
        print("Ideas iniciales sembradas.")


if __name__ == '__main__':
    app.run(debug=True)