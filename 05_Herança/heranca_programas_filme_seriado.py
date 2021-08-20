# Quando pensamos em herança, pensamos em uma pessoa mais velha
# que vai deixar bens ou transmitir dados genéticos.
# Usaremos essa ideia para classes, pois estamos pensando em Filme e Série,
#  cujos comportamentos têm algumas semelhanças. Se tivéssemos uma
# classe mais genérica com estes mesmos comportamentos,
# as duas poderiam aproveitar os dados em comum.

# O Programa é a superclasse a classe Mãe que tem atributos
# e metodos da suas filhas (filmes e séries )
class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def imprime(self):
        print(f"Nome: {self.nome} - Ano: {self.ano}")


class Filme(Programa):
    # Na classe Filme, chamamos o super(), que por sua vez chama
    # qualquer método ou atributo da classe mãe.
    # Podemos testar isto digitando super(). e
    # observando o que o PyCharm nos sugere como autocomplete. Todos os métodos
    # ou propriedades exibidos são provenientes da classe mãe,
    # evidenciado por Programa,
    # ao lado. Podemos acessá-los direta ou indiretamente.
    def __init__(self, nome, ano, duracao):
        super().__init__(
            nome,
            ano,
        )
        self.duracao = duracao
        # Neste exemplo, sobrescrevemos o método __init__()
        # para que possamos utilizar o
        #  __init__() da classe mãe,
        # e além disto ter algo mais específico.

    # uma fora de impressão
    #    def imprime(self):
    #        a = f" Nome: {self.nome} - Anos: {self.ano}"
    #        b = f"- Duração: {self.duracao}- Likes: {self._likes}"
    #        print(a, b)
    def __str__(self):
        return (
            f"Nome {self.nome} Duração: {self.duracao}- Likes: {self._likes}"
        )


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

        #    def imprime(self):
        #        a = f" Nome: {self.nome} - Anos: {self.ano}"
        #        b = f"- Duração: {self.temporadas}- Likes: {9self._likes}"
        #        print(a, b)

    def __str__(self):
        return f"Nomes:{self.nome} - temp:{self.temporadas} - L:{self._likes}"


"""
# vamos criar uma herença d elista para a classe seja interavél
# e tenha heraça de tudo de lista
class Playlist(list):
    def __init__(self, nome, programas):
        self.nome = nome
        super().__init__(programas)
"""
# se fosse dicionário ou outro tipo sem ser buit in que não venha uma uma
# estrutura pronta pois não sabemos as restrições da mesma

# Tínhamos feito a herança de list na nossa classe Playlist,
# e com isso podemos dizer Playlist é um list,
# e que absorvemos todas as suas funcionalidades para a Playlist.
# No entanto, list é uma classe conhecida como built-in,
# embutida no Python e pronta para uso. E tivemos o benefício de
# reaproveitarmos vários códigos desta classe, mesmo não conhecendo
# todas as suas funcionalidades ou extensões. Precisamos tomar
# cuidado ao fazermos este tipo de herança!
# No código, em relação a Playlist, utilizamos o __init__() para
# fazermos a chamada usando nome e programas. Sendo assim, trata-se de
# um __init__ diferente de um inicializador de um list.
# Quando alguém for criar um objeto de Playlist,
# terá que utilizar este inicializador,
# o que será um tanto confuso, pois por ser um list, deveria receber
# apenas a listagem de itens,
# ou de repente somente um item, para começar uma lista,
# a qual possui um protocolo,
#  uma interface, distintos.
# Um ponto positivo é que estamos criando uma playlist
# mas não nos limitaremos a um
# list só - a playlist tem mais significado para o
#  nosso sistema, talvez possamos
# fazer uma busca por nome, uma filtragem para encontrar elementos
# que façam parte
# de uma categoria, como "série", por exemplo.


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    # interar como lista getItem não precisa heradar
    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)


#        self.programas = programas

#    def tamanho(self):
#        return len(self.programas)


vingadores = Filme("vingadores - guerra infinita", 2018, 160)
atlanta = Serie("atlanta", 2018, 2)
tmep = Filme("Todo mundo em pânico", 1999, 100)
demolidor = Serie("Demolidor", 2016, 2)

vingadores.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()

filmes_e_series = [vingadores, atlanta, tmep]
playlist_fim_de_semana = Playlist("fim de semana", filmes_e_series)

print(f"O Tamanho da playlist é { len(playlist_fim_de_semana) }")

for programa in playlist_fim_de_semana:
    print(programa)

# print(f"Nome: {vingadores.nome} - Likes: {vingadores.likes}")
# print(f"Nome: {atlanta.nome} - Likes: {atlanta.likes}")
print(f"lista? R: {demolidor in playlist_fim_de_semana}")

lista = [vingadores, atlanta]

"""
Aqui, vemos a vantagem de trabalharmos com heranças,
chamada de polimorfismo. Desta forma,
conseguimos percorrer uma lista qualquer e,
 sendo elas do mesmo supertipo, no caso, de Programa,
 e com uma estrutura similar, com nome e likes,
conseguimos usar o for independentemente do tipo que existe ali.

for programa in lista:
    detalhes = (
        programa.duracao
        if hasattr(programa, "duracao")
        else programa.temporadas
    )
    print(f"Nome: {programa.nome}- D: {detalhes} - Likes: {programa.likes}")
"""
"""
Na verdade, ao retirarmos a herança, tivemos uma melhoria de prática.
 Para tentar entendermos o porquê da herança ser boa ou ruim dependendo
  do seu propósito, vamos pensar nos motivos para seu uso:

Interface, quando queremos resolver questões relativas a polimorfismo;

Reuso do código, ou remoção de duplicações.

Quando estávamos herdando de uma lista, tínhamos apenas um motivo
a classe Playlist não precisa ser uma lista efetivamente, e sim ter
algumas de suas funcionalidades. Ao mesmo tempo, queríamos alguns
códigos que faziam sentido de estarem na nossa classe, como uma
solução para mensurar quantidades na lista, sem termos que implementar
ou verificar isto manualmente.

"""
