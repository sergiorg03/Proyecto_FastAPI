from fastapi import HTTPException
from sqlalchemy.orm import Session
from app import models
from datetime import date

'''
    Recintos
'''

def crear_recinto(db: Session, recinto):
    nuevo = models.Recinto(**recinto.dict())

    if nuevo.capacidad < 0:
        raise HTTPException(400, "La capacidad no puede ser negativa")

    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


def listar_recintos(db: Session):
    return db.query(models.Recinto).all()

def obtener_recinto(db: Session, id: int):
    recinto = db.query(models.Recinto).get(id)
    if not recinto:
        raise HTTPException(404, "Recinto no encontrado")
    return recinto

def actualizar_recinto(db: Session, id: int, datos):
    # Obtenemos el recinto de la BD
    recinto_db = db.query(models.Recinto).get(id)

    # Si no existe el recinto lanzamos un error 404
    if not recinto_db:
        raise HTTPException(404, "Recinto no encontrado")

    if datos.capacidad < 0:
        raise HTTPException(400, "La capacidad no puede ser negativa")

    # Cambiamos los datos
    recinto_db.ciudad = datos.ciudad
    recinto_db.nombre = datos.nombre
    recinto_db.capacidad = datos.capacidad

    # Guardamos
    db.commit()
    db.refresh(recinto_db)
    return recinto_db

def eliminar_recinto(db: Session, id: int):
    recinto_db = db.query(models.Recinto).get(id)

    if not recinto_db:
        raise HTTPException(404, "Recinto no encontrado")

    # Eliminamos los eventos asociados a dicho recinto
    eventos = db.query(models.Evento).filter(models.Evento.recinto_id == id).all()
    for evento in eventos:
        db.delete(evento)
    db.commit()

    # Eliminamos el recinto
    db.delete(recinto_db)
    db.commit()
    return recinto_db

'''
    Eventos
'''

def crear_evento(db: Session, evento):
    
    # Comprobamos que el id del recinto exista
    recinto = db.query(models.Recinto).get(evento.recinto_id)
    if not recinto:
        raise HTTPException(404, "Recinto no existente")

    if evento.precio < 0:
        raise HTTPException(400, "El precio no puede ser negativo")

    if evento.fecha < date.today():
        raise HTTPException(400, "La fecha no puede ser pasada")

    nuevo = models.Evento(**evento.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


def listar_eventos(db: Session, ciudad: str = None):
    query = db.query(models.Evento).join(models.Recinto) # Obtenemos los datos del evento de la DB y unimos tablas

    # Filtramos por ciudad si se introduce
    if ciudad:
        # Filtramos por el campo 'ciudad' de la tabla 'Recinto'
        query = query.filter(models.Recinto.ciudad.ilike(f"%{ciudad}%"))

    # Devolvemos los datos
    return query.all()


def comprar_tickets(db: Session, evento_id: int, cantidad: int):
    evento = db.query(models.Evento).get(evento_id)

    # Comprobamos que el evento exista
    if not evento:
        raise HTTPException(404, "Evento no encontrado")

    # comprobamos que el id del recinto exista
    recinto = db.query(models.Recinto).get(evento.recinto_id)
    if not recinto:
        raise HTTPException(404, "Recinto no existente")

    # Comprobamos que haya aforo suficiente
    if evento.tickets_vendidos + cantidad > evento.recinto.capacidad:
        raise HTTPException(400, "Aforo insuficiente en el recinto")

    # Comprobamos que la cantidad sea positiva
    if cantidad < 0:
        raise HTTPException(400, "La cantidad debe ser positiva")
    
    # Realizamos la venta de entradas
    evento.tickets_vendidos += cantidad
    db.commit()
    db.refresh(evento)
    return evento
