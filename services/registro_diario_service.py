from typing import List, Optional, Dict, Any
from datetime import datetime
from models.registro_diario import RegistroDiario
from repositories.registro_diario_repository import RegistroDiarioRepository
from .base_service import BaseService

class RegistroDiarioService(BaseService[RegistroDiario]):
    def __init__(self, repository: RegistroDiarioRepository):
        super().__init__(repository)
        self.registro_repository = repository

    def create_registro(self, usuario_id: int, datos: Dict[str, Any]) -> RegistroDiario:
        nuevo_registro = RegistroDiario(
            usuario_id=usuario_id,
            mood_level=datos.get('mood_level'),
            stability=datos.get('stability'),
            irritability=datos.get('irritability'),
            motivation=datos.get('motivation'),
            anxiety=datos.get('anxiety'),
            sleep_hours=datos.get('sleep_hours'),
            eating=datos.get('eating'),
            physical_activity=datos.get('physical_activity'),
            took_meds=datos.get('took_meds'),
            substances=datos.get('substances'),
            sociability=datos.get('sociability'),
            conflicts=datos.get('conflicts'),
            emotional_support=datos.get('emotional_support'),
            daily_feeling=datos.get('daily_feeling'),
            concentration=datos.get('concentration'),
            control_level=datos.get('control_level'),
            negative_thoughts=datos.get('negative_thoughts')
        )
        return self.repository.create(nuevo_registro)

    def get_registros_usuario(self, usuario_id: int) -> List[RegistroDiario]:
        return self.registro_repository.get_by_usuario_id(usuario_id)

    def get_registros_periodo(self, fecha_inicio: str, fecha_fin: str) -> List[RegistroDiario]:
        return self.registro_repository.get_registros_by_fecha(fecha_inicio, fecha_fin)
