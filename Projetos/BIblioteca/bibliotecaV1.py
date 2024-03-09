import time

prazo = 21
current_time = time.localtime()
ano = current_time.tm_year
mes = current_time.tm_mon
devolucao_dia = current_time.tm_mday + prazo

if devolucao_dia > 30:
    mes += 1
    devolucao_dia = devolucao_dia - prazo

if mes > 12:
    ano += 1



class Funcionario():
    def __init__(self, cpf: str, nome: str, endereco: str, telefone: int, email: str):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.email = email

    def infofunc(self):
        print(f'Cpf:{self.cpf}\n'
              f'Nome:{self.nome}\n'
              f'Endereço:{self.endereco}\n'
              f'Telefone:{self.telefone}\n'
              f'Email:{self.email}')


class Gerente():
    def __init__(self, nome_g: str, funcionarios: list = None) -> None:
        self.nome_g = nome_g
        if funcionarios is None:
            self.funcionarios = []
        else:
            self.funcionarios = funcionarios

    def addfuncionario(self, funcionario):
        self.funcionarios.append(funcionario)
        print(f'Lista de funcionários atualizada:{self.funcionarios}')

    def removefuncionario(self, funcionario):
        if funcionario in self.funcionarios:
            self.funcionarios.remove(funcionario)
            print(f'Lista de funcionários atualizada:{self.funcionarios}')
        else:
            print(f'FUncionário {funcionario} não encontrado')

    def infogerente(self):
        print(f'Lista de funcionários do gerente {self.nome_g}:{self.funcionarios}')



class Biblioteca():
    def __init__(self, biblio: list = None) -> None:
        self.emprestados = []
        if biblio is None:
            self.biblio= []
        else:
            self.biblio = biblio


    def devolver(self, livro, tempo):
        if tempo > 21:
            print(f'Tempo limite de devolução de 21 dias excedido, devido a esse motivo você será multado em R${tempo/2:.2f}.') #formula: qntidade de dias dividido por 2
        else:
            print("Livro devolvido dentro do periodo de devolução correto. Parabéns!")
        if livro in self.emprestados:
            self.biblio.append(livro)
            self.emprestados.remove(livro)
            print(f'"{livro}" devolvido com sucesso!\n'
                  f'Biblioteca atualizada:{self.biblio}')
        else:
            print(f'O livro "{livro}" não está atualmente emprestado, impossível devolver.')


    def emprestar(self, livro):
        if livro in self.biblio:
            if livro not in self.emprestados:
                self.biblio.remove(livro)
                self.emprestados.append(livro)
                print(f"{livro} emprestado com sucesso!\n"
                      f"Você deverá devolve-lo até o dia {devolucao_dia}/{mes}/{ano}\n"
                      f'Biblioteca atualizada:{self.biblio}')
            else:
                print("Livro ja foi emprestado.")
        else:
            print(f'O livro "{livro}" não está disponível na biblioteca.')

    def infobiblio(self):
        print(self.catalogo)


roberio = Funcionario('12', 'Roberio', 'Rua dos piroquios', 116969696, 'piupiugames@gmail.com')
roberio.infofunc()

nelson = Gerente('Nelson', ['José', 'João', 'Maria'])
nelson.infogerente()




