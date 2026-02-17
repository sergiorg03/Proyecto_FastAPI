from pydantic import BaseModel
from datetime import date

'''
    Recintos
'''

class RecintoBase(BaseModel):
    nombre: str
    ciudad: str
    capacidad: int

class RecintoCreate(RecintoBase):
    pass

class RecintoResponse(RecintoBase):
    id: int

    class Config:
        from_attributes = True

class RecintoUpdate(RecintoBase):
    nombre: str
    ciudad: str
    capacidad: int

'''
    Eventos
'''

class EventoCreate(BaseModel):
    nombre: str
    fecha: date
    precio: float
    recinto_id: int

class EventoResponse(EventoCreate):
    id: int
    tickets_vendidos: int

    class Config:
        from_attributes = True
