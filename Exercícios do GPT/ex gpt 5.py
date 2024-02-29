class LivroBiblioteca:
    def __init__(self,titulo,autor,ano,disponivel):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = bool(disponivel)

    def emprestar(self):
        self.disponivel = False
        print(f'O livro "{self.titulo}" foi emprestado.')

    def devolver(self):
        self.disponivel = True
        print(f'O livro "{self.titulo}" foi devolvido.')

livro= LivroBiblioteca('Nilto no país das maravilhas', 'Nilto', '2006', False)
livro.emprestar()
livro.devolver()

