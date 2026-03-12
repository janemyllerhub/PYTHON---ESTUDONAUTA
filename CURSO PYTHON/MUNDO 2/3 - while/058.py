from random import randint
computer = randint(0,10)
person = 0
erro = 0
acerto = 0
print('Vou pensar em um número, você consegue adivinhar?')
while person != computer:
    person =int(input('Digite um número entre 0 e 10: '))
    if person != computer:
        erro += 1
        if person > computer:
            print ('Menos, tente novamente...')
        if person < computer:
            print ('Mais, tente novamente...')
    else:
        acerto += 1
        print('\033[034m=-=\033[034m\033[0m' * 12)
        print ('Parabéns, você acertou!')
        print (f'Número digitado pelo computador: {computer}')
        print(f'Número digitado pelo jogador: {person}')
        print('\033[034m=-=\033[034m\033[0m' * 12)
print (f'\033[034mPLACAR DE ERROS\033[034m\033[0m')
print (f'\033[034m[{erro}]\033[034m\033[0m erros para conseguir acertar!')
print('\033[034m=-=\033[034m\033[0m' * 12)