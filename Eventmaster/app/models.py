from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Recinto(Base):
    __tablename__ = "recintos"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    ciudad = Column(String, nullable=False)
    capacidad = Column(Integer, nullable=False)

    eventos = relationship("Evento", back_populates="recinto")


class Evento(Base):
    __tablename__ = "eventos"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    fecha = Column(Date, nullable=False)
    precio = Column(Float, nullable=False)
    tickets_vendidos = Column(Integer, default=0)

    recinto_id = Column(Integer, ForeignKey("recintos.id"), nullable=False)
    recinto = relationship("Recinto", back_populates="eventos")
