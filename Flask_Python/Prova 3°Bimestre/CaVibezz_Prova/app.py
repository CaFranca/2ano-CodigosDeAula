from flask import Flask, render_template,flash,session,request,abort
from controllers.controller import blueprint_default as pagina

app = Flask(__name__)
app.secret_key = 'top_seguranca'  # Defina uma chave secreta para a sessão

# Configurações de segurança para cookies de sessão
app.config['SESSION_COOKIE_HTTPONLY'] = True  # Protege contra XSS
app.config['SESSION_COOKIE_SECURE'] = True  # Só envia o cookie via HTTPS

rotas_publicas=['static','blueprint_cool.index','blueprint_cool.login']
rotas_privadas=['static','blueprint_cool.livros', 'blueprint_cool.logout', 'blueprint_cool.limpar', 'blueprint_cool.adicionar_livro']
#Evita que pessoas sem um usuario acesse a pagina de livros
@app.before_request
def verificaSessao():
    
    if request.endpoint not in rotas_privadas and request.endpoint not in rotas_publicas:
        abort(404)
    if request.endpoint in rotas_publicas:
        return
    
    elif "usuario" not in session:
        print("Bloqueado")
        abort(403)

    return

app.register_blueprint(pagina)

#leva para uma pagina de erro caso alguem digite errado a url
@app.errorhandler(404)
def page_not_found(e):
    flash('A url da pagina parece estar incorreta, tente voltar para a pagina de login','warning')
    return render_template('404.html'), 404

#leva para uma pagina de erro caso alguem não tenha uma sessão de usuario
@app.errorhandler(403)
def acesso_negado(e):
    flash('Voce parece não estar logado tente voltar para a pagina de login','warning')
    return render_template('403.html'), 403


# Manipulador de erros genéricos
@app.errorhandler(Exception)
def handle_generic_error(e):
    return render_template('erro.html', message=str(e)), 500

if __name__ == "__main__":
    app.run(debug=True)
