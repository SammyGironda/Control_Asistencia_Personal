"""
Configuración central de la aplicación.
Lee las variables de entorno desde .env usando pydantic-settings.
"""

from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    """
    Configuración de la aplicación cargada desde variables de entorno.
    Pydantic valida automáticamente los tipos.
    """

    # --- Conexión a Base de Datos ---
    DATABASE_URL: str
    DB_SCHEMA: str = "rrhh"

    # --- Información de la App ---
    APP_NAME: str = "RRHH Bolivia MVP"
    APP_VERSION: str = "0.1.0"
    API_PREFIX: str = "/api/v1"

    # --- Modo Debug ---
    DEBUG: bool = False

    # --- Carpetas de Archivos ---
    UPLOAD_DIR: str = "uploads"
    REPORTS_DIR: str = "reportes_generados"

    # --- Seguridad JWT (Semana 9) ---
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


@lru_cache
def get_settings() -> Settings:
    """
    Retorna la configuración cacheada (singleton).
    Se carga una sola vez y se reutiliza en toda la app.
    """
    return Settings()
