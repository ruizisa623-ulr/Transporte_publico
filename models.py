from sqlalchemy import Column, Integer, String

from database import Base

class Transporte(Base):
    #nombre de la tabla
    __tablename__ = "Transporte"

    #columnas de la tabla
    id = Column(Integer, primary_key=True, index=True)
    nombre_ruta = Column(String(100), nullable=False)
    punto_origen = Column(String(100), nullable=False)
    destino = Column(String(100), nullable=False)
    distancia_km = Column(Integer, nullable=False)
    duracion = Column(Integer, nullable=False)


class Usuario(Base):
    __tablename__ = "Usuario"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    contraseña = Column(String(255), nullable=False)