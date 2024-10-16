# Arquivo de definição de rotas

# Importando um recurso,
# Utilização conforme a requisição que o cliente quer realizar
from flask_restful import Resource

# Importando schemas
from ..schemas import professor_schema

# Importando requisições, retorno de resposta das requisições e retorno
# de valores em json
from flask import request, make_response, jsonify

# Importando entidades
from ..entidades import professor

# Importando serviços
from ..services import professor_service

# Paginação
from ..paginate import paginate

# Model
from ..models.professor_model import Professor

#importando a Api
from api import api

from flask_jwt_extended import jwt_required

# Classe que herda o recurso importado anteriormente
class ProfessorList(Resource):
    @jwt_required()
    def get(self):
        ps = professor_schema.ProfessorSchema(many=True)
        return paginate(Professor, ps)
    @jwt_required()
    def post(self):
        ps = professor_schema.ProfessorSchema()
        validate = ps.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json['nome']
            idade = request.json['idade']
            novo_professor = professor.Professor(nome = nome, idade = idade)
            resultado = professor_service.cadastrar_professor(novo_professor)
            jsonifyresultado = ps.jsonify(resultado)
            return make_response(jsonifyresultado, 201)

class ProfessorDetail(Resource):
    @jwt_required()
    def get(self, id):
        professores = professor_service.listar_professor_id(id)
        if professores is None:
            return make_response(jsonify("Professor não foi encontrado"), 404)
        else:
            ps = professor_schema.ProfessorSchema()
            return make_response(ps.jsonify(professores), 200)
    @jwt_required()
    def put(self, id):
        professor_bd = professor_service.listar_professor_id(id)
        if professor_bd is None:
            return make_response(jsonify("Professor não foi encontrado"), 404)
        else:
            ps = professor_schema.ProfessorSchema()
            validate = ps.validate(request.json)
            if validate:
                return make_response(jsonify(validate), 200)
            else:
                nome = request.json['nome']
                idade = request.json['idade']
                novo_professor = professor.Professor(nome = nome, idade = idade)
                professor_service.editar_professor(professor_bd, novo_professor)
                professor_atualizado = professor_service.listar_professor_id(id)
                return make_response(ps.jsonify(professor_atualizado), 200)
    @jwt_required()
    def delete(self, id):
        professor = professor_service.listar_professor_id(id)
        if professor is None:
            return make_response(jsonify("Formação não foi encontrada"), 404)
        else:
            professor_service.excluir_professor(professor)
            return make_response(jsonify("Formação excluida"), 204)




# Recurso que vem da classe CursoList, com a rota /cursos
api.add_resource(ProfessorList, '/professores')
api.add_resource(ProfessorDetail, '/professores/<int:id>')