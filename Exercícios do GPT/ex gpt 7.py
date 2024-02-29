class Aluno:
    def __init__(self, nome, matricula, notas):
        self.nome = nome
        self.matricula = matricula
        self.notas = notas
        self.media = 0

    def adicionar_nota(self, nota):
        if 0<= nota <= 10:
           self.notas.append(nota)
           print(f'As notas de {self.nome} foram:{self.notas}')
        else:
            print('A nota precisa estar no intervalo de 0 a 10')

    def calcular_media(self):
        if self.notas:
           soma = 0
           for x in self.notas:
               soma += x
           self.media = (soma/len(self.notas))
           print(f'A média de {self.nome} foi {self.media:.2f}')
        else:
            print('O aluno não possui notas para calcular a média.')

    def verificar_aprovação(self):
        if self.media:
           if (self.media >= 7):
               verificacao = True
           else:
               verificacao = False
           print(f'O aluno passou? {verificacao}')
        else:
            print('O aluno não possui notas e nem média.')


Vinicius= Aluno('Vinicius', 'SP31164844',[10,10,9,8,7])

Vinicius.adicionar_nota(5)
Vinicius.calcular_media()
Vinicius.verificar_aprovação()

#esse foi poggers de fazer