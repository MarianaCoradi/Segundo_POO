

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


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    #Usando o duck typing, o objeto irá se comportar como uma sequência iterável
    def __getitem__(self, item): #Este método define algo que é iterável
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self): #faz com que quando função len() é chamada externamente, ele retorne o tamanho
        return len(self._programas)

    def __add__(self,outro_programa): #resignificando o sinal de adição, sobrescrevendo o método __add__
        return self._programas.append(outro_programa)

    def __sub__(self,outro_programa): #resignificando o sinal de subtração, sobrescrevendo o método __sub__
        return self._programas.remove(outro_programa)


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


print(f'Tamanho da playlist: {len(playlist_fim_de_semana)}') # --> Agora com o uso do __len__ podemos usar a função leng9) que ela irá retornar o tamanho da lista do nosso objeto
print("-------")
for programa in playlist_fim_de_semana: #voltei com a funcionalidade de playlist_fim_de_semana ser iterável usando __getitem__
    print(programa)
print("-------")
print(f'Está ou não na minha playlist? {demolidor in playlist_fim_de_semana}')
print(playlist_fim_de_semana[0])

rei_leao = Filme('rei leão', 1999, 120)
playlist_fim_de_semana + rei_leao #resignificando o sinal de adição, sobrescrevendo o método __add__
print("-------")
for programa in playlist_fim_de_semana:
    print(programa)

print("-------")
playlist_fim_de_semana - atlanta #resignificando o sinal de subtração, sobrescrevendo o método __sub__
for programa in playlist_fim_de_semana:
    print(programa)