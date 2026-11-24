from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from models import Transporte
from schemas import TransporteCreate, TransporteResponse

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Servicio API")