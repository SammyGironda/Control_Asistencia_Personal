"""
Utilidades comunes para toda la aplicación.
Funciones auxiliares, mixins y helpers reutilizables.
"""

from datetime import datetime, date
from typing import Optional


def fecha_actual() -> date:
    """Retorna la fecha actual (solo fecha, sin hora)."""
    return date.today()


def datetime_actual() -> datetime:
    """Retorna el datetime actual con timezone naive."""
    return datetime.now()


def formatear_ci(ci_numero: str, complemento: Optional[str] = None, sufijo: Optional[str] = None) -> str:
    """
    Formatea el CI completo de un empleado.

    Ejemplo:
        formatear_ci("1234567", "LP", "1A") -> "1234567-LP-1A"
        formatear_ci("1234567", "SC") -> "1234567-SC"
        formatear_ci("1234567") -> "1234567"
    """
    partes = [ci_numero]
    if complemento:
        partes.append(complemento)
    if sufijo:
        partes.append(sufijo)
    return "-".join(partes)
