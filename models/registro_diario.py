from sqlalchemy import Column, Integer, String, DateTime, Boolean, SmallInteger, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from . import Base

class RegistroDiario(Base):
    __tablename__ = 'registros_diario'

    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id', ondelete='CASCADE'), nullable=True)
    fecha_registro = Column(DateTime, server_default=func.now())

    # Métricas de estado de ánimo
    mood_level = Column(SmallInteger)      # 1-10
    stability = Column(SmallInteger)       # 1-5
    irritability = Column(SmallInteger)    # 1-5
    motivation = Column(SmallInteger)      # 1-10
    anxiety = Column(SmallInteger)         # 1-10

    # Hábitos y rutinas
    sleep_hours = Column(String(50))
    eating = Column(String(255))
    physical_activity = Column(String(255))
    took_meds = Column(Boolean)
    substances = Column(String(255))

    # Interacción social
    sociability = Column(SmallInteger)     # 1-5
    conflicts = Column(String(255))
    emotional_support = Column(SmallInteger)  # 1-5

    # Bienestar general
    daily_feeling = Column(String(255))
    concentration = Column(SmallInteger)    # 1-5
    control_level = Column(SmallInteger)    # 1-5
    negative_thoughts = Column(String(255))

    # Relación con Usuario
    usuario = relationship('Usuario', backref='registros_diario')
