class Personagem:
    def __init__(self, id, nome, idade, formacao, emprego):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.formacao = formacao
        self.emprego = emprego

personagens = []

def add_personagem(nome, idade, formacao, emprego):
    id = len(personagens) + 1
    novo_personagem = Personagem(id, nome, idade, formacao, emprego)
    personagens.append(novo_personagem)

def edit_personagem(id, nome, idade, formacao, emprego):
    for personagem in personagens:
        if personagem.id == id:
            personagem.nome = nome
            personagem.idade = idade
            personagem.formacao = formacao
            personagem.emprego = emprego
            return

def delete_personagem(id):
    for personagem in personagens:
        if personagem.id == id:
            personagens.remove(personagem)
            return

# Exemplo de uso
add_personagem("Sheldon", 27, "Doutorado", "Físico Teórico")
add_personagem("Penny", 25, "Ensino Médio", "Garçonete")
