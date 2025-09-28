from fastapi import FastAPI, HTTPException
from core.cache import cache_data
from models.schemas import HistorialMedico, DocumentoMedico
import random
import time
from typing import Dict

app = FastAPI(title="API Veterinaria Optimizada (FICHA 3147246)")

# Datos simulados de ejemplo (como si vinieran de PostgreSQL)
# El historial más consultado es el que se debe cachear.
MOCK_DATABASE: Dict[str, HistorialMedico] = {
    "vet_001": HistorialMedico(
        id_mascota="vet_001",
        nombre_mascota="Fido",
        especie="Canino",
        raza="Golden Retriever",
        documentos=[
            DocumentoMedico(tipo="Vacunación", fecha="2024-01-15", descripcion="Vacuna Rabia anual.", veterinario="Dr. Smith"),
            DocumentoMedico(tipo="Diagnóstico", fecha="2024-05-20", descripcion="Revisión general, dieta especial.", veterinario="Dra. Lopez"),
        ],
        ultima_actualizacion="2024-09-28T10:00:00Z"
    )
}

# ----------------------------------------------------
# 📌 PRÁCTICA 23: REDIS CACHING
# ----------------------------------------------------

@app.get("/vet/mascota/{mascota_id}/historial", response_model=HistorialMedico)
@cache_data(prefix="historial_id", ttl=60)
async def get_historial_medico_optimizado(mascota_id: str):
    """
    Ruta CRÍTICA: Obtiene el Historial Médico completo de una mascota.
    Implementación de Caching para Historiales muy consultados.
    """
    
    # ⚠️ SIMULACIÓN DE LATENCIA ALTA SIN CACHE
    # (Simulando una consulta pesada a PostgreSQL o lectura de archivo grande)
    simulated_delay = random.uniform(0.7, 1.5)
    time.sleep(simulated_delay) 
    
    if mascota_id not in MOCK_DATABASE:
        raise HTTPException(status_code=404, detail="Mascota no encontrada")

    historial = MOCK_DATABASE[mascota_id]
    
    # Añadimos un campo para demostrar la latencia
    historial_dict = historial.dict()
    historial_dict['performance_info'] = {
        'simulated_latency_ms': round(simulated_delay * 1000, 2),
        'source': 'POSTGRESQL_DB_CALL'
    }
    
    print(f"❌ CACHE MISS: Consulta real a la DB, tiempo: {round(simulated_delay * 1000)}ms")
    return HistorialMedico(**historial_dict)

# ----------------------------------------------------
# 💡 ENDPOINT BASE PARA COMPARACIÓN
# ----------------------------------------------------

@app.get("/vet/status")
async def get_status():
    """Endpoint simple de health check."""
    return {"status": "ok", "message": "API Veterinaria está en línea."}