import time
from time import sleep

n1 = int(float(input('Digite o primeiro número: ')))
n2 = int(float(input('Digite o segundo número: ')))
op = 0
while op != 5:
        print (f'''Oque deseja fazer com os números {n1} e {n2}?
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
        op = int(input('Escolha uma opção: '))
        if op == 1:
            print('\033[034m=-=\033[034m\033[0m' * 14)
            print (f'Resultado da soma: {n1} + {n2} = {n1 + n2}')
            print('\033[034m=-=\033[034m\033[0m' * 14)
            sleep(3)
        if op == 2:
            print('\033[034m=-=\033[034m\033[0m' * 14)
            print(f'Resultado da multiplicação: {n1} x {n2} = {n1 * n2}')
            print('\033[034m=-=\033[034m\033[0m' * 14)
            sleep(3)
        if op == 3:
            print('\033[034m=-=\033[034m\033[0m' * 14)
            print(f'O maior número entre {n1} e {n2} é {max(n1,n2)}')
            print('\033[034m=-=\033[034m\033[0m' * 14)
            sleep(3)
        if op == 3 and n1 == n2:
            print ('Os dois números são iguais, tente outra opção ou se desejar pode digitar [4]')
            sleep(3)
        if op == 4:
            print('\033[034m=-=\033[034m\033[0m' * 14)
            n1 = int(float(input('Digite o primeiro número: ')))
            n2 = int(float(input('Digite o segundo número: ')))
            print('\033[034m=-=\033[034m\033[0m' * 14)
        if op == 5:
            print ('Obrigada por jogar!')
        if op not in [1, 2, 3, 4, 5]:
            print('\033[031m=-=\033[031m\033[0m' * 30)
            print ('\033[031mNão entendi, vamos tentar novamente e dessa vez selecione uma opção correta entre 1 e 5.\033[031m\033[0m')
            print('\033[031m=-=\033[031m\033[0m' * 30)