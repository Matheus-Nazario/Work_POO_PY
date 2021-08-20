class Veiculo:
    def __init__(self, marca, modelo, placa):
        self.marca = marca
        self.modelo = modelo
        self.placa = placa

    def exibir(self):
        print("---------------------")
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Placa:", self.placa)


# Carro herda da classe Veiculo
class Carro(Veiculo):
    def __init__(self, marca, modelo, placa, portas):
        super().__init__(marca, modelo, placa)  # construtor da classe mãe
        self.portas = portas  # atributo especifico do Carro

    def exibir(self):
        super().exibir()  # chama o método da classe mãe
        print("Portas:", self.portas)


# Moto herda da classe Veiculo
class Moto(Veiculo):
    def __init__(self, marca, modelo, placa, partida_eletrica):
        super().__init__(marca, modelo, placa)  # construtor da classe mãe
        self.partida_eletrica = partida_eletrica  # atributo especifico da Moto

    def exibir(self):
        super().exibir()  # chama o método da classe mãe
        print("Partida Elétrica:", self.partida_eletrica)


# cria objeto Carro
carro1 = Carro("Ford", "Ka", "AAA-1234", 4)
carro1.exibir()

# cria um objeto Moto
moto1 = Moto("Honda", "Biz", "BBB-5678", True)
moto1.exibir()
