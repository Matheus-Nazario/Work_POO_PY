"""
Para fazer o mesmo no Python, é possível usar classes abstratas,
as chamadas ABC (A*bstract *Base Classes). Existem classes já
prontas que ajudam nessa ideia.
"""

from collections.abc import MutableSequence


class MinhaListinhaMutavel(MutableSequence):
    def __init__(self):
        super().__init__()

    def __len__(self):
        pass


"""
5) A classe MinhaListinhaMutavel herda de MutableSequence,
ou seja, é desejável que o Python avise que tem que
implementar todos os métodos abstratos de uma
MutableSequence. Só que parece que não funcionou.
"""
objetoValidado = MinhaListinhaMutavel()
print(objetoValidado)
