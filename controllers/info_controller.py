from flask import Blueprint, jsonify

info_bp = Blueprint('info', __name__)

@info_bp.route('/info', methods=['GET'])
def get_api_info():
    return jsonify({
        "api_name": "API de Registro Diario de Estado de Ánimo",
        "version": "1.0.0",
        "descripcion": "API para el seguimiento del estado de ánimo y hábitos diarios",
        "endpoints": {
            "auth": {
                "/api/usuarios/registro": {
                    "method": "POST",
                    "description": "Registrar nuevo usuario",
                    "body": {
                        "nombre": "string",
                        "email": "string",
                        "contrasena": "string"
                    }
                },
                "/api/usuarios/login": {
                    "method": "POST",
                    "description": "Iniciar sesión",
                    "body": {
                        "email": "string",
                        "contrasena": "string"
                    }
                }
            },
            "registros": {
                "/api/registros": {
                    "GET": {
                        "description": "Obtener todos los registros del usuario",
                        "auth": "Bearer token requerido"
                    },
                    "POST": {
                        "description": "Crear nuevo registro diario",
                        "auth": "Bearer token requerido",
                        "body": {
                            "mood_level": "int (1-10)",
                            "stability": "int (1-5)",
                            "motivation": "int (1-10)",
                            "anxiety": "int (1-10)",
                            "sleep_hours": "string",
                            "eating": "string",
                            "physical_activity": "string"
                        }
                    }
                },
                "/api/registros/<id>": {
                    "GET": {
                        "description": "Obtener un registro específico",
                        "auth": "Bearer token requerido"
                    }
                }
            }
        },
        "autenticacion": {
            "tipo": "JWT Bearer Token",
            "formato": "Authorization: Bearer <token>",
            "validez": "24 horas"
        }
    })
