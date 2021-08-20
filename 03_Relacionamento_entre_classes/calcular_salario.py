class Emprego:
    def __init__(self, cargo, area, salario, bonus):
        self.cargo = cargo
        self.area = area
        self.salario = salario
        self.bonus = bonus


class Pessoa:
    def __init__(self, nome, fone, email, emprego):
        self.nome = nome
        self.fone = fone
        self.email = email
        self.emprego = emprego
        self.dependentes = []

    def calcular_salario(self):
        quantidade = len(self.dependentes)
        porcentagem = quantidade * self.emprego.bonus
        salario = self.emprego.salario + (
            self.emprego.salario * porcentagem / 100
        )
        return salario


emprego = Emprego("Programador", "TI", 2000, 5)
pessoa1 = Pessoa("Paulo", "11-99999999", "paulo@email.com", emprego)

dep1 = Pessoa("Maria", "", "", None)
dep2 = Pessoa("Joao", "", "", None)

pessoa1.dependentes.append(dep1)

print("Salario: ", pessoa1.calcular_salario())
