from pydantic import BaseModel, Field
from typing import Optional

# El modelo base para crear o actualizar un paciente
class PacienteBase(BaseModel):
    """
    Modelo base para la entidad Paciente (Clínica Dental).
    Campos adaptados según la Ficha (nombre, edad, historial_medico).
    """
    nombre: str = Field(..., min_length=3, description="Nombre completo del paciente.")
    edad: int = Field(..., gt=0, le=120, description="Edad del paciente. Debe ser positiva.")
    historial_medico: str = Field(..., min_length=10, description="Historial de alergias/antecedentes. Campo obligatorio para el dominio dental.")
    tipo_sangre: str = Field("Desconocido", description="Tipo de sangre del paciente.")
    contacto_emergencia: str = Field(..., min_length=7, description="Teléfono de contacto en caso de emergencia.")
    
    # Campo crucial para la regla de negocio
    autorizacion_tutor: bool = Field(False, description="True si es menor de 18 y tiene autorización.")

# El modelo completo (incluye el ID para la respuesta)
class PacienteCompleto(PacienteBase):
    id: str

    class Config:
        from_attributes = True