from abc import ABC, abstractmethod

# Exemplo de interface. Em python, uma interface é uma classe abstrata que
# possui apenas métodos abstratos.pass

# As classes herdeiras serão obrigadas a implementar os métodos abstratos.


class Conta(ABC):
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular
        self.saldo = 0

    @abstractmethod
    def depositar(self, valor):
        pass

    @abstractmethod
    def sacar(self, valor):
        pass

    @abstractmethod
    def consultar_saldo(self):
        pass
