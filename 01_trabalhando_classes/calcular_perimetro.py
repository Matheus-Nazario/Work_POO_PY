'''
Classe Triangulo
Atributos:
-> lado_a
-> lado_b
-> lado_c

Métodos:
-> calcular_perimetro

Solicitar dados ao usuario para criar um objeto
'''


class Triangulo:
    def __init__(self, lado_a, lado_b, lado_c):
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c

    def calcular_perimetro(self):
        return self.lado_a + self.lado_b + self.lado_c


a = float(input("Medida do primeiro lado: "))
b = float(input("Medida do segundo lado: "))
c = float(input("Medida do terceiro lado: "))

# criar um objeto (instanciar)
triangulo = Triangulo(a, b, c)
print(triangulo.calcular_perimetro())
