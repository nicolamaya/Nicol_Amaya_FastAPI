from fastapi import FastAPI
from routers import dental
import uvicorn

app = FastAPI(
    title="API Clínica Dental - Ficha 3147246",
    description="Implementación modular para la tarea de Testing y Calidad."
)

# Incluir el router personalizado
app.include_router(dental.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)