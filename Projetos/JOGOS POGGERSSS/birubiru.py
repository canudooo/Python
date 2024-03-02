import random

contador = 0
while True:
    contador += 1
    x = random.randint(0, 100)

    if x != 0:
        print(x)
    else:
        print('FINALMENTE O >{}<'.format(x))
        print('Rodou:{}'.format(contador))
        break