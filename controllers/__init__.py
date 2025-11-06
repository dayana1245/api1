from .usuario_controller import usuario_bp, init as init_usuario
from .registro_diario_controller import registro_bp, init as init_registro
from .info_controller import info_bp

def init_app(app, usuario_service, registro_service):
    init_usuario(usuario_service)
    init_registro(registro_service)
    
    app.register_blueprint(usuario_bp, url_prefix='/api/usuarios')
    app.register_blueprint(registro_bp, url_prefix='/api/registros')
    app.register_blueprint(info_bp, url_prefix='/api')
