"""
Considere o sistema de uma loja virtual e implemente as classes Produto,
Item e ItemDesconto.

A classe Produto possui os atributos codigo, descricao e preco.
A classe Item possui os atributos produto e quantidade.
A classe ItemDesconto deve herdar da classe Item.

A classe Item deve implementar o método calcular_preco, que retorna como valor
o resultado da multiplicação do preço do produto pela quantidade de itens.
A classe ItemDesconto deve sobrescrever o método calcular_preco e aplicar um
desconto de 20% no preço total calculado.
"""


# --------------------- IMPLEMENTE SEU CÓDIGO AQUI --------------------------
class Produto:
    def __init__(self, codigo, descricao, preco):
        self.codigo = codigo
        self.descricao = descricao
        self.preco = preco


class Item:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

    def calcular_preco(self):
        valor = self.quantidade * self.produto.preco
        return valor


class ItemDesconto(Item):
    def calcular_preco(self):
        valor = self.quantidade * self.produto.preco
        valor = valor - (valor * 0.20)
        return valor


# -------------- PROGRAMA PRINCIPAL (não deve ser alterado) -----------------

produto1 = Produto(1, "Produto 1", 30.0)
produto2 = Produto(2, "Produto 2", 50.0)

item1 = Item(produto1, 5)
item2 = ItemDesconto(produto1, 5)
item3 = ItemDesconto(produto2, 10)

print("Total:", item1.calcular_preco())  # Total: 150.0
print("Total:", item2.calcular_preco())  # Total: 120.0
print("Total:", item3.calcular_preco())  # Total: 400.0
