from fastapi import APIRouter, HTTPException, status
from schemas import PacienteBase, PacienteCompleto
from database import DB_PACIENTES, get_paciente_by_id
import uuid

# Router para el prefijo asignado: /dental/pacientes
router = APIRouter(
    prefix="/dental/pacientes",
    tags=["Clínica Dental: Pacientes"]
)

@router.post("/", response_model=PacienteCompleto, status_code=status.HTTP_201_CREATED)
def crear_paciente(paciente: PacienteBase):
    """
    Registra un nuevo paciente. Implementa la Regla de Negocio:
    Pacientes menores de 18 años requieren autorización.
    """
    
    # Implementación de la Regla de Negocio Específica de Clínica Dental
    if paciente.edad < 18 and not paciente.autorizacion_tutor:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="REGLA DE NEGOCIO DENTAL: Pacientes menores de 18 años deben contar con autorización de un tutor para el registro."
        )

    # Si el historial médico es demasiado corto o genérico (otra regla)
    if len(paciente.historial_medico) < 15:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="REGLA DE NEGOCIO DENTAL: El historial médico debe ser descriptivo (mínimo 15 caracteres)."
        )

    # Si pasa las validaciones, generar ID y almacenar
    new_id = str(uuid.uuid4())
    paciente_data = paciente.model_dump()
    DB_PACIENTES[new_id] = {**paciente_data, "id": new_id}

    return DB_PACIENTES[new_id]

@router.get("/{paciente_id}", response_model=PacienteCompleto)
def obtener_paciente(paciente_id: str):
    """Obtiene un paciente por su ID."""
    paciente = get_paciente_by_id(paciente_id)
    if not paciente:
        # Mensaje de error específico del dominio
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Paciente con ID {paciente_id} no encontrado en la Clínica Dental.")
    return paciente

