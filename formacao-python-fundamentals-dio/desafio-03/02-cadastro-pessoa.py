class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir_informacoes(self):
        return f"Nome: {self.nome}, Idade: {self.idade}"


# Tratamento de entrada para evitar que o código quebre
try:
    nome = input("Digite o nome: ")
    # O int() pode gerar um ValueError se a entrada não for um número
    idade = int(input("Digite a idade: "))

    # Criamos a instância apenas se a idade for válida
    p = Pessoa(nome, idade)
    print(p.exibir_informacoes())

except ValueError:
    print("Erro: A idade deve ser um número inteiro válido! ⚠️")
