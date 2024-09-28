from api import ma
from ..models import curso_model
from flask import url_for
from marshmallow import fields

# Criando Schema e suas validações de dados recebidos
class CursoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = curso_model.Curso
        load_instance = True
        fields = ("id", "nome", "descricao", "data_publicacao", "formacao", "_links")

    nome = fields.String(required=True)
    descricao = fields.String(required=True)
    data_publicacao = fields.Date(required=True)
    formacao = fields.String(required=True)

    _links = fields.Method("get_links")

    def get_links(self, obj):
        return {
            "get": url_for("cursodetail", id=obj.id) if obj.id else None,
            "put": url_for("cursodetail", id=obj.id) if obj.id else None,
            "delete": url_for("cursodetail", id=obj.id) if obj.id else None,
        }