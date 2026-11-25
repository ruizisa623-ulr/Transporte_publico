from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database.conexion import get_db
from app.repositories.usuario_repository import UsuarioRepository
from app.schemas.usuario import UsuarioCreate, UsuarioResponse
from app.services.usuario_service import UsuarioService

router = APIRouter(prefix="/usuario", tags=["usuario"])


def get_service(db: Session = Depends(get_db)) -> UsuarioService:
    return UsuarioService(UsuarioRepository(db))


@router.get("", response_model=list[UsuarioResponse])
def get_usuarios(service: UsuarioService = Depends(get_service)):
    return service.list()


@router.get("/{usuario_id}", response_model=UsuarioResponse)
def get_usuario(
    usuario_id: int,
    service: UsuarioService = Depends(get_service),
):
    return service.get(usuario_id)


@router.post(
    "",
    response_model=UsuarioResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_usuario(
    data: UsuarioCreate,
    service: UsuarioService = Depends(get_service),
):
    return service.create(data)


@router.put("/{usuario_id}", response_model=UsuarioResponse)
def update_usuario(
    usuario_id: int,
    data: UsuarioCreate,
    service: UsuarioService = Depends(get_service),
):
    return service.update(usuario_id, data)


@router.delete("/{usuario_id}")
def delete_usuario(
    usuario_id: int,
    service: UsuarioService = Depends(get_service),
):
    return service.delete(usuario_id)
