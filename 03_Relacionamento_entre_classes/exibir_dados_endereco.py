'''

Exemplo de Associação de Classes:

|-------------------|           |-------------------|
| Pessoa            |           | Endereco          |
|-------------------|           |-------------------|
| nome              |           | rua               |
| idade             |-----------| numero            |
| sexo              |           | complemento       |
| endereco          |           | cep               |
|-------------------|           |-------------------|
| exibir_dados()    |           | exibir_dados()    |
|-------------------|           |-------------------|

'''


class Endereco:
    def __init__(self, rua, numero, cep):
        self.rua = rua
        self.numero = numero
        self.complemento = ""
        self.cep = cep

    def exibir_dados(self):
        print("Rua: ", self.rua)
        print("Numero: ", self.numero)
        print("Complemento: ", self.complemento)
        print("CEP: ", self.cep)


class Pessoa:
    def __init__(self, nome, idade, sexo, endereco):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.endereco = endereco

    def exibir_dados(self):
        print("Nome: ", self.nome)
        print("Idade: ", self.idade)
        print("Sexo: ", self.sexo)
        print("Endereço: ")
        # Executa metodo exibir_dados da Classe Endereço
        self.endereco.exibir_dados()


# Cria objeto Endereco
end = Endereco("Av. Paulista", 100, 999999999)
# Cria objeto Pessoa e associa o objeto Endereco a ela
pessoa1 = Pessoa("Paulo", 25, "M", end)
pessoa1.exibir_dados()

# Cria outro objeto Endereco
end2 = Endereco("Av. Brasil", 198, 777777777)
# Cria outro objeto Pessoa
pessoa2 = Pessoa("Maria", 30, "F", end2)
pessoa2.exibir_dados()
