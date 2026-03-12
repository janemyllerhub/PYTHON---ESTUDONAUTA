#Desenvolva um programa que faça o sorteio de 20 números entre 0 e 10 e mostre na tela:
#a) Quais foram os números sorteados
#b) Quantos números estão acima de 5
#c) Quantos números são divisíveis por 3
#EX FOR:
#import random
#from random import randint
#cinco = tres = 0
#print ('Os 20 números sorteados foram:')
#for n in range (1, 21):
#    nun = randint(0,10)
#    print (f'{nun}', end = ' - ')
#    if nun > 5:
#        cinco += 1
#    if nun % 3 == 0:
#        tres += 1
#print ('FIM')
#print (f'Temos {cinco} números maiores que 5 e {tres} números divisiveis por 3.')

#EX: WHILE
from random import randint
cont = cinco = tres = 0
while cont < 21:
    sortidos = randint(0,10)
    print (f'{sortidos}', end = ' - ')
    cont +=1
    if sortidos > 5:
        cinco += 1
    if sortidos % 3 == 0:
        tres += 1
print ('FIM')
print (f'Temos {cinco} números maiores que cinco e {tres} números divisiveis por 3.')