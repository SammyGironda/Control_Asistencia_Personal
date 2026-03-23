"""
Base declarativa para todos los modelos SQLAlchemy 2.0.
Todos los modelos heredan de esta clase Base.

IMPORTANTE:
- Cada modelo nuevo debe importarse aquí para que Alembic lo detecte.
- Usar Mapped y mapped_column (SQLAlchemy 2.0 puro).
"""

from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime

from app.core.config import get_settings

settings = get_settings()

# --- Convención de nombres para constraints ---
# Esto genera nombres consistentes para PKs, FKs, UNIQUEs, etc.
convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(
    naming_convention=convention,
    schema=settings.DB_SCHEMA  # Todas las tablas en schema 'rrhh'
)


class Base(DeclarativeBase):
    """
    Clase base para todos los modelos.
    Incluye campos comunes: id, created_at, updated_at.
    """
    metadata = metadata


# ============================================================
# IMPORTAR TODOS LOS MODELOS AQUÍ
# Alembic usa este archivo para detectar los modelos
# ============================================================

# --- Semana 1: Modelos base ---
from app.features.auth.rol.models import Rol
from app.features.employees.departamento.models import Departamento, ComplementoDep
from app.features.employees.cargo.models import Cargo
from app.features.employees.empleado.models import Empleado

# --- Semana 2: Auth ---
# from app.features.auth.usuario.models import Usuario

# --- Semana 4: Contracts ---
# from app.features.contracts.contrato.models import Contrato
# from app.features.contracts.ajuste_salarial.models import AjusteSalarial

# --- Semana 5-7: Attendance ---
# from app.features.attendance.marcacion.models import Marcacion
# from app.features.attendance.asistencia_diaria.models import AsistenciaDiaria
# from app.features.attendance.feriados.models import DiaFestivo
# from app.features.attendance.beneficio_cumpleanos.models import BeneficioCumpleanos
# from app.features.attendance.justificacion.models import JustificacionAusencia

# --- Semana 8: Reports ---
# from app.features.reports.reporte.models import Reporte
