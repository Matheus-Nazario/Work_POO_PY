# Crie a classe Motor que contém cilindrada e potencia.


class Motor:
    def __init__(self, cilindrada, potencia):
        self.cilindrada = cilindrada
        self.potencia = potencia


# Crie a classe Veiculo contendo ano de fabricação, preco e motor.
# Crie também o metodo exibir_dados para mostrar os dados do Veículo.


class Veiculo:
    def __init__(self, ano, preco, motor):
        self.ano = ano
        self.preco = preco
        self.motor = motor

    def exibir_dados(self):
        print("-------------------------")
        print("Ano: ", self.ano)
        print("Preço: ", self.preco)
        print("Cilindrada do Motor: ", self.motor.cilindrada)
        print("Potencia do Motor: ", self.motor.potencia)


# Crie a classe Caminhão, que herda da classe Veiculo e
# adiciona o atributos comprimento (em metros).
# Crie também o metodo exibir_dados para mostrar os dados do Caminhão


class Caminhao(Veiculo):
    def __init__(self, ano, preco, motor, comprimento):
        super().__init__(ano, preco, motor)
        self.comprimento = comprimento

    def exibir_dados(self):
        super().exibir_dados()
        print(f"comprimento: {self.comprimento}")


class Carro(Veiculo):
    def __init__(self, ano, preco, motor, cor, modelo):
        super().__init__(ano, preco, motor)
        self.cor = cor
        self.modelo = modelo

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Cor: {self.cor}")
        print(f"Modelo: {self.modelo}")


motor1 = Motor(1000, 500)
motor2 = Motor(8000, 900)
carro = Carro(2010, 20000, motor1, "branca", "gol")
caminhao = Caminhao(2015, 80000, motor2, 10)

carro.exibir_dados()  # imprime os valores de todos os atributos do carro
caminhao.exibir_dados()  # imprime os valores de todos os atributos do caminhão
