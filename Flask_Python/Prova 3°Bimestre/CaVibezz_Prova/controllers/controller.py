from flask import Blueprint, render_template, request, session, redirect, url_for, make_response, flash, abort
from datetime import datetime

blueprint_default = Blueprint("blueprint_cool", __name__)

# Página inicial
@blueprint_default.route("/")
def index():
    return redirect(url_for('blueprint_cool.login'))

#login do usuario
@blueprint_default.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form["usuario"]
        session['usuario'] = usuario  # Armazena o login na sessão
        return redirect(url_for('blueprint_cool.livros'))
    return render_template("index.html")



# Página inicial com a lista de livros
@blueprint_default.route('/livros')
def livros():
    livros = session.get('livros', [])  # Recupera livros da sessão
    total_livros = request.cookies.get('total_livros', 0)  # Conta livros do cookie
    return render_template("livros.html", livros=livros, total_livros=total_livros)

# Adicionar livro
@blueprint_default.route('/adicionar_livro', methods=['POST'])
def adicionar_livro():
    titulo = request.form.get('titulo')
    autor = request.form.get('autor')
    ano_publicação = request.form.get('ano_publicação')

    if not titulo:
        flash('////O Título do livro, deve estar  estar preecnhido para o cadastro do livro.', 'danger')
        if not ano_publicação:
            flash('////O Ano de publicação, deve estar preecnhido para o cadastro do livro.', 'danger')
        if not autor:
            flash('////O nome do autor, deve estar  estar preecnhido para o cadastro do livro.', 'danger')
        return redirect(url_for('blueprint_cool.livros'))
    
    elif not ano_publicação:
        flash('////O Ano de publicação, deve estar preecnhido para o cadastro do livro.', 'danger')
        if not autor:
            flash('////O nome do autor, deve estar  estar preecnhido para o cadastro do livro.', 'danger')
        if not titulo:
            flash('////O Título do livro, deve estar  estar preecnhido para o cadastro do livro.', 'danger')
        return redirect(url_for('blueprint_cool.livros'))
    
    elif not autor:
        flash('////O nome do autor, deve estar  estar preecnhido para o cadastro do livro.', 'danger')
        if not titulo:
            flash('////O Título do livro, deve estar  estar preecnhido para o cadastro do livro.', 'danger')
        if not ano_publicação:
            flash('////O Ano de publicação, deve estar preecnhido para o cadastro do livro.', 'danger')
        return redirect(url_for('blueprint_cool.livros'))

    
    
    livro = {
        "titulo": titulo,
        "autor": autor,
        "ano_publicação": ano_publicação or datetime.now().strftime("%d-%Y-%m")

    }

    livros = session.get('livros', [])
    livros.append(livro)
    session['livros'] = livros  # Salva na sessão

    # Incrementa o total de livros no cookie

    total_livros = int(request.cookies.get('total_livros', 0)) +1
    resp = make_response(redirect(url_for('blueprint_cool.livros')))
    resp.set_cookie('total_livros', str(total_livros), max_age=60*60)  # Expira em 1 hora

    flash('////Livro adicionada com sucesso!', 'success')
    return resp

# Logout
@blueprint_default.route('/logout')
def logout():
    session.pop('usuario', None)
    session.pop('livros', None)
    flash('////Você foi desconectado com sucesso!', 'success')
    return redirect(url_for('blueprint_cool.login'))

@blueprint_default.route('/limpar')
def limpar():
    resp = make_response(redirect(url_for('blueprint_cool.livros')))
    resp.set_cookie('total_livros', '', expires=0)  # Remove o cookie do carrinho
    session.pop('livros', None)
    flash('////Catalogo limpo com sucesso!', 'success')
    return resp

