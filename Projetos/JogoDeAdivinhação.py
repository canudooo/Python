import random

random_number = int(random.randint(0, 10))
chances = 3

for tentativa in range(0,3,1):
    chute = (int(input('\nAcho que é:')))
    chances-=1
    if chute != random_number and chances!=0:
        print('Você errou, mas ainda tem mais {} chances'.format(chances))
    if chute == random_number:
        print('Você acertou!!!')
        print('O número era de fato o {}, parabéns!!!'.format(random_number))
        break
    if (chances == 0):
        print('Suas chances acabaram!')
        print('\nO número era:', random_number)
        break