from fastapi import HTTPException, status
from pwdlib import PasswordHash

from app.models.usuario import Usuario
from app.repositories.usuario_repository import UsuarioRepository
from app.schemas.usuario import UsuarioCreate

password_hash = PasswordHash.recommended()


class UsuarioService:
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    def list(self):
        return self.repository.list()

    def get(self, usuario_id: int):
        usuario = self.repository.get(usuario_id)
        if usuario is None:
            raise HTTPException(status_code=404, detail="usuario not found")
        return usuario

    def create(self, data: UsuarioCreate):
        if self.repository.get_by_email(data.email):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already registered",
            )

        usuario = Usuario(
            nombre=data.nombre,
            email=data.email,
            contraseña=password_hash.hash(data.contraseña),
        )
        return self.repository.create(usuario)

    def update(self, usuario_id: int, data: UsuarioCreate):
        usuario = self.get(usuario_id)
        duplicated = self.repository.get_by_email(data.email)
        if duplicated and duplicated.id != usuario_id:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already registered",
            )

        usuario.nombre = data.nombre
        usuario.email = data.email
        usuario.contraseña = password_hash.hash(data.contraseña)
        return self.repository.update(usuario)

    def delete(self, usuario_id: int):
        usuario = self.get(usuario_id)
        self.repository.delete(usuario)
        return {"message": "usuario deleted successfully"}
