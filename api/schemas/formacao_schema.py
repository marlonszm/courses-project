from api import ma
from ..models import formacao_model
from marshmallow import fields
from flask import url_for
from ..schemas import curso_schema, professor_schema

# Criando Schema e suas validações de dados recebidos
class FormacaoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = formacao_model.Formacao
        load_instance = True
        fields = ("id", "nome", "descricao", "cursos", "professores", "_links")

    nome = fields.String(required=True)
    descricao = fields.String(required=True)
    cursos =  fields.List(fields.Nested(curso_schema.CursoSchema, only=('id', 'nome')))
    professores = ma.Nested(professor_schema.ProfessorSchema, many=True, only=('id', 'nome'))

    _links = fields.Method("get_links")

    def get_links(self, obj):
        return {
            "get": url_for("formacaodetail", id=obj.id) if obj.id else None,
            "put": url_for("formacaodetail", id=obj.id) if obj.id else None,
            "delete": url_for("formacaodetail", id=obj.id) if obj.id else None,
        }