# Desenvolva um aplicativo que mostre na tela o resultado da expressão 500 + 450 + 400 + 350 + 300 + ... + 50 + 0
#EX: FOR
#soma = 0
#print ('A soma entre os números: ')
#for n in range (500, 0, -50):
#    print (f'{n}', end = ' + ')
#    soma += n
#print ('FIM')
#print (f'É igual a: {soma}')

#EX:  WHILE
soma = 0
cont = 500
print ('O resultado da soma dos números: ')
while cont >= 0:
    print (f'{cont}', end = ' + ')
    soma += cont
    cont -= 50
print ('FIM')
print (f'É igual a: {soma}')
