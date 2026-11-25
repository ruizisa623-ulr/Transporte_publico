from sqlalchemy import Column, Integer, String

from app.database.conexion import Base


class Usuario(Base):
    __tablename__ = "Usuario"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    contraseña = Column(String(255), nullable=False)
