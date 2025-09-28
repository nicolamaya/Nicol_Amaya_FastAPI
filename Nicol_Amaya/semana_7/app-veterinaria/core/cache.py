import json
import redis
from functools import wraps
from typing import Any, Callable

# Configuración de Redis (asume un servidor local por defecto)
# En un entorno real, usarías variables de entorno para esto.
REDIS_HOST = "localhost"
REDIS_PORT = 6379

try:
    # Conexión Singleton
    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
    r.ping()
    print("Conexión con Redis exitosa.")
except redis.exceptions.ConnectionError as e:
    print(f"Error al conectar con Redis: {e}. El caching NO funcionará.")
    r = None

def get_cache_key(prefix: str, *args, **kwargs) -> str:
    """Genera una clave de caché única, usando el prefijo VET."""
    # Usamos el primer argumento posicional (ej: el ID de la mascota)
    # y el prefijo único asignado.
    identifier = args[0] if args else json.dumps(kwargs)
    return f"vet_cache:{prefix}:{identifier}"

def cache_data(prefix: str, ttl: int = 60) -> Callable:
    """
    Decorador para cachear el resultado de una función en Redis.

    :param prefix: Prefijo para la clave de Redis (ej: 'historial_id').
    :param ttl: Tiempo de vida de la caché en segundos (Time To Live).
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(*args, **kwargs) -> Any:
            if not r:
                # Si Redis no está conectado, llama a la función original
                return await func(*args, **kwargs)

            # Genera la clave usando el identificador (ej: id_mascota)
            cache_key = get_cache_key(prefix, *args, **kwargs)
            
            # 1. INTENTO DE LECTURA DE CACHÉ
            cached_data = r.get(cache_key)
            
            if cached_data:
                print(f"✅ CACHE HIT: Devolviendo datos de {cache_key}")
                # El valor debe ser parseado de vuelta al tipo de retorno
                return json.loads(cached_data)

            # 2. FALLO DE CACHÉ (MISS) - Ejecutar la función original
            result = await func(*args, **kwargs)
            
            # 3. ESCRITURA EN CACHÉ
            # La respuesta de la API (Pydantic Model) debe ser serializada
            # Usamos json.dumps, asumiendo que el resultado es serializable o un dict
            try:
                data_to_cache = result.json() if hasattr(result, 'json') else json.dumps(result)
                r.setex(cache_key, ttl, data_to_cache)
                print(f"✍️ CACHE MISS: Datos escritos en {cache_key} con TTL de {ttl}s")
            except Exception as e:
                print(f"⚠️ Error al escribir en caché: {e}")
            
            return result

        return wrapper
    return decorator