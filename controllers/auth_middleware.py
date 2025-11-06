from functools import wraps
from flask import request, jsonify
import jwt
from datetime import datetime, timedelta
import os

JWT_SECRET = os.getenv('JWT_SECRET', 'your-secret-key')

def generate_token(user_id: int) -> str:
    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(days=1)
    }
    return jwt.encode(payload, JWT_SECRET, algorithm='HS256')

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token no proporcionado'}), 401

        try:
            token = token.split(' ')[1]  # Eliminar "Bearer "
            data = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])
            kwargs['user_id'] = data['user_id']
        except:
            return jsonify({'message': 'Token inválido'}), 401

        return f(*args, **kwargs)
    return decorated
