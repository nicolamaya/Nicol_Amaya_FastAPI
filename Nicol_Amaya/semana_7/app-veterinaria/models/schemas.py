from pydantic import BaseModel
from typing import List

class DocumentoMedico(BaseModel):
    """Esquema para un documento dentro del historial."""
    tipo: str # Ej: 'Vacunación', 'Diagnóstico', 'Cirugía'
    fecha: str
    descripcion: str
    veterinario: str

class HistorialMedico(BaseModel):
    """Esquema principal para la entidad crítica: Historial Médico."""
    id_mascota: str
    nombre_mascota: str
    especie: str
    raza: str
    documentos: List[DocumentoMedico]
    ultima_actualizacion: str