class AnimalTerrestre:
    def __init__(self, nome, altura):
        self.nome = nome
        self.altura = altura

    def andar(self):
        print("O animal terrestre andou")

    def comer(self):
        print("O animal terrestre comeu")


class AnimalAquatico:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def nadar(self):
        print("O animal aquatico nadou")

    def comer(self):
        print("O animal aquatico comeu")


class Anfibio(AnimalAquatico, AnimalTerrestre):
    def __init__(self, nome, peso, altura, especie):
        AnimalTerrestre.__init__(self, nome, altura)        # chamada explicita
        AnimalAquatico.__init__(self, nome, especie)        # chamada explicita
        self.peso = peso

    def comer(self):
        AnimalTerrestre.comer(self)


anfibio = Anfibio("nome", 100, 200, "especie")
anfibio.andar()
anfibio.comer()
anfibio.nadar()
