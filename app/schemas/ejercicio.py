from pydantic import BaseModel, ConfigDict, Field, field_validator


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


class TransporteResponse(BaseModel):
    id: int
    nombre_ruta: str
    punto_origen: str
    destino: str
    distancia_km: int
    duracion: int

    model_config = ConfigDict(from_attributes=True)
