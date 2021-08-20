class Pessoa:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def exibir_dados(self):
        print("--------------------")
        print("Nome:", self.nome)
        print("Email:", self.email)
        print("Telefone:", self.telefone)


# Aluno herda da classe Pessoa
class Aluno(Pessoa):
    def __init__(self, nome, email, telefone, ra, turma):
        super().__init__(nome, email, telefone)      # construtor da classe mãe
        self.ra = ra
        self.turma = turma

    def exibir_dados(self):
        super().exibir_dados()                   # chama o método da classe mãe
        print("RA: ", self.ra)
        print("Turma:", self.turma)


# Professor herda da classe Pessoa
class Professor(Pessoa):
    def __init__(self, nome, email, telefone, salario):
        super().__init__(nome, email, telefone)      # construtor da classe mãe
        self.salario = salario

    def exibir_dados(self):
        super().exibir_dados()                   # chama o método da classe mãe
        print("Salario:", self.salario)


aluno1 = Aluno("Pedro", "pedro@email.com", "11-987777733", 1234, "ADS2D")
aluno1.exibir_dados()

professor1 = Professor("João", "joao@email.com", "11-988887777", 2000.0)
professor1.exibir_dados()
