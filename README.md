# 🚀 Cookiecutter FastAPI Clean Architecture

Plantilla profesional para proyectos **FastAPI** siguiendo los principios de **Clean Architecture** y adaptada para desarrolladores que vienen de .NET.  
Genera en segundos una estructura de carpetas lista para producción, con separación en capas, inyección de dependencias, ORM SQLAlchemy y documentación automática con Swagger.

[![Cookiecutter](https://img.shields.io/badge/built%20with-Cookiecutter-f5a623?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

---

## ✨ Características

- 🧱 **Clean Architecture** estricta: Domain, Application, Infrastructure, API.
- 🗂️ **Estructura de carpetas familiar** para desarrolladores .NET (Entities, UseCases, DTOs, Repositories, Mappers, Presenters).
- 🗄️ **SQLAlchemy** como ORM con soporte para SQLite, PostgreSQL y otros motores.
- 💉 **Inyección de dependencias** nativa de FastAPI con `Depends`.
- 📜 **Documentación automática** en `/docs` (Swagger UI) y `/redoc`.
- 🔐 Preparada para autenticación con JWT y redes sociales.
- 📦 Lista para producción con variables de entorno y migraciones con Alembic.
- 🧪 Separación de responsabilidades que facilita las pruebas unitarias.

---

## 📋 Requisitos previos

- Python 3.10 o superior
- pip
- [Cookiecutter](https://cookiecutter.readthedocs.io) instalado:

  ```bash
  pip install cookiecutter
  ```
## 🚀 Uso rápido
Para crear un nuevo proyecto a partir de esta plantilla, ejecuta:

```bash
cookiecutter https://github.com/dvnber10/cookiecutter-fastapi-clean
```
