# ⚡ Semana 7: API de Veterinaria Optimizada (Ficha 3147246)

## 🎯 Objetivo del Proyecto

Este repositorio contiene la implementación de las técnicas avanzadas de optimización y performance para la FICHA 3147246.

El dominio asignado es Veterinaria, y el foco principal de la optimización es la consulta de Historiales médicos de las mascotas, ya que son datos consultados con alta frecuencia y contienen información crítica y potencialmente pesada.

---

## 🛠️ Estructura del Proyecto

El proyecto sigue la estructura modular recomendada para facilitar la separación de preocupaciones (FastAPI, Redis, Modelos).

app-veterinaria/
├── api/
│   └── main.py              # Rutas de la API (Endpoints)
├── core/
│   └── cache.py             # Implementación de la Práctica 23 (Redis Caching)
├── models/
│   └── schemas.py           # Definiciones de datos Pydantic (Historial Médico)
└── requirements.txt         # Dependencias del proyecto

## ⚙️ Configuración y Requisitos

Para ejecutar el proyecto localmente, necesitas tener instalados Python 3.8+ y un servidor de Redis en ejecución.

1. Requisitos de Python
Instala las dependencias necesarias:

pip install -r requirements.txt

Contenido de requirements.txt:

fastapi
uvicorn[standard]
pydantic
redis

2. Configuración de Redis
El módulo de caché (core/cache.py) asume que Redis está corriendo en la configuración por defecto (localhost:6379).

Para iniciar un servidor Redis rápidamente con Docker:

docker run --name redis-cache -p 6379:6379 -d redis

---

## 🚀 Implementación de Prácticas de Optimización

Práctica 23: Redis Caching (Veterinaria - Historiales Médicos)
Foco: Optimizar el tiempo de respuesta en la consulta de Historiales médicos, que son documentos grandes y esenciales para la operación diaria.

Implementación Clave:

Ruta Crítica: /vet/mascota/{mascota_id}/historial

Módulo: core/cache.py implementa un decorador @cache_data que chequea Redis antes de ejecutar la función real.

Clave de Caching: Se utiliza el prefijo único vet_cache seguido del identificador de la mascota (vet_cache:historial_id:vet_001).

TTL (Time To Live): 60 segundos (ajustable) para asegurar que los historiales se refresquen periódicamente en caso de actualizaciones.

Impacto Esperado:

Primer acceso (Cache Miss): Latencia alta (simulada entre 700ms - 1500ms) por consulta a la DB.

Accesos subsecuentes (Cache Hit): Latencia ultrabaja (∼50ms) al servir la respuesta directamente desde Redis.

---

## 💻 Instrucciones de Ejecución

Asegúrate de que Redis está corriendo (ver Configuración de Redis).

Ejecuta el servidor FastAPI usando Uvicorn:

uvicorn api.main:app --reload

Endpoints de Prueba
Una vez que el servidor esté en ejecución, puedes probar la optimización:

Health Check (Base):

GET /vet/status

Consulta Optimizable (Práctica 23):

GET /vet/mascota/vet_001/historial

Llama a esta ruta varias veces en un minuto y observa la diferencia de tiempo de respuesta en la terminal.

Verifica el log de la API para confirmar los eventos CACHE HIT y CACHE MISS.

---

## 💡 Próximos Pasos (Fichas 24, 25, 26)

Este proyecto está preparado para futuras implementaciones:

Práctica

Foco en Veterinaria

Práctica 24

Database Optimization: Optimizar consultas de la entidad mascota (ej. Índices en campos de búsqueda por nombre o dueño).

Práctica 25

Middleware Rate Limiting: Limitar la tasa de peticiones a endpoints costosos (ej. búsquedas avanzadas de historiales por filtros complejos) para prevenir sobrecarga.

Práctica 26

Monitoring & Profiling: Configurar Prometheus y Grafana para medir la latencia y la tasa de aciertos/fallos del caché (Cache Hit Ratio).