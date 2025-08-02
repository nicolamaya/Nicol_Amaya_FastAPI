# Mi Primera API FastAPI - Bootcamp

**👤 Desarrollador**: Nicol Amaya
**📧 Email**: 199396618+nicolamaya@users.noreply.github.com.
**� Privacidad**: Email configurado según mejores prácticas de GitHub
**�📅 Fecha de creación**: 2025-08-02 16:24:34
**📂 Ruta del proyecto**: /c/Users/Administrador/Desktop/FastAPI_Nicol/mi-primera-api-fastapi
**💻 Equipo de trabajo**: BOGDFPCGMP5673

## 🔧 Configuración Local

Este proyecto está configurado para trabajo en equipo compartido:

- **Entorno virtual aislado**: `venv-personal/`
- **Configuración Git local**: Solo para este proyecto
- **Dependencias independientes**: No afecta otras instalaciones

## 🚀 Instalación y Ejecución

```bash
# 1. Activar entorno virtual personal
source venv-personal/bin/activate

# 2. Instalar dependencias (si es necesario)
pip install -r requirements.txt

# 3. Ejecutar servidor de desarrollo
uvicorn main:app --reload --port 8000
```

## 📝 Notas del Desarrollador

- **Configuración Git**: Local únicamente, no afecta configuración global
- **Email de GitHub**: Configurado con email privado para proteger información personal
- **Entorno aislado**: Todas las dependencias en venv-personal/
- **Puerto por defecto**: 8000 (cambiar si hay conflictos)
- **Estado del bootcamp**: Semana 1 - Configuración inicial

## 🛠️ Troubleshooting Personal

- Si el entorno virtual no se activa: `rm -rf venv-personal && python3 -m venv venv-personal`
- Si hay conflictos de puerto: cambiar --port en uvicorn
- Si Git no funciona: verificar `git config user.name` y `git config user.email`
- Si necesitas cambiar el email: usar el email privado de GitHub desde Settings → Emails



# Mi Primera API FastAPI

# REFLEXIÓN: 

- La experiencia de desarrollo es muy buena con FastAPI
- Genera automáticamente documentación interactiva y validación de datos
- Lo anterior ayuda a reducir significativamente los errores en tiempo de ejecución


## ¿Qué hace?

Una API básica creada en el Bootcamp FastAPI Semana 1.

## ¿Cómo ejecutar?

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```