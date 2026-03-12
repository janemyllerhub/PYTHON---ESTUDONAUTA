print('\033[034m=-=\033[034m\033[0m' * 6)
print (' SOMANDO NÚMEROS')
print('\033[034m=-=\033[034m\033[0m' * 6)
print ('''[?] Digite números para serem somados.
[0] Digite 0 para receber os resultados.''')
cont = 1
soma = 0
lis = []
while cont != 0:
    cont = int(input('Digite um número: '))
    soma += cont
    lis.append(cont) if cont != 0 else 0
print (f'O total dos números {lis} é igual a: {soma}')