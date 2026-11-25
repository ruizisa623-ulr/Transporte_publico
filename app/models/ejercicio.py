from sqlalchemy import Column, Integer, String

from app.database.conexion import Base


class Transporte(Base):
    __tablename__ = "Transporte"

    id = Column(Integer, primary_key=True, index=True)
    nombre_ruta = Column(String(100), nullable=False)
    punto_origen = Column(String(100), nullable=False)
    destino = Column(String(100), nullable=False)
    distancia_km = Column(Integer, nullable=False)
    duracion = Column(Integer, nullable=False)
