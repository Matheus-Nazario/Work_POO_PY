"""
No Python, não é preciso herdar de uma classe específica pra
ter polimorfismo. O que é importante no Python é: se você
quer um iterável, devo se preocupar com o que um iterável deve fazer.
O nome dessa característica é duck typing.
3) Será que dá para alterar a classe de outra
forma para suportar também o len, ao invés de ter que acessar o
método/property tamanho? Sim! Faça o seguinte:
"""


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)


"""
Desta forma, você consegue chamar len(minha_playlist),
já que Playlist implementa __len__. Isso torna a Playlist
um Sized (alguém que implementa __len__).
Observação: Você não precisa mais dos métodos/propriedades
listagem e tamanho, então pode apagar :)
"""
