class Tarefa:
    def __init__(self, id, descricao, completo=False):
        self.id = id
        self.descricao = descricao
        self.completo = completo

tarefas = []

def addTarefa(descricao):
    id = len(tarefas) + 1
    nova_tarefa = Tarefa(id, descricao)
    tarefas.append(nova_tarefa)

def completarTarefa(tarefa_id):
    for tarefa in tarefas:
        if tarefa.id == tarefa_id:
            tarefa.completo = True

