from typing import Optional
from models.usuario import Usuario
from repositories.usuario_repository import UsuarioRepository
from .base_service import BaseService
from werkzeug.security import generate_password_hash, check_password_hash

class UsuarioService(BaseService[Usuario]):
    def __init__(self, repository: UsuarioRepository):
        super().__init__(repository)
        self.usuario_repository = repository

    def create_usuario(self, nombre: str, email: str, contrasena: str) -> Usuario:
        # Verificar si el email ya existe
        if self.usuario_repository.get_by_email(email):
            raise ValueError("El email ya está registrado")
        
        # Crear nuevo usuario con contraseña hasheada
        nuevo_usuario = Usuario(
            nombre=nombre,
            email=email,
            contrasena=generate_password_hash(contrasena)
        )
        return self.repository.create(nuevo_usuario)

    def authenticate_usuario(self, email: str, contrasena: str) -> Optional[Usuario]:
        usuario = self.usuario_repository.get_by_email(email)
        if usuario and check_password_hash(usuario.contrasena, contrasena):
            return usuario
        return None
