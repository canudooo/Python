class Livro:
    def __init__(self, titulo, autor, genero, preco):
       self.titulo = titulo
       self.autor = autor
       self.genero = genero
       self.preco = int(preco)

    def desconto (self, porcentagem):
        desconto = ((porcentagem/100)*(self.preco))
        preco_com_desconto = self.preco - desconto
        print(f'Seu livro, com título de {self.titulo}, do {self.autor} de genêro {self.genero} custa R${self.preco:.2f}')
        print(f'Com desconto de {porcentagem}%, ele sairá de R${self.preco},00 por:R${preco_com_desconto:.2f}')


livrofoda = Livro('Livro Foda', 'Nélson Torres', 'Terror', 100)
livrofoda.desconto(5)
print('')
livropoggers = Livro('Livro Poggers', 'Pereira Silva', 'Romance', 69)
livropoggers.desconto(20)
