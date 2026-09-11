from app import app
from sqlalchemy import text, inspect

def add_midi_column_to_db():
    """
    Añade las columnas faltantes ('midi', 'arreglo') a la tabla 'cancion' si no existen.
    Compatible con SQLite y PostgreSQL en Render.
    """
    with app.app_context():
        engine = app.extensions['sqlalchemy'].engine
        
        with engine.connect() as connection:
            inspector = inspect(engine)
            existing_cols = [c['name'] for c in inspector.get_columns('cancion')]
            
            if 'midi' not in existing_cols:
                try:
                    print("Añadiendo columna 'midi' a la tabla 'cancion'...")
                    connection.execute(text('ALTER TABLE cancion ADD COLUMN midi VARCHAR(150)'))
                    connection.commit()
                    print("¡Éxito! La columna 'midi' ha sido añadida.")
                except Exception as e:
                    print(f"Nota columna midi: {e}")
                    
            if 'arreglo' not in existing_cols:
                try:
                    print("Añadiendo columna 'arreglo' a la tabla 'cancion'...")
                    connection.execute(text('ALTER TABLE cancion ADD COLUMN arreglo VARCHAR(100)'))
                    connection.commit()
                    print("¡Éxito! La columna 'arreglo' ha sido añadida.")
                except Exception as e:
                    print(f"Nota columna arreglo: {e}")

if __name__ == '__main__':
    add_midi_column_to_db()
