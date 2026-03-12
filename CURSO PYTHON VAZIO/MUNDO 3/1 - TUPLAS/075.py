tupla = (int(input('Digite um número: ')),
        int(input('Digite outro número: ')),
        int(input('Digite mais um número: ')),
        int(input('Digite o último número: ')),)
pares = []
print ('Você digitou os valores: ',tupla)
print ('O valor 9 apareceu',tupla.count(9),'vezes')
for c in tupla:
        if c % 2 == 0:
                pares.append(c)
        if c == 3:
                print('O primeiro valor 3 foi digitado na posição', tupla.index(3) + 1)
print (f'Temos os valores {pares} pares digitados.')
