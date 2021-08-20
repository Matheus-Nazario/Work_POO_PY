'''
Classe Livro
Atributos:
- titulo
- autor
- quantidade_paginas

Criar dois objetos no programa principal
'''


class Livro:
    def __init__(self, titulo, autor, quantidade_paginas):
        self.titulo = titulo
        self.autor = autor
        self.quantidade_paginas = quantidade_paginas


livro1 = Livro("Titulo do livro 1", "João da Silva", 120)
livro2 = Livro("Poeira em alto mar", "Alan Bida", 100)
