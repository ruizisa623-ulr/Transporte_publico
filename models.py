from sqlalchemy import Colum, Integer, String

from database import Base

class Transporte(Base):
    #nombre de la tabla
    __tablename__ = "Transporte"

    #columnas de la tabla
    id = Colum(Integer, primary_key=True, index=True)
    nombre_ruta = Colum(String(100), nullable=False)
    punto_origen = Colum(String(100), nullable=False)
    destino = Colum(String(100), nullable=False)
    distancia_km = Colum(Integer, nullable=False)
    duracion = Colum(Integer, nullable=False)