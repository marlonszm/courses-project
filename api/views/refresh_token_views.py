# Arquivo de definição de rotas

# Importando um recurso,
# Utilização conforme a requisição que o cliente quer realizar
from flask_restful import Resource


# Importando requisições, retorno de resposta das requisições e retorno
# de valores em json
from flask import request, make_response, jsonify

# Importações do token de acesso JWT
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from datetime import timedelta

#importando a Api
from api import api

# Classe que herda o recurso importado anteriormente
class RefreshTokenList(Resource):
    @jwt_required(refresh=True)
    def post(self):
        usuario_token = get_jwt_identity()
        access_token = create_access_token(
            identity=usuario_token,
            expires_delta=timedelta(seconds=100)
        )
        refresh_token = create_refresh_token(
            identity=usuario_token
        )
        return make_response({
            'access_token': access_token,
            'refresh_token': refresh_token
        }, 200)
# Recurso que vem da classe CursoList, com a rota /cursos
api.add_resource(RefreshTokenList, '/token/refresh')
