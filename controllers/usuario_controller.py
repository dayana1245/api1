from flask import Blueprint, request, jsonify
from services.usuario_service import UsuarioService
from .auth_middleware import generate_token

usuario_bp = Blueprint('usuarios', __name__)
_usuario_service = None

def init(usuario_service: UsuarioService):
    global _usuario_service
    _usuario_service = usuario_service

@usuario_bp.route('/registro', methods=['POST'])
def registro():
    data = request.get_json()
    try:
        usuario = _usuario_service.create_usuario(
            nombre=data['nombre'],
            email=data['email'],
            contrasena=data['contrasena']
        )
        return jsonify({
            'message': 'Usuario registrado exitosamente',
            'id': usuario.id
        }), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@usuario_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    usuario = _usuario_service.authenticate_usuario(
        email=data['email'],
        contrasena=data['contrasena']
    )
    
    if usuario:
        token = generate_token(usuario.id)
        return jsonify({
            'token': token,
            'usuario': {
                'id': usuario.id,
                'nombre': usuario.nombre,
                'email': usuario.email
            }
        })
    return jsonify({'error': 'Credenciales inválidas'}), 401
