'''
|------------|         |---------------------|        |-------------|
| Produto    |         | Carrinho            |        | Cliente     |
|------------|         |---------------------|        |-------------|
| descricao  |0..*    1| cliente             |1      1| nome        |
| valor      |---------| produtos            |--------|-------------|
|------------|         |---------------------|        |             |
|            |         | adicionar_produto() |        |-------------|
|------------|         | listar_produtos()   |
                       | calcular_total()    |
                       |---------------------|
'''


class Cliente:
    def __init__(self, nome):
        self.nome = nome


class Produto:
    def __init__(self, descricao, valor):
        self.descricao = descricao
        self.valor = valor


class Carrinho:
    def __init__(self, cliente):
        self.cliente = cliente      # armamzena um objeto da classe Cliente
        self.produtos = []    # armazena uma lista de objetos da classe Produto

    def adicionar_produto(self, prod):
        self.produtos.append(prod)

    def listar_produtos(self):
        for prod in self.produtos:
            print(prod.descricao, prod.valor)

    def calcular_total(self):
        soma = 0
        for prod in self.produtos:
            soma += prod.valor
        return soma


# cria objetos Produto
prod1 = Produto("HD Externo", 100.0)
prod2 = Produto("Pen Drive", 20.0)
prod3 = Produto("Teclado", 45.0)

# cria objeto Cliente
cliente1 = Cliente("Paulo")

# cria objeto Carrinho de Compra
carrinho1 = Carrinho(cliente1)

# insere produtos no carrinho
carrinho1.adicionar_produto(prod1)
carrinho1.adicionar_produto(prod2)
carrinho1.adicionar_produto(prod2)
carrinho1.adicionar_produto(prod3)

# lista produtos do carrinho
carrinho1.listar_produtos()

# exibe total da compra
print('Total: ', carrinho1.calcular_total())
