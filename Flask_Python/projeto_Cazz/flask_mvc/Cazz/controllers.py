from models import tarefas, addTarefa, completarTarefa
from flask import Blueprint, render_template, request, redirect, url_for

tarefa_controller = Blueprint("tarefa", __name__)

@tarefa_controller.route("/")
def index():
    return render_template('index.html', tarefas=tarefas)

@tarefa_controller.route('/add', methods=['POST'])
def add():
    descricao = request.form['descricao']
    addTarefa(descricao)
    return redirect(url_for('tarefa.index'))

@tarefa_controller.route('/complete/<int:tarefa_id>', methods=['POST'])
def complete(tarefa_id):
    completarTarefa(tarefa_id)
    return redirect(url_for('tarefa.index'))
