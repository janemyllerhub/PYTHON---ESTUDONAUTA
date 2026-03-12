# Desenvolva um programa usando a estrutura “para” que mostre na tela a seguinte contagem:
#0 5 10 15 20 25 30 35 40 Acabou!
cont = 0
while cont < 41:
    print (f'{cont}', end = '... ' if cont < 40 else ' ')
    cont += 5
