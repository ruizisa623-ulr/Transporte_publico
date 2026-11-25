from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Optional

from database import Base, engine, get_db
from models import Transporte, Usuario
from schemas import TransporteCreate, TransporteResponse
from schemas import UsuarioCreate, UsuarioResponse
from pwdlib import PasswordHash

#importar el hash para las contraseñas
password_hash = PasswordHash.recommended()

#crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Transporte API")

#Consultar rutas, con filtros
@app.get("/transporte", response_model=list[TransporteResponse])
def get_transporte(
    punto_origen: Optional[str] = None,
    destino: Optional[str] = None,
    db: Session = Depends(get_db)
):
    consulta = db.query(Transporte)

    if punto_origen:
        consulta = consulta.filter(
            Transporte.punto_origen == punto_origen
        )

    if destino:
        consulta = consulta.filter(
            Transporte.destino == destino
        )

    return consulta.all()

#GET consultar una ruta por id
@app.get("/transporte/{transporte_id}", response_model=TransporteResponse)
def get_transporte(
    transporte_id: int,
    db: Session = Depends(get_db)
):
    transporte = db.query(Transporte).filter(
        Transporte.id == transporte_id
    ).first()

    if transporte is None:
        raise HTTPException(
            status_code=404,
            detail="ruta no encontrada"
        )

    return transporte

#POST registrar una ruta
@app.post(
    "/transporte",
    response_model=TransporteResponse,
    status_code=status.HTTP_201_CREATED
)
def create_transporte(
    transporte_data: TransporteCreate,
    db: Session = Depends(get_db)
):
    transporte = Transporte(
        nombre_ruta=transporte_data.nombre_ruta,
        punto_origen=transporte_data.punto_origen,
        destino=transporte_data.destino,
        distancia_km=transporte_data.distancia_km,
        duracion=transporte_data.duracion
    )
    db.add(transporte)
    db.commit()
    db.refresh(transporte)
    return transporte

#PUT actualizar una ruta por id
@app.put("/transporte/{transporte_id}", response_model=TransporteResponse)
def update_transporte(
    transporte_id: int,
    transporte_data: TransporteCreate,
    db: Session = Depends(get_db)
):
    transporte = db.query(Transporte).filter(
        Transporte.id == transporte_id
    ).first()

    if transporte is None:
        raise HTTPException(
            status_code=404,
            detail="ruta no encontrada"
        )


    #actualizar los campos de la ruta
    transporte.nombre_ruta = transporte_data.nombre_ruta
    transporte.punto_origen = transporte_data.punto_origen
    transporte.destino = transporte_data.destino
    transporte.distancia_km = transporte_data.distancia_km
    transporte.duracion = transporte_data.duracion

    db.commit()
    db.refresh(transporte)
    return transporte


#DELETE eliminar una ruta por id
@app.delete("/transporte/{transporte_id}")
def delete_transporte(
    transporte_id: int,
    db: Session = Depends(get_db)
): 
    transporte = db.query(Transporte).filter(
        Transporte.id == transporte_id
    ).first()

    if transporte is None:
        raise HTTPException(
            status_code=404,
            detail="ruta not found"
        )

    db.delete(transporte)
    db.commit()

    return {
        "message": "ruta delete successfully"
    }


#GET consultar todos los usuarios
@app.get("/usuario", response_model=list[UsuarioResponse])
def get_usuario(db: Session = Depends(get_db)):
    usuario = db.query(Usuario).all()
    return usuario


#GET consultar un usuario por id
@app.get("/usuario/{usuario_id}", response_model=UsuarioResponse)
def get_usuario(
    usuario_id: int,
    db: Session = Depends(get_db)
):
    usuario = db.query(Usuario).filter(
        Usuario.id == usuario_id
    ).first()

    if usuario is None:
        raise HTTPException(
            status_code=404,
            detail="usuario not found"
        )
    
    return usuario

#POST registrar un usuario
@app.post(
    "/usuario",
    response_model=UsuarioResponse,
    status_code=status.HTTP_201_CREATED
)
def create_usuario(
    usuario_data: UsuarioCreate,
    db: Session = Depends(get_db)
):
    #validar que el correo no este registrado
    existing = db.query(Usuario).filter(
        Usuario.email == usuario_data.email
    ).first()

   # evitar correo duplicados
    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered"
        )

    usuario = Usuario(
        nombre=usuario_data.nombre,
        email=usuario_data.email,
        contraseña=password_hash.hash(usuario_data.contraseña)
    )

    db.add(usuario)
    db.commit()
    db.refresh(usuario)

    return usuario



#PUT ACTUALIZAR UN USUARIO POR ID
@app.put("/usuario/{usuario_id}", response_model=UsuarioResponse)
def update_usuario(
    usuario_id: int,
    usuario_data: UsuarioCreate,
    db: Session = Depends(get_db)
):
    usuario = db.query(Usuario).filter(
        Usuario.id == usuario_id
    ).first()

    if usuario is None:
        raise HTTPException(
            status_code=404,
            detail="usuario not found"
        )


    # Validar que el correo no pertenezca a otra persona
    duplicated = db.query(Usuario).filter(
        Usuario.email == usuario_data.email,
        Usuario.id != usuario_id
    ).first()

    if duplicated:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered"
        )

    usuario.nombre = usuario_data.nombre
    usuario.email = usuario_data.email
    usuario.contraseña = password_hash.hash(usuario_data.contraseña)

    db.commit()
    db.refresh(usuario)

    return usuario



#DELETE eliminar un usuario por el id
@app.delete("/usuario/{usuario_id}")
def delete_usuario(
    usuario_id: int,
    db: Session = Depends(get_db)
):
    usuario = db.query(Usuario).filter(
        Usuario.id == usuario_id
    ).first()

    if usuario is None:
        raise HTTPException(
            status_code=404,
            detail="usuario not found"
        )

    db.delete(usuario)
    db.commit()

    return {
        "message": "usuario deleted successfully"
    }