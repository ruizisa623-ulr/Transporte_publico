from fastapi import FastAPI

from app.database.conexion import Base, engine
from app.models import ejercicio, usuario
from app.routes.ejercicio import router as ejercicio_router
from app.routes.usuarios import router as usuarios_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Transporte API")

app.include_router(ejercicio_router)
app.include_router(usuarios_router)