from app import app
from sqlalchemy import text
from sqlalchemy.exc import OperationalError

def add_interprete_column_to_db():
    """
    Añade la columna 'interprete' a la tabla 'cancion' si no existe.
    """
    with app.app_context():
        engine = app.extensions['sqlalchemy'].engine
        
        with engine.connect() as connection:
            try:
                print("Intentando añadir la columna 'interprete' a la tabla 'cancion'...")
                connection.execute(text('ALTER TABLE cancion ADD COLUMN interprete VARCHAR(200)'))
                connection.commit()
                print("¡Éxito! La columna 'interprete' ha sido añadida.")
            except OperationalError as e:
                # En SQLite, el error típico es "duplicate column name" o "duplicate column"
                if 'duplicate column' in str(e) or 'already exists' in str(e):
                    print("La columna 'interprete' ya existe. No se necesita ninguna acción.")
                else:
                    print(f"Error al añadir columna interprete: {e}")

if __name__ == '__main__':
    add_interprete_column_to_db()
