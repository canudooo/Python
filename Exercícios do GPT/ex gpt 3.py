class Estudante:
    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso

    def apresentar(self):
        print(f'Olá, meu nome é {self.nome}, tenho {self.idade} anos e estou cursando {self.curso}')

    def gosto(self, comida, bebida, hooby):
        print(f'Gosto de comer {comida}, beber {bebida} e fazer/praticar {hooby}')


carlos = Estudante('Carlos', 14, 'DS')
carlos.apresentar()
carlos.gosto('carne', 'suco de laranja','basquete')
print('')

roberio = Estudante('Robério', 17, 'Mecânica')
roberio.apresentar()
roberio.gosto('macarrão','coca', 'vôlei')
