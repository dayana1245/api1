from flask import Flask
from flask_cors import CORS
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from repositories.usuario_repository import UsuarioRepository
from repositories.registro_diario_repository import RegistroDiarioRepository
from services.usuario_service import UsuarioService
from services.registro_diario_service import RegistroDiarioService
from controllers import init_app
import os
import logging

# Configuración de base de datos
def get_database_url():
    # Intentar usar MySQL primero
    mysql_url = os.getenv('DATABASE_URL')
    if mysql_url:
        try:
            engine = create_engine(mysql_url)
            engine.connect()
            return mysql_url
        except Exception as e:
            logging.warning(f"No se pudo conectar a MySQL: {e}")
    
    # Usar SQLite como fallback
    sqlite_path = os.path.join(os.path.dirname(__file__), 'database.sqlite')
    return f'sqlite:///{sqlite_path}'

DATABASE_URL = get_database_url()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crear tablas
Base.metadata.create_all(bind=engine)

def create_app():
    app = Flask(__name__)
    CORS(app)  # Habilitar CORS

    # Configurar sesión de base de datos
    db_session = SessionLocal()

    # Configurar repositorios
    usuario_repository = UsuarioRepository(db_session)
    registro_repository = RegistroDiarioRepository(db_session)

    # Configurar servicios
    usuario_service = UsuarioService(usuario_repository)
    registro_service = RegistroDiarioService(registro_repository)

    # Inicializar controladores
    init_app(app, usuario_service, registro_service)

    # Manejador de errores global
    @app.errorhandler(Exception)
    def handle_error(e):
        return {
            "error": str(e),
            "status": getattr(e, 'code', 500)
        }, getattr(e, 'code', 500)

    # Limpiar sesión al finalizar cada petición
    @app.teardown_appcontext
    def cleanup(exc):
        db_session.close()

    return app

if __name__ == '__main__':
    app = create_app()
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
