# Solemne FastAPI Time

API simple desarrollada con **FastAPI** que expone el endpoint `/time` y devuelve la **fecha y hora actual** en formato JSON.

Este proyecto fue realizado usando **uv** para la gestión del entorno virtual, **pytest** para pruebas, **Docker** para contenerización y **GitHub Actions** para automatizar linting, testing y publicación de la imagen en Docker Hub.

La hora es obtenida desde la **Hora Oficial de Chile** utilizando la librería **ntplib** y consultando el servidor **ntp.shoa.cl**.

## Dependencias usadas

- Python 3.12
- FastAPI
- Uvicorn
- uv
- Pytest
- Ruff
- Docker
- GitHub Actions

## Estructura general del proyecto

- `main.py`: aplicación FastAPI y endpoint `/time`
- `test_main.py`: pruebas unitarias
- `pyproject.toml`: configuración del proyecto y dependencias
- `uv.lock`: bloqueo de dependencias con uv
- `Dockerfile`: contenerización de la aplicación
- `.github/workflows/main.yml`: flujo CI/CD con GitHub Actions

## Ejecución local con uv

Ubícate en la carpeta del proyecto, donde se encuentra `pyproject.toml`.

### 1. Instalar dependencias
uv sync

### 2. Ejecutar la aplicacion localmente
uv run python -m uvicorn main:app --host 127.0.0.1 --port 8000

Probar en el navegador: http://127.0.0.1:8000/time

### 3. Ejecutar Pytest

uv run python -m pytest

### 4. Instrucciones para ejecutar la aplicación con Docker
Antes de ejecutar estos comandos, asegúrate de estar en la carpeta donde se encuentra el archivo Dockerfile.

a) Construir la imagen Docker

docker build -t taller-fastapi-time .

b) Ejecutar el contenedor Docker

docker run -p 8000:8000 taller-fastapi-time

c) Abrir en el navegador

http://127.0.0.1:8000/time

### 5. Instrucciones para testear el API

## Opción 1: desde el navegador web
Abrir: http://127.0.0.1:8000/time

## Opción 2: usando curl
curl http://127.0.0.1:8000/time
