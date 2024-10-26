# Arquivo de definição de rotas

# Importando um recurso,
# Utilização conforme a requisição que o cliente quer realizar
from flask_restful import Resource

# Importando schemas
from ..schemas import usuario_schema

# Importando requisições, retorno de resposta das requisições e retorno
# de valores em json
from flask import request, make_response, jsonify

# Importando entidades
from ..entidades import usuario

# Importando serviços
from ..services import usuario_service

# Model
from ..models.usuario_model import Usuario

#importando a Api
from api import api

import uuid

# Classe que herda o recurso importado anteriormente
class UsuarioList(Resource):
    def post(self):
        us = usuario_schema.UsuarioSchema()
        validate = us.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json['nome']
            email = request.json['email']
            senha = request.json['senha']
            is_admin = request.json['is_admin']
            api_key = str(uuid.uuid4())
            novo_usuario = usuario.Usuario(nome= nome, email=email, senha= senha, is_admin=is_admin, api_key=api_key)
            resultado = usuario_service.cadastrar_usuario(novo_usuario)
            jsonifyresultado = us.jsonify(resultado)
            return make_response(jsonifyresultado, 201)

# Recurso que vem da classe CursoList, com a rota /cursos
api.add_resource(UsuarioList, '/usuario')
