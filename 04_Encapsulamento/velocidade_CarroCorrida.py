class CarroCorrida:
    def __init__(self, numero, piloto, velocidade_maxima):
        self.__numero = numero
        self.__piloto = piloto
        self.__velocidade_maxima = velocidade_maxima
        self.__velocidade_atual = 0
        self.__ligado = False

    def ligar(self):
        self.__ligado = True

    def desligar(self):
        self.__ligado = False

    def acelerar(self, velocidade):
        if self.__ligado is True:
            self.__velocidade_atual += velocidade
            # se ultrapassar a velocidade máxima, mantém a velocidade limitada na máxima
            if self.__velocidade_atual > self.__velocidade_maxima:
                self.__velocidade_atual = self.__velocidade_maxima

    def frear(self):
        self.__velocidade_atual = 0

    def get_velocidade_atual(self):
        return self.__velocidade_atual


carro = CarroCorrida(1, "Paulo", 150)
carro.acelerar(20)
print(carro.get_velocidade_atual())  # imprime 0, porque o carro esta desligado
carro.ligar()
carro.acelerar(20)
print(carro.get_velocidade_atual())  # imprime 20
carro.acelerar(80)
print(carro.get_velocidade_atual())  # imprime 100
carro.acelerar(70)
print(carro.get_velocidade_atual())  # imprime 150, não ultrapassar a vel. max.
carro.frear()
print(carro.get_velocidade_atual())  # imprime 0
