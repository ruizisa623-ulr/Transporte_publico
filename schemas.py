from pydantic import BaseModel, ConfigDict, Field, EmailStr, field_validator

#registrar rutas
class TransporteCreate(BaseModel):
    nombre_ruta: str = Field()
    punto_origen: str = Field()
    destino: str = Field()
    distancia_km: int = Field()
    duracion: int = Field()

    @field_validator("nombre_ruta", "punto_origen", "destino")
    @classmethod
    def reject_blank_text(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("Este campo no puede estar vacío")
        return value

#devolver una ruta
class TransporteResponse(BaseModel):
    id: int
    nombre_ruta: str
    punto_origen: str
    destino: str
    distancia_km: int
    duracion: int

    model_config = ConfigDict(from_attributes=True)

#REGISTRAR usuario
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

#DEVOLVER UN usuario
class UsuarioResponse(BaseModel):
    id: int
    nombre: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)
