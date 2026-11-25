from fastapi import HTTPException

from app.repositories.ejercicio_repository import EjercicioRepository
from app.schemas.ejercicio import TransporteCreate


class EjercicioService:
    def __init__(self, repository: EjercicioRepository):
        self.repository = repository

    def list(self, punto_origen: str | None = None, destino: str | None = None):
        return self.repository.list(punto_origen, destino)

    def get(self, transporte_id: int):
        transporte = self.repository.get(transporte_id)
        if transporte is None:
            raise HTTPException(status_code=404, detail="ruta no encontrada")
        return transporte

    def create(self, data: TransporteCreate):
        return self.repository.create(data)

    def update(self, transporte_id: int, data: TransporteCreate):
        transporte = self.get(transporte_id)
        return self.repository.update(transporte, data)

    def delete(self, transporte_id: int):
        transporte = self.get(transporte_id)
        self.repository.delete(transporte)
        return {"message": "ruta delete successfully"}
