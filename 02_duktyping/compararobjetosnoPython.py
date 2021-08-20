"""
Tenho um sistema em Python que armazena os filmes
que eu tenho em uma lista, para organização,
com uma função que pega todos os filmes e
retorna uma lista com eles:
"""


class Filme:
    def __init__(self, titulo, diretor):
        self.titulo = titulo
        self.diretor = diretor

    def __str__(self):
        return self.titulo + " - " + self.diretor

    def __eq__(self, outro_filme):
        return self.titulo == outro_filme.titulo  # AquiIIIIIII


filme_1 = Filme("A Teoria de Tudo", "James Marsh")
filme_2 = Filme("La La Land ", "Damien Chazelle")
filme_3 = Filme("O Poderoso Chefão", "Francis Ford Coppola")
meus_filmes = [filme_1, filme_2, filme_3]
"""
for filme in meus_filmes:
    print(filme)
"""


def tenho_o_filme(filme_procurado):
    for filme in meus_filmes:
        # AQUIIIIIIII essá finção só funciona
        # se tiver aquela função na linha 18
        if filme_procurado == filme:

            return True
    return False


filme_procurado = Filme("A Teoria de Tudo", "James Marsh")

if tenho_o_filme(filme_procurado):
    print("Tenho o filme!")
else:
    print("Não tenho :(")
