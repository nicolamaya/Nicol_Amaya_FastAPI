# 🏥 PetHealth API: Gestión Veterinaria (Tipo A)

## 🎯 Objetivo del Proyecto

Este repositorio contiene la implementación de una **API RESTful** para el dominio **Sistema Veterinario PetHealth**, clasificado bajo el **Tipo A (Gestión de Datos)**.

El enfoque principal de este proyecto es la aplicación de metodologías de **Testing Automatizado** (Pytest) y **Calidad de Código** (Prácticas 27-30), asegurando la integridad de las operaciones **CRUD** sobre los registros de pacientes veterinarios.

---

## 🏗️ Estructura del Directorio

El proyecto sigue una estructura limpia que separa la lógica de las rutas (routers) de las pruebas (tests):

app-veterinaria-pethealth/
├── app/
│   ├── routers/
│   │   ├── patient_routes.py    # Rutas CRUD de la API (Core de Gestión de Datos)
│   └── main.py                  # Archivo principal de la aplicación Flask
└── tests/
├── init.py
├── conftest.py              # (Vacío, pero listo para Fixtures universales)
└── test_patient_routes.py   # Tests de Integración Pytest para las rutas CRUD

---

## 🚀 Instalación y Uso

### 1. Requisitos

Asegúrate de tener **Python 3.x** y **pip** instalados.

### 2. Entorno Virtual

```bash
python -m venv venv
source venv/bin/activate  # En Linux/macOS
# o .\venv\Scripts\activate  # En Windows