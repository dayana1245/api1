from flask import Blueprint, request, jsonify
from services.registro_diario_service import RegistroDiarioService
from .auth_middleware import token_required

registro_bp = Blueprint('registros', __name__)
_registro_service = None

def init(registro_service: RegistroDiarioService):
    global _registro_service
    _registro_service = registro_service

@registro_bp.route('/registros', methods=['POST'])
@token_required
def crear_registro(user_id: int):
    data = request.get_json()
    try:
        registro = _registro_service.create_registro(
            usuario_id=user_id,
            datos=data
        )
        return jsonify({
            'message': 'Registro creado exitosamente',
            'id': registro.id
        }), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@registro_bp.route('/registros', methods=['GET'])
@token_required
def obtener_registros(user_id: int):
    registros = _registro_service.get_registros_usuario(user_id)
    return jsonify([{
        'id': r.id,
        'fecha': r.fecha_registro,
        'mood_level': r.mood_level,
        'stability': r.stability,
        'motivation': r.motivation,
        # ... otros campos ...
    } for r in registros])

@registro_bp.route('/registros/<int:registro_id>', methods=['GET'])
@token_required
def obtener_registro(registro_id: int, user_id: int):
    registro = _registro_service.get_by_id(registro_id)
    if not registro or registro.usuario_id != user_id:
        return jsonify({'error': 'Registro no encontrado'}), 404
    return jsonify(registro)
