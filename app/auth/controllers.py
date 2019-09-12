from flask import request, jsonify
from flask import current_app as app
from app import db
from . import auth
import jwt
from .models import User, users_share_schema, user_share_schema


@auth.route('/')
def home():
    return "Hello World"


@auth.route('/api/auth/register', methods=["POST"])
def register_user():
    if request.get_json():
        username = request.json['username']
        email = request.json['email']
        password = request.json['password']
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        result = User.query.filter_by(email=email).first()
        return user_share_schema.dump(result)
    return {'error':'requisição vazia'}

@auth.route('/api/auth/login', methods=['POST'])
def login():
    if request.get_json():
        email = request.json['email']
        password = request.json['password']
        user = User.query.filter_by(email=email).first_or_404()
        if not user.verify_password(password):
            return jsonify({
                'error':'Credenciais invalidas'
            }),403

        payload = {
            "id": user.id
        }
        token = jwt.encode(payload,app.config['SECRET_KEY'])
        return jsonify({"token":token.decode('utf-8')})
