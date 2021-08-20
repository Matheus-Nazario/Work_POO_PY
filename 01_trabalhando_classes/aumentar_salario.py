'''
Classe Funcionario:
Atributos:
- nome
- salario
Métodos:
- aumentar_salario: recebe percentual e altera o salário
'''


class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def aumentar_salario(self, percentual):
        self.salario = (self.salario * percentual / 100) + self.salario


n = input("Nome: ")
s = float(input("Salario: "))
funcionario1 = Funcionario(n, s)
p = float(input("Percentual de aumento: "))
funcionario1.aumentar_salario(p)

print("O nome do funcioario: ", funcionario1.nome)
print("O salario do funcionario é: ", funcionario1.salario)
