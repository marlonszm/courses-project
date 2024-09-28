# Arquivo de definição de rotas

# Importando um recurso,
# Utilização conforme a requisição que o cliente quer realizar
from flask_restful import Resource

# Importando schemas
from ..schemas import curso_schema

# Importando requisições, retorno de resposta das requisições e retorno
# de valores em json
from flask import request, make_response, jsonify

# Importando entidades
from ..entidades import curso

# Importando serviços
from ..services import curso_service, formacao_service

#importando a Api
from api import api

# Importando paginação
from ..paginate import paginate

# Importando os models
from ..models.curso_model import Curso

# Classe que herda o recurso importado anteriormente
class CursoList(Resource):
    def get(self):
        cs = curso_schema.CursoSchema(many=True)
        return paginate(Curso, cs)

    def post(self):
        cs = curso_schema.CursoSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json['nome']
            descricao = request.json['descricao']
            data_publicacao = request.json['data_publicacao']
            formacao = request.json['formacao']
            formacao_curso = formacao_service.listar_formacao_id(formacao)
            if formacao_curso is None:
                return make_response(jsonify("Formação não foi encontrada", 404))
            else:
                novo_curso = curso.Curso(nome = nome, descricao = descricao, data_publicacao = data_publicacao, formacao = formacao_curso)
                resultado = curso_service.cadastrar_curso(novo_curso)
                jsonifyresultado = cs.jsonify(resultado)
                return make_response(jsonifyresultado, 201)

class CursoDetail(Resource):
    def get(self, id):
        curso = curso_service.listar_curso_id(id)
        if curso is None:
            return make_response(jsonify("Curso não foi encontrado"), 404)
        else:
            cs = curso_schema.CursoSchema()
            return make_response(cs.jsonify(curso), 200)

    def put(self, id):
        curso_bd = curso_service.listar_curso_id(id)
        if curso_bd is None:
            return make_response(jsonify("Curso não foi encontrado"), 404)
        else:
            cs = curso_schema.CursoSchema()
            validate = cs.validate(request.json)
            if validate:
                return make_response(jsonify(validate), 200)
            else:
                nome = request.json['nome']
                descricao = request.json['descricao']
                data_publicacao = request.json['data_publicacao']
                formacao = request.json['formacao']
                formacao_curso = formacao_service.listar_formacao_id(formacao)
                if formacao_curso is None:
                    return make_response(jsonify("Formação não foi encontrada", 404))
                else:
                    novo_curso = curso.Curso(nome = nome, descricao = descricao, data_publicacao = data_publicacao, formacao = formacao_curso)
                    curso_service.editar_curso(curso_bd, novo_curso)
                    curso_atualizado = curso_service.listar_curso_id(id)
                    return make_response(cs.jsonify(curso_atualizado), 200)

    def delete(self, id):
        curso = curso_service.listar_curso_id(id)
        if curso is None:
            return make_response(jsonify("Curso não foi encontrado"), 404)
        else:
            curso_service.excluir_curso(curso)
            return make_response(jsonify("Curso excluido"), 204)




# Recurso que vem da classe CursoList, com a rota /cursos
api.add_resource(CursoList, '/cursos')
api.add_resource(CursoDetail, '/cursos/<int:id>')