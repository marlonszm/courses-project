# Arquivo de definição de rotas

# Importando um recurso,
# Utilização conforme a requisição que o cliente quer realizar
from flask_restful import Resource

# Importando schemas
from ..schemas import login_schema

# Importando requisições, retorno de resposta das requisições e retorno
# de valores em json
from flask import request, make_response, jsonify

# Importando entidades
from ..entidades import usuario

# Importando serviços
from ..services import usuario_service

# Model
from ..models.usuario_model import Usuario


# Importações do token de acesso JWT
from flask_jwt_extended import create_access_token
from datetime import timedelta

#importando a Api
from api import api

# Classe que herda o recurso importado anteriormente
class LoginList(Resource):
    def post(self):
        ls = login_schema.LoginSchema()
        validate = ls.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            email = request.json['email']
            senha = request.json['senha']
            usuario_bd = usuario_service.listar_usuario_email(email)
            if usuario_bd and usuario_bd.ver_senha(senha):
                access_token = create_access_token(
                    identity=usuario_bd.id,
                    expires_delta=timedelta(seconds=100)
                )
                return make_response(jsonify({
                    "access_token": access_token,
                    "message": "Login realizado com sucesso"
                }), 200)
            else:
                return make_response(jsonify({
                    'message': "As credencias estão inválidas"
                }), 200)
# Recurso que vem da classe CursoList, com a rota /cursos
api.add_resource(LoginList, '/login')
