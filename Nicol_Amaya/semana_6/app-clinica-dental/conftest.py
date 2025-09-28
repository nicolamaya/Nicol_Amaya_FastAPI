import pytest
from fastapi.testclient import TestClient
from main import app # Importa la app principal
from database import clear_db # Importa la función de limpieza

@pytest.fixture(scope="module")
def client():
    """Cliente de prueba para FastAPI (ejecución única)."""
    return TestClient(app)

@pytest.fixture(autouse=True)
def clean_db_before_test():
    """Limpia la base de datos simulada antes de cada test."""
    clear_db()
    yield

# --- FIXTURES DE DATOS ESPECÍFICOS PARA CLÍNICA DENTAL ---

@pytest.fixture
def paciente_adulto_valido():
    """Datos de un paciente adulto válido (Caso Éxito)."""
    return {
        "nombre": "Sofia Montoya",
        "edad": 35,
        "historial_medico": "Ninguna alergia conocida. Última visita hace 6 meses.",
        "tipo_sangre": "A+",
        "contacto_emergencia": "3009876543",
        "autorizacion_tutor": False 
    }

@pytest.fixture
def paciente_menor_sin_autorizacion():
    """Datos de un paciente menor de edad SIN autorización (Caso Error: Regla de Negocio)."""
    return {
        "nombre": "Camilo Torres",
        "edad": 15,
        "historial_medico": "Asma leve, sin medicación actual.",
        "tipo_sangre": "O-",
        "contacto_emergencia": "3101234567",
        "autorizacion_tutor": False # Esto DEBE causar un error 400
    }

@pytest.fixture
def paciente_menor_con_autorizacion():
    """Datos de un paciente menor de edad CON autorización (Caso Éxito)."""
    data = paciente_menor_sin_autorizacion() # Reutiliza los datos base
    data["autorizacion_tutor"] = True # Solamente cambia la autorización a True
    return data