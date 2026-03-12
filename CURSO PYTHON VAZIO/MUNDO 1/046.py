#Crie um programa que calcule e mostre na tela o resultado da soma entre 6 + 8 + 10 + 12 + 14 + ... + 98 + 100.
#EX: FOR
#soma = 6
#print (f'O resultado da soma dos números: ')
#for n in range (6,101,2):
#    print (f'{n}', end = ' + ')
#    soma += n
#print ('FIM')
#print (f'É igual a: {soma}')

#EX: WHILE
soma = 6
cont = 6
print (f'O resultado da soma entre os números: ')
while cont <= 100:
    print (f'{cont}', end = ' + ')
    soma += cont
    cont += 2
print ('FIM')
print (f'É igual a {soma}')
