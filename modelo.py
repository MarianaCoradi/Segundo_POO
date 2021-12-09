

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

    #trocando a função imprime por uma função dunder, que é mais pythônico.
    #Esse método especial necessita retornar um valor como strig, que represente o objeto desejado
    def __str__(self):
       return f'{self.nome} - {self.ano} -  {self._likes}Likes'


class Filme(ProgramaDeTv):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    # sobrescrevendo o método __str__ da classe mãe para adicionar atributos específicos da classe filha
    def __str__(self):
        return f'Nome: {self.nome} - Ano: {self.ano} - Duracao: {self.duracao} minutos: {self._likes} Likes'


class Serie(ProgramaDeTv):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    #sobrescrevendo o método __str__ da classe mãe para adicionar atributos específicos da classe filha
    def __str__(self):
        return f'Nome: {self.nome} - Ano: {self.ano} - Temporadas: {self.temporadas} : {self._likes} Likes'


#Retirando a herança de list da classe Palylist, pois eu não sei todos os métodos da classe built-in de list eu quero apenas algumas características de list
#Essa herança criou complexidades desnecessárias
class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('Todo mundo em pânico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)

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

filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist('Playlist de fim de semana', filmes_e_series)

#Algumas vantagens de Playlist ter herdado a superclasse list: Posso iterar, posso saber o seu tanho a partir do len() e posso ver ser algum objeto está contido nela
print(f'Tamnho da playlist: {len(playlist_fim_de_semana.listagem)}')

for programa in playlist_fim_de_semana.listagem: #removi o. programs, pois meu objeto playlist_fim_de_semana agora é iterável, agora o playlist pode ser usado como list
    print(programa)

#print(f'Está ou não na minha playlist? {demolidor in playlist_fim_de_semana}')
