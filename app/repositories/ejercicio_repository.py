from sqlalchemy.orm import Session

from app.models.ejercicio import Transporte
from app.schemas.ejercicio import TransporteCreate


class EjercicioRepository:
    def __init__(self, db: Session):
        self.db = db

    def list(self, punto_origen: str | None = None, destino: str | None = None):
        consulta = self.db.query(Transporte)
        if punto_origen:
            consulta = consulta.filter(Transporte.punto_origen == punto_origen)
        if destino:
            consulta = consulta.filter(Transporte.destino == destino)
        return consulta.all()

    def get(self, transporte_id: int):
        return self.db.query(Transporte).filter(
            Transporte.id == transporte_id
        ).first()

    def create(self, data: TransporteCreate):
        transporte = Transporte(**data.model_dump())
        self.db.add(transporte)
        self.db.commit()
        self.db.refresh(transporte)
        return transporte

    def update(self, transporte: Transporte, data: TransporteCreate):
        for field, value in data.model_dump().items():
            setattr(transporte, field, value)
        self.db.commit()
        self.db.refresh(transporte)
        return transporte

    def delete(self, transporte: Transporte):
        self.db.delete(transporte)
        self.db.commit()
