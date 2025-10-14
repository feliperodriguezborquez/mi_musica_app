# c:\Users\felip\OneDrive - uc.cl\Yo\IA\GitHub\mi_musica_app\add_midi_column.py
from app import app
from sqlalchemy import text
from sqlalchemy.exc import OperationalError

def add_midi_column_to_db():
    """
    Añade la columna 'midi' a la tabla 'cancion' si no existe.
    """
    with app.app_context():
        engine = app.extensions['sqlalchemy'].engine
        
        with engine.connect() as connection:
            try:
                print("Intentando añadir la columna 'midi' a la tabla 'cancion'...")
                connection.execute(text('ALTER TABLE cancion ADD COLUMN midi VARCHAR(150)'))
                print("¡Éxito! La columna 'midi' ha sido añadida.")
            except OperationalError as e:
                if 'duplicate column name' in str(e):
                    print("La columna 'midi' ya existe. No se necesita ninguna acción.")
                else:
                    raise e

if __name__ == '__main__':
    add_midi_column_to_db()
