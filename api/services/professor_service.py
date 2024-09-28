# Arquivo específico para interagir com o SQLAlchemye oferecer os serviços da aplicação (métodos)
from ..models import professor_model
from api import db

# Cadastro de professor
def cadastrar_professor(professor):
    professor_bd = professor_model.Professor(nome=professor.nome, idade=professor.idade)
    db.session.add(professor_bd)
    db.session.commit()
    return professor_bd

# Listagem de professor
def listar_professor():
    professores = professor_model.Professor.query.all()
    return professores

# Listagem de professor por ID
def listar_professor_id(id):
    professor = professor_model.Professor.query.filter_by(id=id).first()
    return professor

# Editar professor
def editar_professor(professor_anterior, professor_novo):
    professor_anterior.nome = professor_novo.nome
    professor_anterior.idade = professor_novo.idade
    db.session.commit()

# Deletar professor
def excluir_professor(professor):
    db.session.delete(professor)
    db.session.commit()
