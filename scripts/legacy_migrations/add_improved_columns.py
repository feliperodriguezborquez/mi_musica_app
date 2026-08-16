from app import app
from sqlalchemy import text
from sqlalchemy.exc import OperationalError

def add_improved_columns_to_db():
    """
    Añade las columnas 'audios_json' y 'tipo_pdf' a la tabla 'cancion' si no existen.
    """
    with app.app_context():
        engine = app.extensions['sqlalchemy'].engine
        
        with engine.connect() as connection:
            # Columna audios_json
            try:
                print("Intentando añadir la columna 'audios_json' a la tabla 'cancion'...")
                connection.execute(text('ALTER TABLE cancion ADD COLUMN audios_json TEXT'))
                connection.commit()
                print("¡Éxito! La columna 'audios_json' ha sido añadida.")
            except OperationalError as e:
                if 'duplicate column' in str(e) or 'already exists' in str(e):
                    print("La columna 'audios_json' ya existe. No se necesita ninguna acción.")
                else:
                    print(f"Error al añadir columna audios_json: {e}")

            # Columna tipo_pdf
            try:
                print("Intentando añadir la columna 'tipo_pdf' a la tabla 'cancion'...")
                connection.execute(text('ALTER TABLE cancion ADD COLUMN tipo_pdf VARCHAR(50)'))
                connection.commit()
                print("¡Éxito! La columna 'tipo_pdf' ha sido añadida.")
            except OperationalError as e:
                if 'duplicate column' in str(e) or 'already exists' in str(e):
                    print("La columna 'tipo_pdf' ya existe. No se necesita ninguna acción.")
                else:
                    print(f"Error al añadir columna tipo_pdf: {e}")

if __name__ == '__main__':
    add_improved_columns_to_db()
