import statistics

print('\033[034m=-=\033[034m\033[0m' * 8)
print ('   ANALISE DE NÚMEROS')
print('\033[034m=-=\033[034m\033[0m' * 8)
lis = []
pro = ''
cont = 0

while pro != 'N':
        nun = int(input('Digite um número: '))
        lis.append(nun)
        pro = str(input('Deseja continuar? [S/N]: ')).upper()
        cont += 1
print (f'A média dos {cont:.2f} valores digitados é igual a: {statistics.mean(lis)}')
print (f'O maior número digitado foi {max(lis)} e o menor número digitado foi {min(lis)}')


