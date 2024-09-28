# Arquivo de definição de rotas

# Importando um recurso,
# Utilização conforme a requisição que o cliente quer realizar
from flask_restful import Resource

# Importando schemas
from ..schemas import formacao_schema

# Importando requisições, retorno de resposta das requisições e retorno
# de valores em json
from flask import request, make_response, jsonify

# Importando entidades
from ..entidades import formacao

# Importando serviços
from ..services import formacao_service

# Importando paginação
from ..paginate import paginate

# Importando modelo
from ..models.formacao_model import Formacao

#importando a Api
from api import api

# Classe que herda o recurso importado anteriormente
class FormacaoList(Resource):
    def get(self):
        fs = formacao_schema.FormacaoSchema(many=True)
        return paginate(Formacao, fs)
    def post(self):
        fs = formacao_schema.FormacaoSchema()
        validate = fs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json['nome']
            descricao = request.json['descricao']
            professores = request.json['professores']
            nova_formacao = formacao.Formacao(nome = nome, descricao = descricao, professores = professores)
            resultado = formacao_service.cadastrar_formacao(nova_formacao)
            jsonifyresultado = fs.jsonify(resultado)
            return make_response(jsonifyresultado, 201)

class FormacaoDetail(Resource):
    def get(self, id):
        formacao = formacao_service.listar_formacao_id(id)
        if formacao is None:
            return make_response(jsonify("Formação não foi encontrada"), 404)
        else:
            fs = formacao_schema.FormacaoSchema()
            return make_response(fs.jsonify(formacao), 200)

    def put(self, id):
        formacao_bd = formacao_service.listar_formacao_id(id)
        if formacao_bd is None:
            return make_response(jsonify("Formação não foi encontrada"), 404)
        else:
            fs = formacao_schema.FormacaoSchema()
            validate = fs.validate(request.json)
            if validate:
                return make_response(jsonify(validate), 200)
            else:
                nome = request.json['nome']
                descricao = request.json['descricao']
                professores = request.json['professores']
                nova_formacao = formacao.Formacao(nome=nome, descricao=descricao, professores=professores)
                formacao_service.editar_formacao(formacao_bd, nova_formacao)
                formacao_atualizado = formacao_service.listar_formacao_id(id)
                return make_response(fs.jsonify(formacao_atualizado), 200)

    def delete(self, id):
        formacao = formacao_service.listar_formacao_id(id)
        if formacao is None:
            return make_response(jsonify("Formação não foi encontrada"), 404)
        else:
            formacao_service.excluir_formacao(formacao)
            return make_response(jsonify("Formação excluida"), 204)




# Recurso que vem da classe CursoList, com a rota /cursos
api.add_resource(FormacaoList, '/formacoes')
api.add_resource(FormacaoDetail, '/formacoes/<int:id>')