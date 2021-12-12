
class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def registra_horas(self, horas):
        print(f'Horas registradas...{horas} horas')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')

class Caelum(Funcionario):
    def mostrar_tarefas(self):#sobrescrevendo o método mostrar_tarefas da classe mãe Funcionario
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')

class Alura(Funcionario):
    def mostrar_tarefas(self): #sobrescrevendo o método mostrar_tarefas da classe mãe Funcionario
        print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')

class Hipster: #Exemplo de MIXINS
    def __str__(self):
        return f'Hipster, {self.nome}' # Não tem o inicializador de nome, pois eu quero q a classe q for herdar hister ja possua esse  atributo

class Junior(Alura): #Funcionário Junior só tem acesso aos métodos da Alura
    pass

class Pleno(Alura, Caelum): #Funcionário Pleno tem acesso tanto as ações da Alura quanto da Caelum
    pass

class Senior(Alura, Caelum, Hipster): #Funcionário Senior tem acesso tanto as ações da Alura quanto da Caelum e de Hipster(esse último que retorna uma string do nome do funionário para o print)
    pass


jose = Junior('José')
jose.busca_perguntas_sem_resposta()

luan = Pleno('Luan')
luan.busca_perguntas_sem_resposta()
luan.busca_cursos_do_mes()
luan.registra_horas(50)
luan.mostrar_tarefas()


pedrin = Senior('Pedro')
print(pedrin)
