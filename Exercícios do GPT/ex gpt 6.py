class Produto():
    def __init__(self, nome, preco, estoq_old):
        self.nome = str(nome)
        self.preco = float(preco)
        self.estoq_old = int(estoq_old)

    def atualizar_preco(self, preco_new):
        self.preco = preco_new
        print(f'O preço de {self.nome} foi atualizado: Preço antigo: R${self.preco:.2f} --- Preço atualizado: {preco_new:.2f}')

    def adicionar_estoque (self, adc_estoq):
        estoq_new = self.estoq_old + adc_estoq
        print(f'Produto: {self.nome}. Quantidade antiga de produtos: {self.estoq_old}. Comprados:{adc_estoq}. Quantidade de produtos em estoque agora: {estoq_new}')

    def remover_estoq (self, remov_estoq):
        if self.estoq_old > remov_estoq:
           estoq_new = self.estoq_old - remov_estoq
           print(f'Produto: {self.nome}. Quantidade antiga de produtos: {self.estoq_old}. Vendidos:{remov_estoq}. Quantidade de produtos em estoque agora: {estoq_new}')
        else:
            print(f'Não há {remov_estoq} {self.nome} suficientes em estoque.')


escova_dent = Produto('Escova de dentes', 10, 100)

escova_dent.atualizar_preco(9.99)
print('')
escova_dent.remover_estoq(101)
print('')
escova_dent.adicionar_estoque(15)