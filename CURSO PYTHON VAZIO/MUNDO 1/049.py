#Crie um programa que leia 6 números inteiros e no final mostre quantos deles são pares e quantos são ímpares.
#EX: FOR
#par = 0
#impar = 0
#for n in range (1,7):
#    nun = int(input(f'{n}° número: '))
#    if nun % 2 == 0:
#        par += 1
#    else:
#        impar += 1
#print (f'Temos {par} números pares e {impar} números impar.')

#EX: WHILE
par = impar = 0
cont = 1
while cont < 7:
    nun = int(input(f'{cont}° número: '))
    cont += 1
    if nun % 2 == 0:
        par += 1
    else:
        impar += 1
print (f'No total temos {par} números pares e {impar} números impares.')