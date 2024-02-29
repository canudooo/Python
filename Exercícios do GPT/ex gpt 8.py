class Carro:
    def __init__(self, modelo, ano, km, preco):
        self.modelo = modelo
        self.ano = ano
        self.km = km
        self.preco = preco
        self.depreciacao = None

    def calcular_deprecicao(self, ano_deprec):
        anos_vivo = ano_deprec-self.ano
        self.depreciacao = (anos_vivo)*(0.05)*self.preco #0.05 de depreciaçao por ano
        print(f'O carro {self.modelo} sofreu R${self.depreciacao:.2f} de depreciação no período de {anos_vivo} anos.')

    def atualizar_preco(self):
        current_price = self.preco - self.depreciacao
        print(f'Preço atual, no ano de {self.ano} do carro {self.modelo}:R${current_price:.2f}')


evoX = Carro('MitsubisH Lancer Evo X', 2008, 0, 226000 )
evoX.calcular_deprecicao(2024)
evoX.atualizar_preco()