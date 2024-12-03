from app import create_app, db
from app.models import Livro, Usuario, Reserva

app = create_app()
with app.app_context():
    db.create_all()

    if Livro.query.count() == 0:
        livros = [
        Livro(titulo="Dom Casmurro", autor="Machado de Assis", preco=39.90, imagem_url="imagens/dom_Casmurro.jpg"),
        Livro(titulo="O Alquimista", autor="Paulo Coelho", preco=29.90, imagem_url="imagens/o_alquimista.jpg"),
        Livro(titulo="1984", autor="George Orwell", preco=49.90, imagem_url="imagens/1984.jpg"),
        Livro(titulo="A Revolução dos Bichos", autor="George Orwell", preco=19.90, imagem_url="imagens/a_Revolução_dos_Bichos.jpg"),
        Livro(titulo="O Pequeno Príncipe", autor="Antoine de Saint-Exupéry", preco=24.90, imagem_url="imagens/o_Pequeno_Príncipe.jpg"),
        Livro(titulo="Cem Anos de Solidão", autor="Gabriel García Márquez", preco=59.90, imagem_url="imagens/cem_Anos_de_Solidão.jpg"),
        Livro(titulo="A Moreninha", autor="Joaquim Manuel de Macedo", preco=34.90, imagem_url="imagens/a_Moreninha.jpg"),
        Livro(titulo="O Senhor dos Anéis: A Sociedade do Anel", autor="J.R.R. Tolkien", preco=69.90, imagem_url="imagens/o_Senhor_dos_Anéis_a_Sociedade_do_Anel.jpg"),
        Livro(titulo="O Hobbit", autor="J.R.R. Tolkien", preco=39.90, imagem_url="imagens/o_Hobbit.jpg"),
        Livro(titulo="A Menina que Roubava Livros", autor="Markus Zusak", preco=34.90, imagem_url="imagens/a_Menina_que_Roubava_Livros.jpg"),
        Livro(titulo="Orgulho e Preconceito", autor="Jane Austen", preco=29.90, imagem_url="imagens/orgulho_e_Preconceito.jpg"),
        Livro(titulo="A Arte da Guerra", autor="Sun Tzu", preco=19.90, imagem_url="imagens/a_Arte_da_Guerra.jpg"),
        Livro(titulo="O Morro dos Ventos Uivantes", autor="Emily Brontë", preco=39.90, imagem_url="imagens/o_Morro_dos_Ventos_Uivantes.jpg"),
        Livro(titulo="Fahrenheit 451", autor="Ray Bradbury", preco=29.90, imagem_url="imagens/Fahrenheit 451.jpg"),
        Livro(titulo="O Diário de Anne Frank", autor="Anne Frank", preco=34.90, imagem_url="imagens/O Diário de Anne Frank.jpg"),
        Livro(titulo="A Culpa é das Estrelas", autor="John Green", preco=29.90, imagem_url="imagens/A Culpa é das Estrelas.jpg"),
        Livro(titulo="O Lobo da Estepe", autor="Hermann Hesse", preco=39.90, imagem_url="imagens/O Lobo da Estepe.jpg"),
        Livro(titulo="O Processo", autor="Franz Kafka", preco=34.90, imagem_url="imagens/O Processo.jpg"),
        Livro(titulo="O Estrangeiro", autor="Albert Camus", preco=29.90, imagem_url="imagens/O Estrangeiro.jpg"),
        Livro(titulo="A Metamorfose", autor="Franz Kafka", preco=19.90, imagem_url="imagens/A Metamorfose.jpg"),
    ]

    db.session.bulk_save_objects(livros)

    if Usuario.query.filter_by(email='teste@example.com').first() is None:
        usuario1 = Usuario(nome="Usuario Teste", sobrenome="Teste", email="teste@example.com", cpf="123.456.789-00", idade=30)
        db.session.add(usuario1)

    db.session.commit()
    print("Banco de dados inicializado com sucesso!")