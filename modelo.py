

class ProgramaDeTv:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    #métodos em comum que todas as classes filhas herdarão
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

    #criando um método genérico de imprimir os atributos em comum das classes filhas
    def imprime(self):
        print(f'{self.nome} - {self.ano} -  {self._likes}Likes')


class Filme(ProgramaDeTv):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    # sobrescrevendo o método imprime da classe mãe para adicionar atributos específicos da classe filha
    def imprime(self):
        print(f'Nome: {self.nome} - Ano: {self.ano} - Duracao: {self.duracao} minutos: {self._likes} Likes')


class Serie(ProgramaDeTv):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    #sobrescrevendo o método imprime da classe mãe para adicionar atributos específicos da classe filha
    def imprime(self):
        print(f'Nome: {self.nome} - Ano: {self.ano} - Temporadas: {self.temporadas} : {self._likes} Likes')

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_like()

atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_like()
atlanta.dar_like()

filmes_e_series = [vingadores, atlanta]

for programa in filmes_e_series:
    programa.imprime() #chamará o método imprime pertecente a cada classe daquele objeto dentro da lista, quando for filme imprimirá o imprime() do filme, etc
    #polimorfismo