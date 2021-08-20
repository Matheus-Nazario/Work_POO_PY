class Estudante:
    def __init__(self, nome, matricula, curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso


class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario


class Monitor(Estudante, Funcionario):
    def __init__(
        self, nome, matricula, curso, salario, disciplina, carga_horaria
    ):
        Estudante.__init__(self, nome, matricula, curso)
        Funcionario.__init__(self, nome, salario)
        self.__disciplina = disciplina
        self.__carga_horaria = carga_horaria

    def get_disciplina(self):
        return self.__disciplina

    def get_carga_horaria(self):
        return self.__carga_horaria

    def set_disciplina(self, disciplina):
        self.__disciplina = disciplina

    def set_carga_horaria(self, carga_horaria):
        self.__carga_horaria = carga_horaria


estudante = Estudante("Maria", 456789, "ADS")
funcionario = Funcionario("João", 2000)
monitor = Monitor("Paulo", 123456, "SI", 1000.0, "POO", 4)
print("Nome:", monitor.nome)  # Paulo
print("Matricula:", monitor.matricula)  # 123456
print("Curso:", monitor.curso)  # SI
print("Salario:", monitor.salario)  # 1000.0
print("Disciplina:", monitor.get_disciplina())  # POO
print("Carga Horaria:", monitor.get_carga_horaria())  # 4
