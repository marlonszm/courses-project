# importação de db do módulo api
from api import db

# biblioteca de encrypt e decrypt
from passlib.hash import pbkdf2_sha256

# Criação das tabelas via extensão da classe db
class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome= db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    senha = db.Column(db.String(255), nullable=False)

    def encriptar_senha(self):
        self.senha = pbkdf2_sha256.hash(self.senha)

    def ver_senha(self, senha):
        return pbkdf2_sha256.verify(senha, self.senha)