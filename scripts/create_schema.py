"""
Script para crear el schema 'rrhh' en PostgreSQL.
Ejecutar una sola vez antes de las migraciones.
"""

from sqlalchemy import create_engine, text
from app.core.config import get_settings

settings = get_settings()


def create_schema():
    """Crea el schema 'rrhh' si no existe."""
    engine = create_engine(settings.DATABASE_URL)

    with engine.connect() as conn:
        # Crear schema
        conn.execute(text(f"CREATE SCHEMA IF NOT EXISTS {settings.DB_SCHEMA}"))
        conn.commit()
        print(f"Schema '{settings.DB_SCHEMA}' creado exitosamente.")

    engine.dispose()


if __name__ == "__main__":
    create_schema()
