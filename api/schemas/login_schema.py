from api import ma
from ..models import usuario_model
from marshmallow import fields

# Criando Schema e suas validações de dados recebidos
class LoginSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = usuario_model.Usuario
        load_instance = True
        fields = ("id", "nome", "email", "senha")

    nome = fields.String(required=False)
    email = fields.String(required=True)
    senha = fields.String(required=True)
