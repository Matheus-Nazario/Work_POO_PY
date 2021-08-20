class Funcionario:
    def __init__(self, nome, idade, salario):
        # atributos publicos
        self.nome = nome
        self.idade = idade
        # atributo privado
        self.__salario = salario

    # GET - retornar o valor de um atributo privado
    def get_salario(self):
        return self.__salario

    # SET - alterar o valor de um atributo privado
    def set_salario(self, novosalario):
        # realiza uma validação para ver se o salario é positivo
        if novosalario > 0:
            self.__salario = novosalario
        else:
            # se nao for positivo, nao altera o salario
            print('Salario inválido')


joao = Funcionario('João Silva', 25, 1500.00)
maria = Funcionario('Maria Carolina', 27, 2000.00)

print('Nome:', joao.nome)
print('Idade:', joao.idade)
print('Salario:', joao.get_salario())

joao.set_salario(2000.00)
print('Salario:', joao.get_salario())

maria.set_salario(-3000)
print('Salario:', maria.get_salario())
