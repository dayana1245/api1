from sqlalchemy.orm import Session
from typing import List
from models.registro_diario import RegistroDiario
from .base_repository import BaseRepository

class RegistroDiarioRepository(BaseRepository[RegistroDiario]):
    def __init__(self, session: Session):
        super().__init__(session, RegistroDiario)

    def get_by_usuario_id(self, usuario_id: int) -> List[RegistroDiario]:
        return self.session.query(RegistroDiario)\
            .filter(RegistroDiario.usuario_id == usuario_id)\
            .all()

    def get_registros_by_fecha(self, fecha_inicio: str, fecha_fin: str) -> List[RegistroDiario]:
        return self.session.query(RegistroDiario)\
            .filter(RegistroDiario.fecha_registro.between(fecha_inicio, fecha_fin))\
            .all()
