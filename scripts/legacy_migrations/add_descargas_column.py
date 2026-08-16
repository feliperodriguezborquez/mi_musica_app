from app import app
from sqlalchemy import text
from sqlalchemy.exc import OperationalError

def add_descargas_column_to_db():
    """
    Añade la columna 'descargas_json' a la tabla 'cancion' si no existe.
    """
    with app.app_context():
        engine = app.extensions['sqlalchemy'].engine
        
        with engine.connect() as connection:
            try:
                print("Intentando añadir la columna 'descargas_json' a la tabla 'cancion'...")
                connection.execute(text('ALTER TABLE cancion ADD COLUMN descargas_json TEXT'))
                connection.commit()
                print("¡Éxito! La columna 'descargas_json' ha sido añadida.")
            except OperationalError as e:
                if 'duplicate column' in str(e) or 'already exists' in str(e):
                    print("La columna 'descargas_json' ya existe. No se necesita ninguna acción.")
                else:
                    print(f"Error al añadir columna descargas_json: {e}")

if __name__ == '__main__':
    add_descargas_column_to_db()
