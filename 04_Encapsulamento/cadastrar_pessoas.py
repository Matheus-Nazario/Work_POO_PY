class Pessoa:
    def __init__(self, nome, idade, cpf, rg):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf        # Atributo Privado
        self.__rg = rg          # Atributo Privado

    # Métodos Get
    def get_cpf(self):
        return self.__cpf

    def get_rg(self):
        return self.__rg

    # Métodos Set
    def set_cpf(self, cpf):
        if len(cpf) == 11:      # Valida CPF
            self.__cpf = cpf
        else:
            print("Valor Inválido")

    def set_rg(self, rg):
        self.__rg = rg


pessoa1 = Pessoa("João", 25, "11111111111", "3333333")
pessoa1.idade = 26                      # Altera a idade
pessoa1.set_cpf("22222222222")          # Altera cpf

print("Nome: ", pessoa1.nome)
print("CPF:", pessoa1.get_cpf())        # Exibe CPF
