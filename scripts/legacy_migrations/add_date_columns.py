from app import app, db
from sqlalchemy import text
from sqlalchemy.exc import OperationalError

def add_dia_mes_columns():
    """
    Añade las columnas 'dia' y 'mes' a la tabla 'cancion' si no existen.
    """
    with app.app_context():
        engine = db.engine
        
        with engine.connect() as connection:
            # 1. Añadir la columna 'dia'
            try:
                print("Intentando añadir la columna 'dia' a la tabla 'cancion'...")
                connection.execute(text('ALTER TABLE cancion ADD COLUMN dia INTEGER'))
                print("¡Éxito! La columna 'dia' ha sido añadida.")
            except OperationalError as e:
                if 'duplicate column name' in str(e).lower():
                    print("La columna 'dia' ya existe. No se necesita ninguna acción.")
                else:
                    raise e

            # 2. Añadir la columna 'mes'
            try:
                print("Intentando añadir la columna 'mes' a la tabla 'cancion'...")
                connection.execute(text('ALTER TABLE cancion ADD COLUMN mes INTEGER'))
                print("¡Éxito! La columna 'mes' ha sido añadida.")
            except OperationalError as e:
                if 'duplicate column name' in str(e).lower():
                    print("La columna 'mes' ya existe. No se necesita ninguna acción.")
                else:
                    raise e

if __name__ == '__main__':
    add_dia_mes_columns()