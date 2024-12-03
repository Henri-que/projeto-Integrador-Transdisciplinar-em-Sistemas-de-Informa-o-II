from decimal import Decimal
from functools import wraps
from flask import render_template, redirect, url_for, flash, request, session
from flask_login import login_required, login_user
from app import db
from app.models import Usuario, Livro, Reserva
from flask_login import current_user
from flask import Blueprint

bp = Blueprint('main', __name__)


@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form.get('nome')
        sobrenome = request.form.get('sobrenome')
        email = request.form.get('email')
        cpf = request.form.get('cpf')
        idade = request.form.get('idade')

        if not nome or not sobrenome or not email or not cpf or not idade:
            flash('Por favor, preencha todos os campos.')
            return redirect(url_for('main.index'))

        try:
            idade = int(idade)
        except ValueError:
            flash('Idade inválida. Por favor, insira um número inteiro.')
            return redirect(url_for('main.index'))

        usuario = Usuario(nome=nome, sobrenome=sobrenome, email=email, cpf=cpf, idade=idade)
        db.session.add(usuario)
        db.session.commit()

        login_user(usuario)

        flash('Cadastro realizado com sucesso!')
        return redirect(url_for('main.index'))

    reservas = Reserva.query.all()
    livros = Livro.query.all()
    return render_template('index.html', reservas=reservas, livros=livros, Usuario=Usuario)



@bp.route('/livros')
@login_required
def listar_livros():
    livros = Livro.query.all()
    return render_template('livro.html', livros=livros, livro=None, Usuario=Usuario)


@bp.route('/livro/<int:livro_id>')
@login_required
def livro(livro_id):
    livro = Livro.query.get_or_404(livro_id)
    return render_template('livro.html', livro=livro, Usuario=Usuario)

@bp.route('/reserva/<int:livro_id>', methods=['GET', 'POST'])
@login_required
def reserva(livro_id):
    livro = Livro.query.get_or_404(livro_id)
    if request.method == 'POST':
        usuario_id = request.form.get('usuario')
        if usuario_id:
            try:
                usuario_id = int(usuario_id)
                usuario = Usuario.query.get(usuario_id)

                if usuario:
                    reserva = Reserva(livro_id=livro_id, usuario_id = usuario_id)
                    db.session.add(reserva)
                    db.session.commit()


                    flash('Livro reservado com sucesso!')
                    return redirect(url_for('main.index'))
                else:
                    flash('Usuário não encontrado!')
            except ValueError:
                flash('ID de usuário inválido. Por favor, insira um número inteiro.')
        else:
            flash('Selecione um usuário para fazer a reserva.')

    usuarios = Usuario.query.all()
    return render_template('reserva.html', livro=livro, usuarios=usuarios)


@bp.route('/comprar/<int:livro_id>')
@login_required
def comprar_livro(livro_id):
    livro = Livro.query.get_or_404(livro_id)
    return render_template('comprar.html', livro=livro)


@bp.route('/processar_pagamento/<int:livro_id>', methods=['POST'])
@login_required
def processar_pagamento(livro_id):
    livro = Livro.query.get_or_404(livro_id)
    forma_pagamento = request.form['forma_pagamento']
    flash(f'Compra do livro {livro.titulo} foi realizada com sucesso usando {forma_pagamento}.')
    return redirect(url_for('main.index'))


@bp.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('usuario_id', None)

    flash('Logout realizado com sucesso!')
    return redirect(url_for('main.index'))

@bp.route('/finalizar_reserva', methods=['GET', 'POST'])
@login_required
def finalizar_reserva():
    reservas_usuario = Reserva.query.filter_by(usuario_id=current_user.id).all()
    total = Decimal(0)

    for reserva in reservas_usuario:
        total += Decimal(str(reserva.livro.preco))

    if request.method == 'POST':
        flash('Reserva finalizada com sucesso!', 'success')
        return redirect(url_for('main.index'))

    return render_template('finalizar_reserva.html', reservas=reservas_usuario, total=total)