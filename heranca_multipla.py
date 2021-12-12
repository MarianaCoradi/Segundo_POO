
class Funcionario:
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

class Junior(Alura): #Funcionário Junior só tem acesso aos métodos da Alura
    pass

class Pleno(Alura, Caelum): #Funcionário Pleno tem acesso tanto as ações da Alura quanto da Caelum --> Exemplo de herança múltipla
    pass

jose = Junior()
jose.busca_perguntas_sem_resposta()

luan = Pleno()
luan.busca_perguntas_sem_resposta()
luan.busca_cursos_do_mes()
luan.registra_horas(50)

luan.mostrar_tarefas() #Nessa linha de código o luan que teria acesso ao mostrar_tarefas de Alura e Caelum , apenas printa o do Alura!!!!