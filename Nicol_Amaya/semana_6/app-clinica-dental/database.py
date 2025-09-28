from typing import Dict

# Base de datos simulada en memoria para Pacientes
# Se usará para almacenar los diccionarios de pacientes
DB_PACIENTES: Dict[str, dict] = {}

# Función para limpiar la base de datos (utilizada en conftest.py)
def clear_db():
    DB_PACIENTES.clear()

# Función para simular un "obtener" en la DB
def get_paciente_by_id(paciente_id: str):
    return DB_PACIENTES.get(paciente_id)