

class ProgramaDeTv:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def likes(self):
        return self._likes

    @likes.setter
    def likes(self, likes):
        self._likes = likes


class Filme(ProgramaDeTv):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def retorna_cadastro_diferenciado(self):
        pass


class Serie(ProgramaDeTv):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas



vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_like()

atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_like()


filmes_e_series = [vingadores, atlanta]

for programa in filmes_e_series:
    detalhes = programa.duracao if hasattr(programa, "duracao") else programa.temporadas
    print(f'{programa.nome} - {detalhes}: {programa.likes}')