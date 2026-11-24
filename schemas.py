from pydantic import BaseModel, ConfigDict, Field

#registrar rutas
class TransporteCreate(BaseModel):
    nombre_ruta: str = Field()
    punto_origen: str = Field()
    destino: str = Field()
    distancia_km: int = Field()
    duracion: int = Field()

#devolver una ruta
class TransporteResponse(BaseModel):
    id: int
    nombre_ruta: str
    punto_origen: str
    destino: str
    distancia_km: int
    duracion: int

    Model_config = ConfigDict(from_attributes=True)
