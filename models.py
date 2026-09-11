"""
Modelos de base de datos SQLAlchemy para el catálogo de obras, comentarios e ideas.
"""

import json
import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Comentario(db.Model):
    """
    Comentario público registrado en la ficha de una obra musical.
    """
    __tablename__ = 'comentario'

    id = db.Column(db.Integer, primary_key=True)
    obra_id = db.Column(db.Integer, nullable=False)
    autor = db.Column(db.String(80), nullable=False)
    contenido = db.Column(db.Text, nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"<Comentario {self.id} por {self.autor} en obra {self.obra_id}>"


class Cancion(db.Model):
    """
    Entidad principal que representa una obra musical (composición o arreglo).
    Soporta metadatos de partituras (PDF/MusicXML/MIDI), audios, ensamble y etiquetas jerárquicas.
    """
    __tablename__ = 'cancion'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    musica = db.Column(db.String(100))
    letra = db.Column(db.String(100))
    adaptacion = db.Column(db.String(100))
    arreglo = db.Column(db.String(100), nullable=True)
    idioma = db.Column(db.String(50))
    dia = db.Column(db.Integer, nullable=True)
    mes = db.Column(db.Integer, nullable=True)
    anio = db.Column(db.Integer)
    descripcion = db.Column(db.Text)
    audio = db.Column(db.String(150))
    letras_acordes = db.Column(db.String(150))
    partitura = db.Column(db.String(150))
    midi = db.Column(db.String(150))
    tags_json = db.Column(db.String(500))
    tipo = db.Column(db.String(50), nullable=False, default='local')
    categorias_json = db.Column(db.String(200))
    youtube_video_embed = db.Column(db.Text)
    youtube_audio_embed = db.Column(db.Text)
    interprete = db.Column(db.String(200), nullable=True)
    ensambles_json = db.Column(db.Text, nullable=True)
    descargas_json = db.Column(db.Text, nullable=True)
    audios_json = db.Column(db.Text, nullable=True)
    tipo_pdf = db.Column(db.String(50), nullable=True)  # 'partitura' o 'letras_acordes'

    @property
    def tags(self):
        """Lista deserializada de etiquetas."""
        return json.loads(self.tags_json) if self.tags_json else []

    @property
    def categorias(self):
        """Lista deserializada de categorías (Composición, Arreglo)."""
        return json.loads(self.categorias_json) if self.categorias_json else []

    @property
    def ensambles(self):
        """Lista de configuraciones de ensamble para la obra."""
        return json.loads(self.ensambles_json) if self.ensambles_json else []

    @property
    def descargas(self):
        """Lista de archivos descargables adicionales (partituras por voz/instrumento)."""
        return json.loads(self.descargas_json) if self.descargas_json else []

    @property
    def audios(self):
        """Lista de audios complementarios."""
        return json.loads(self.audios_json) if self.audios_json else []

    def __repr__(self):
        return f"<Cancion {self.id}: {self.titulo}>"


class IdeaCancion(db.Model):
    """
    Registro para el tablero Kanban administrativo de ideas y borradores musicales.
    """
    __tablename__ = 'idea_cancion'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(150), nullable=False)
    notas = db.Column(db.Text, nullable=True)
    estado = db.Column(db.String(20), nullable=False, default='idea')  # 'idea', 'mitad', 'lista'
    cancion_id = db.Column(db.Integer, db.ForeignKey('cancion.id'), nullable=True)
    cancion = db.relationship('Cancion', backref='idea', foreign_keys=[cancion_id])

    def __repr__(self):
        return f"<IdeaCancion {self.id}: {self.titulo} [{self.estado}]>"
