from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app(config_class=Config):
    """Cria e configura a instância da aplicação Flask.

    Args:
        config_class: Classe de configuração a ser usada para configurar a aplicação.

    Returns:
        app: A instância da aplicação Flask configurada.
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Inicializa as extensões com a aplicação
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Define a rota de login e a mensagem de erro para acesso não autorizado
    login_manager.login_view = 'main.index'
    login_manager.login_message = "Você precisa estar logado para acessar essa página."
    login_manager.user_loader(load_user)

    # Importa e registra o blueprint principal da aplicação
    from app.routes import bp as main_bp
    app.register_blueprint(main_bp)

    # Manipulador de erro para página não encontrada (404)
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('404.html'), 404

    # Manipulador de erro para erro interno do servidor (500)
    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        return render_template('500.html'), 500

    return app

def load_user(user_id):
    from app.models import Usuario
    try:
        return Usuario.query.get(int(user_id))
    except (TypeError, ValueError):
        return None