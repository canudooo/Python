
print("Hello Word!")

""""
QUESTÃO:
 Escreva uma função em Python chamada 'soma_sem_multiplos' que receba uma lista de
 números inteiros e retorne a soma dos elementos que não são divisíveis por 3 ou 5.
"""

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def soma_sem_multiplos(lista):
  soma = 0
  for elemento in lista:
    if (elemento % 3 != 0) and (elemento % 5 != 0):
       soma += elemento
  return soma

resultado = soma_sem_multiplos(lista)
print(resultado)

