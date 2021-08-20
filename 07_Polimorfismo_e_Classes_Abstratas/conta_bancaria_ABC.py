from abc import ABC, abstractmethod


class Conta(ABC):                           # Classe Abstrata
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular
        self.saldo = 0

    def consultar_saldo(self):
        print("Saldo: ", self.saldo)

    @abstractmethod
    def depositar(self, valor):             # Método abstrato
        pass

    @abstractmethod
    def sacar(self, valor):
        pass


class ContaEspecial(Conta):
    def __init__(self, numero, titular, limite):
        super().__init__(numero, titular)
        self.limite = limite

    def sacar(self, valor):                         # polimorfismo de inclusão
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
        else:
            print("Saldo + Limite da conta especial é insuficiente")

    def depositar(self, valor):
        self.saldo += valor


class Poupanca(Conta):
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo da poupança é insuficiente")

    def depositar(self, valor):
        self.saldo += valor


conta_especial = ContaEspecial(4567, "João", 500)
conta_especial.depositar(300)
conta_especial.sacar(500)
conta_especial.consultar_saldo()

poupanca = Poupanca(5678, "Maria")
poupanca.depositar(100)
poupanca.sacar(300)
poupanca.consultar_saldo()
