# 🦷 Proyecto de Testing y Calidad: Clínica Dental - Ficha 3147246

## 🎯 Objetivo del Proyecto
Este proyecto implementa una API RESTful básica para la gestión de Pacientes en el dominio de una Clínica Dental. El objetivo principal es desarrollar una suite de Tests de Integración y Lógica de Negocio utilizando Pytest para asegurar la calidad y el cumplimiento de las reglas específicas del negocio asignado (Clínica Dental).

Este desarrollo cumple con la metodología personalizada y los criterios de evaluación de la Ficha 3147246, enfocándose en la implementación de tests específicos y una estructura modular profesional.

## 🛠️ Tecnologías Utilizadas
Python 3.10+: Lenguaje de programación.

FastAPI: Framework moderno y rápido para construir la API.

Pydantic: Para la definición de modelos de datos y validación estricta de esquemas.

Pytest: Framework de testing para la creación de la suite de pruebas.

fastapi.testclient: Para simular peticiones HTTP y probar los endpoints.

## 📂 Estructura del Proyecto
El proyecto sigue una estructura modular para mejorar la organización, escalabilidad y facilitar el testing (criterio de Estructura Profesional):

.
├── main.py             # Punto de entrada de FastAPI y enrutamiento principal.
├── schemas.py          # Definiciones de modelos Pydantic (PacienteBase, PacienteCompleto).
├── database.py         # Simulación de la base de datos (diccionario en memoria).
├── conftest.py         # Configuración de Pytest y Fixtures esenciales (client, limpieza de DB).
├── routers/
│   └── dental.py       # Lógica de Endpoints (CRUD) para /dental/pacientes/ e implementación de Reglas de Negocio.
└── test/
    └── test_dental.py  # Suite de Tests de Lógica de Negocio Específica (Criterio 30%).

## ⚙️ Configuración y Ejecución Local
Requisitos
Asegúrate de tener Python instalado y usa pip para instalar las dependencias:

pip install fastapi uvicorn[standard] pytest

Ejecutar la API
Para levantar el servidor localmente (FastAPI):

uvicorn main:app --reload

La documentación interactiva (Swagger UI) estará disponible en http://127.0.0.1:8000/docs.

Ejecutar los Tests
Para correr la suite de pruebas y validar el cumplimiento de las reglas de negocio:

pytest test/test_dental.py

O para ver la cobertura (opcional, pero recomendado):

# Se requiere instalar pytest-cov: pip install pytest-cov
pytest test/test_dental.py --cov-report term-missing --cov=.

💉 Lógica de Negocio Específica (Clínica Dental)
La API implementa y verifica las siguientes reglas de negocio, siendo la primera la más crítica para el criterio de evaluación:

1. Regla Crítica: Autorización para Menores de Edad 🚨
Descripción: Un paciente con edad < 18 debe tener el campo autorizacion_tutor establecido en True para ser registrado.

Validación: Si un menor intenta registrarse sin autorización (autorizacion_tutor: False), la API retorna un error HTTP 400 Bad Request con un mensaje detallado (Validado por test_03_create_paciente_fail_menor_sin_auth).

2. Historial Médico Detallado
Descripción: El campo historial_medico debe ser descriptivo, con una longitud mínima para evitar registros genéricos e inútiles (e.g., "Sin" o "Ok").

Validación: Si el historial es demasiado corto, la API retorna un error HTTP 400 Bad Request (Validado por test_04_create_paciente_fail_historial_generico).

## 🧪 Suite de Tests (test/test_dental.py)
La suite de pruebas contiene fixtures personalizados y se centra en validar cada caso de éxito y de error de la lógica de negocio:

test_01_create_paciente_success_adulto: Paciente adulto (válido).

test_02_create_paciente_success_menor_con_auth: Paciente menor (válido por autorización).

test_03_create_paciente_fail_menor_sin_auth: Test Crítico de la Regla de Negocio (espera 400).

test_04_create_paciente_fail_historial_generico: Test de la segunda Regla de Negocio (espera 400).

test_05_get_paciente_not_found: Prueba de ruta GET con error (espera 404).

Este README.md fue generado para el dominio de Clínica Dental asignado a la Ficha 3147246.