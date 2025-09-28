import pytest
from fastapi.testclient import TestClient

# Prefijo de la URL: /dental/pacientes
URL_PACIENTES = "/dental/pacientes/"

class TestDentalAPI:
    """
    Suite de tests para la API de la Clínica Dental (AMAYA BEJARANO).
    Se enfoca en validar la lógica de negocio específica.
    """

    # --- TESTS DE ÉXITO ---

    def test_01_create_paciente_success_adulto(self, client, paciente_adulto_valido):
        """
        Test de Éxito: Creación de un paciente adulto válido.
        """
        response = client.post(URL_PACIENTES, json=paciente_adulto_valido)
        assert response.status_code == 201
        data = response.json()
        assert data["nombre"] == "Sofia Montoya"
        assert data["edad"] == 35

    def test_02_create_paciente_success_menor_con_auth(self, client, paciente_menor_con_autorizacion):
        """
        Test de Éxito: Creación de un paciente menor DE EDAD CON autorización.
        Valida que la regla de negocio se cumple correctamente.
        """
        response = client.post(URL_PACIENTES, json=paciente_menor_con_autorizacion)
        assert response.status_code == 201
        data = response.json()
        assert data["autorizacion_tutor"] is True
        assert data["edad"] < 18

    # --- TESTS DE ERROR (Lógica de Negocio Única) ---

    def test_03_create_paciente_fail_menor_sin_auth(self, client, paciente_menor_sin_autorizacion):
        """
        TEST CRÍTICO DE REGLA DE NEGOCIO (30% de la evaluación): 
        Debe fallar si el paciente es menor de edad y NO tiene autorización_tutor=True.
        """
        response = client.post(URL_PACIENTES, json=paciente_menor_sin_autorizacion)
        
        # Debe devolver un error 400 (Bad Request)
        assert response.status_code == 400
        
        # Validar el mensaje de error Específico del Dominio
        detail = response.json()["detail"]
        assert "REGLA DE NEGOCIO DENTAL" in detail
        assert "menores de 18 años deben contar con autorización" in detail

    def test_04_create_paciente_fail_historial_generico(self, client, paciente_adulto_valido):
        """
        Test de error único: El historial médico no puede ser demasiado corto o vacío 
        (ej: 'Sin' o 'Ok') por la importancia de la información en una clínica.
        """
        invalid_data = paciente_adulto_valido.copy()
        invalid_data["historial_medico"] = "Sin" # Menos de 15 caracteres
        
        response = client.post(URL_PACIENTES, json=invalid_data)
        
        # Debe devolver un error 400 (Bad Request)
        assert response.status_code == 400
        assert "historial médico debe ser descriptivo" in response.json()["detail"]

    def test_05_get_paciente_not_found(self, client):
        """
        Test de error: Intenta obtener un paciente que no existe.
        El mensaje de error debe ser específico.
        """
        fake_id = "9999-9999-9999-9999"
        response = client.get(f"{URL_PACIENTES}{fake_id}")
        
        # Debe devolver un error 404
        assert response.status_code == 404
        assert "no encontrado en la Clínica Dental" in response.json()["detail"]