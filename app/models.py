from falcon.errors import datetime
from flask_login import UserMixin

from app import db

class Livro(db.Model):
    """Modelo que representa um livro na base de dados."""
    __tablename__ = 'livro'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    autor = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    imagem_url = db.Column(db.String(200), nullable=True)

    def __init__(self, titulo, autor, preco, imagem_url):
        """Inicializa uma nova instância do modelo Livro.

        Args:
            titulo (str): Título do livro.
            autor (str): Autor do livro.
            preco (float): Preço do livro.
            imagem_url (str): URL da imagem do livro.
        """
        self.titulo = titulo
        self.autor = autor
        self.preco = preco
        self.imagem_url = imagem_url


class Reserva(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    livro_id = db.Column(db.Integer, db.ForeignKey('livro.id'), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    data_reserva = db.Column(db.DateTime, default=datetime.utcnow)


    livro = db.relationship('Livro', backref='reservas_livros')
    usuario = db.relationship('Usuario', backref='reservas_usuarios')


class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    sobrenome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(20), nullable=False)
    idade = db.Column(db.Integer, nullable=False)


    def __repr__(self):
        return f'<Usuário {self.nome} {self.sobrenome}>'