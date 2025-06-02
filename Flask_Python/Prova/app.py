# Prova Caíque França e Bruno Timóteo

from flask import Flask, render_template, request, redirect, url_for
from model import add_personagem, personagens, delete_personagem, edit_personagem

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', personagens=personagens)

@app.route('/', methods=['POST'])
def add():
    add_personagem(request.form["nome"], request.form["idade"], request.form["formacao"], request.form["emprego"])
    return redirect(url_for('index'))

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    delete_personagem(id)
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['GET'])
def edit(id):
    return render_template("edicao.html", personagens=personagens, id=id)

@app.route('/edit/<int:id>', methods=['POST'])
def edicao(id):
    edit_personagem(id, request.form["nome"], request.form["idade"], request.form["formacao"], request.form["emprego"])
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
