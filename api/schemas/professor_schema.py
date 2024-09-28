from api import ma
from ..models import professor_model
from marshmallow import fields
from flask import  url_for

# Criando Schema e suas validações de dados recebidos
class ProfessorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = professor_model.Professor
        load_instance = True
        fields = ("id", "nome", "idade", "_links")

    nome = fields.String(required=True)
    idade = fields.Integer(required=True)

    _links = fields.Method("get_links")

    def get_links(self, obj):
        return {
            "get": url_for("professordetail", id=obj.id) if obj.id else None,
            "put": url_for("professordetail", id=obj.id) if obj.id else None,
            "delete": url_for("professordetail", id=obj.id) if obj.id else None,
        }