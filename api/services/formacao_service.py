# Arquivo específico para interagir com o SQLAlchemye oferecer os serviços da aplicação (métodos)
from ..models import formacao_model
from .professor_service import listar_professor_id
from api import db

# Cadastro de formação
def cadastrar_formacao(formacao):
    formacao_bd = formacao_model.Formacao(nome=formacao.nome, descricao=formacao.descricao)
    for i in formacao.professores:
        professor = listar_professor_id(i)
        formacao.professores.append(professor)
    db.session.add(formacao_bd)
    db.session.commit()
    return formacao_bd

# Listagem de formacao
def listar_formacao():
    formacoes = formacao_model.Formacao.query.all()
    return formacoes

# Listagem de formacao por ID
def listar_formacao_id(id):
    formacao = formacao_model.Formacao.query.filter_by(id=id).first()
    return formacao

# Editar formacao
def editar_formacao(formacao_anterior, formacao_novo):
    formacao_anterior.nome = formacao_novo.nome
    formacao_anterior.descricao = formacao_novo.descricao
    formacao_anterior.professores = []
    for i in formacao_novo.professores:
        professor = listar_professor_id(i)
        formacao_anterior.professores.append(professor)
    db.session.commit()

# Deletar formacao
def excluir_formacao(formacao):
    db.session.delete(formacao)
    db.session.commit()
