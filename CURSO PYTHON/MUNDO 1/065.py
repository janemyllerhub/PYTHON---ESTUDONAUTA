#Desenvolva um programa usando a estrutura “para” que mostre na tela a seguinte contagem:
#100 90 80 70 60 50 40 30 20 10 0 Acabou!
cont = 100
while cont > -1:
    print (f'{cont}',end = '... ' if cont != 0 else '! ')
    cont -= 10