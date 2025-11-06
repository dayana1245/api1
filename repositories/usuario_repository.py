from sqlalchemy.orm import Session
from models.usuario import Usuario
from .base_repository import BaseRepository

class UsuarioRepository(BaseRepository[Usuario]):
    def __init__(self, session: Session):
        super().__init__(session, Usuario)

    def get_by_email(self, email: str) -> Usuario:
        return self.session.query(Usuario).filter(Usuario.email == email).first()
