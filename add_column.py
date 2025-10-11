from app import app
from sqlalchemy import text
from sqlalchemy.exc import OperationalError

def add_adaptacion_column():
    """
    Añade la columna 'adaptacion' a la tabla 'cancion' si no existe.
    Este es un método seguro que no borra datos existentes.
    """
    with app.app_context():
        # Obtenemos la conexión directa a la base de datos
        engine = app.extensions['sqlalchemy'].db.engine
        
        with engine.connect() as connection:
            try:
                # Intentamos añadir la columna. Si ya existe, SQLite dará un error.
                print("Intentando añadir la columna 'adaptacion' a la tabla 'cancion'...")
                connection.execute(text('ALTER TABLE cancion ADD COLUMN adaptacion VARCHAR(100)'))
                print("¡Éxito! La columna 'adaptacion' ha sido añadida.")
            except OperationalError as e:
                # Si el error indica que la columna ya existe, lo ignoramos.
                if 'duplicate column name' in str(e):
                    print("La columna 'adaptacion' ya existe. No se necesita ninguna acción.")
                else:
                    raise e # Si es otro error, lo mostramos.

if __name__ == '__main__':
    add_adaptacion_column()