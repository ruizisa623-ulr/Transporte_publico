from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator


class UsuarioCreate(BaseModel):
    nombre: str = Field()
    email: EmailStr = Field()
    contraseña: str = Field(min_length=8)

    @field_validator("nombre")
    @classmethod
    def reject_blank_name(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("El nombre no puede estar vacío")
        return value

    @field_validator("contraseña")
    @classmethod
    def reject_blank_password(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("La contraseña no puede estar vacía")
        return value


class UsuarioResponse(BaseModel):
    id: int
    nombre: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)
