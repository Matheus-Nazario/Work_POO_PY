class Veiculo:
    def __init__(self, marca, modelo, rodas):
        self.marca = marca
        self.modelo = modelo
        self.rodas = rodas
        self.__velocidade = 0

    def acelerar(self, valor):
        self.__velocidade += valor

    def frear(self, valor):
        self.__velocidade -= valor

    def get_velocidade(self):
        return self.__velocidade


class Automovel(Veiculo):
    def __init__(self, marca, modelo, rodas, potencia):
        super().__init__(marca, modelo, rodas)
        self.potencia = potencia

    def imprimir_informacoes(self):
        print('-------------------------------')
        print("marca: ", self.marca)
        print("modelo: ", self.modelo)
        print("rodas: ", self.rodas)
        print("potencia: ", self.potencia)


class Bicicleta(Veiculo):
    def __init__(self, marca, modelo, rodas, marchas, bagageiro):
        super().__init__(marca, modelo, rodas)
        self.marchas = marchas
        self.bagageiro = bagageiro

    def imprimir_informacoes(self):
        print('-------------------------------')
        print("Marca:", self.marca)
        print("modelo: ", self.modelo)
        print("rodas:", self.rodas)
        print("marchas: ", self.marchas)
        print("bagageiro: ", self.bagageiro)


class Carro(Automovel):
    def __init__(self, marca, modelo, rodas, potencia, portas):
        super().__init__(marca, modelo, rodas, potencia)
        self.portas = portas

    def imprimir_informacoes(self):
        super().imprimir_informacoes()
        print("portas: ", self.portas)


class Moto(Automovel):
    def __init__(self, marca, modelo, rodas, potencia, partida_eletrica):
        super().__init__(marca, modelo, rodas, potencia)
        self.partida_eletrica = partida_eletrica

    def imprimir_informacoes(self):
        super().imprimir_informacoes()
        print("partida eletrica: ", self.partida_eletrica)


carro = Carro("Ford", "Ka", 4, 85.0, 5)
moto = Moto("Honda", "Biz", 2, 9.2, True)
bike = Bicicleta("Caloi", "Elite", 2, 18, True)

carro.acelerar(30)
carro.frear(10)
moto.acelerar(100)
moto.frear(20)
bike.acelerar(20)
bike.frear(5)

carro.imprimir_informacoes()   # imprime os todos os atributos do carro
bike.imprimir_informacoes()    # imprime os todos os atributos da bicicleta
moto.imprimir_informacoes()    # imprime os todos os atributos da moto

# testar a velocidade atual
print("Velocidade atual do Carro:", carro.get_velocidade())       # 20
print("Velocidade atual da Moto:", moto.get_velocidade())         # 80
print("Velocidade atual da Bicicleta:", bike.get_velocidade())    # 15
