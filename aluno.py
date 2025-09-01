class Aluno:
    def __init__(self, nome, turma, altura, peso):
        self.nome = nome
        self.turma = turma
        self.altura = altura
        self.peso = peso
        
    def alimentar(self, comida):
        print(f"{self.nome} está comendo {comida}.")
        
        
    def assistir_aula(self, disciplina):
        print(f"{self.nome} está assistindo à aula de {disciplina}.")