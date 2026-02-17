from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.deps import get_db
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="EventMaster API")

@app.get("/")
def root():
    return {"msg": "API funcionando"}


'''
    Recintos
'''

@app.post("/recintos/", response_model=schemas.RecintoResponse)
def crear_recinto(
    recinto: schemas.RecintoCreate,
    db: Session = Depends(get_db)
):
    return crud.crear_recinto(db, recinto)



@app.get("/recintos/", response_model=list[schemas.RecintoResponse])
def listar_recintos(db: Session = Depends(get_db)):
    return crud.listar_recintos(db)

@app.get("/recintos/{id}", response_model=schemas.RecintoResponse)
def obtener_recinto(id: int, db: Session = Depends(get_db)):
    return crud.obtener_recinto(db, id)

@app.put("/recintos/{id}", response_model=schemas.RecintoResponse)
def actualizar_recinto(id: int, recinto: schemas.RecintoUpdate, db: Session = Depends(get_db)):
    return crud.actualizar_recinto(db, id, recinto)

@app.delete("/recintos/{id}")
def eliminar_recinto(id: int, db: Session = Depends(get_db)):
    return crud.eliminar_recinto(db, id)

'''
    Eventos
'''

@app.post("/eventos/", response_model=schemas.EventoResponse)
def crear_evento(evento: schemas.EventoCreate, db: Session = Depends(get_db)):
    return crud.crear_evento(db, evento)


@app.get("/eventos/", response_model=list[schemas.EventoResponse])
def listar_eventos(ciudad: str = None, db: Session = Depends(get_db)):
    return crud.listar_eventos(db, ciudad)


@app.patch("/eventos/{id}/comprar")
def comprar_evento(id: int, cantidad: int, db: Session = Depends(get_db)):
    return crud.comprar_tickets(db, id, cantidad)
