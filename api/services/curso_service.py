# Arquivo específico para interagir com o SQLAlchemye oferecer os serviços da aplicação (métodos)
from ..models import curso_model
from api import db

# Cadastro de curso
def cadastrar_curso(curso):
    curso_bd = curso_model.Curso(nome=curso.nome, descricao=curso.descricao, data_publicacao=curso.data_publicacao, formacao = curso.formacao)
    db.session.add(curso_bd)
    db.session.commit()
    return curso_bd

# Listagem de cursos
def listar_cursos():
    cursos = curso_model.Curso.query.all()
    return cursos

# Listagem de cursos por ID
def listar_curso_id(id):
    curso = curso_model.Curso.query.filter_by(id=id).first()
    return curso

# Editar curso
def editar_curso(curso_anterior, curso_novo):
    curso_anterior.nome = curso_novo.nome
    curso_anterior.descricao = curso_novo.descricao
    curso_anterior.data_publicacao = curso_novo.data_publicacao
    curso_anterior.formacao = curso_novo.formacao
    db.session.commit()

# Deletar curso
def excluir_curso(curso):
    db.session.delete(curso)
    db.session.commit()
