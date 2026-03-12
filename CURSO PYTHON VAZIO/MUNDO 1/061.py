# Crie um programa que mostre na tela a seguinte contagem, usando a estrutura “faça enquanto”
#0 3 6 9 12 15 18 21 24 27 30 Acabou!
cont = 0
while cont < 31:
    print (f'{cont}',end = '... ' if cont < 30 else ' ')
    cont += 3
