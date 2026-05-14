from fastapi import FastAPI
from api.routes import router as api_router
from infraestructure.data.database import engine, Base

app = FastAPI(
    title="{{ cookiecutter.project_name }}",
    description="{{ cookiecutter.description }}",
    version="1.0.0"
)

app.include_router(api_router, prefix="/api")

# Crear tablas automáticamente en desarrollo (opcional)

Base.metadata.create_all(bind=engine)
