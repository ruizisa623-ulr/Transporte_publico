from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.conexion import get_db
from app.repositories.ejercicio_repository import EjercicioRepository
from app.schemas.ejercicio import TransporteCreate, TransporteResponse
from app.services.ejercicio_service import EjercicioService

router = APIRouter(prefix="/transporte", tags=["transporte"])


def get_service(db: Session = Depends(get_db)) -> EjercicioService:
    return EjercicioService(EjercicioRepository(db))


@router.get("", response_model=list[TransporteResponse])
def get_transporte(
    punto_origen: str | None = None,
    destino: str | None = None,
    service: EjercicioService = Depends(get_service),
):
    return service.list(punto_origen, destino)


@router.get("/{transporte_id}", response_model=TransporteResponse)
def get_transporte_by_id(
    transporte_id: int,
    service: EjercicioService = Depends(get_service),
):
    return service.get(transporte_id)


@router.post(
    "",
    response_model=TransporteResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_transporte(
    data: TransporteCreate,
    service: EjercicioService = Depends(get_service),
):
    return service.create(data)


@router.put("/{transporte_id}", response_model=TransporteResponse)
def update_transporte(
    transporte_id: int,
    data: TransporteCreate,
    service: EjercicioService = Depends(get_service),
):
    return service.update(transporte_id, data)


@router.delete("/{transporte_id}")
def delete_transporte(
    transporte_id: int,
    service: EjercicioService = Depends(get_service),
):
    return service.delete(transporte_id)
