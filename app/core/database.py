"""
Configuración de la conexión a PostgreSQL usando SQLAlchemy 2.0.
Provee el engine, SessionLocal y la dependencia get_db para FastAPI.
"""

from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker, Session
from typing import Generator

from app.core.config import get_settings

settings = get_settings()

# --- Crear Engine ---
# echo=True imprime las queries SQL en consola (útil para debug)
engine = create_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,
    pool_pre_ping=True,  # Verifica conexión antes de usarla
    pool_size=5,
    max_overflow=10
)


# --- Configurar schema por defecto en cada conexión ---
@event.listens_for(engine, "connect")
def set_search_path(dbapi_connection, connection_record):
    """
    Establece el search_path a 'rrhh, public' en cada conexión.
    Así todas las queries usan el schema rrhh por defecto.
    """
    cursor = dbapi_connection.cursor()
    cursor.execute(f"SET search_path TO {settings.DB_SCHEMA}, public")
    cursor.close()
    dbapi_connection.commit()


# --- Session Factory ---
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False
)


# --- Dependencia para FastAPI ---
def get_db() -> Generator[Session, None, None]:
    """
    Dependencia que provee una sesión de base de datos.
    Se usa en los endpoints con: db: Session = Depends(get_db)

    Ejemplo:
        @router.get("/items")
        def get_items(db: Session = Depends(get_db)):
            return db.query(Item).all()
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
