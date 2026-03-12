continuar = 'S'
lista = []
pares = []
impares = []
while continuar == 'S':
    nun = int(input('Digite um número: '))
    lista.append(nun)
    cont = str(input('Deseja continuar [S/N]? ')).upper().strip()
    continuar = cont
    if nun % 2 == 0:
        pares.append(nun)
    else:
        impares.append(nun)
print (f'''A lista completa é {lista};
Os números pares são {pares};
Os números impares são {impares}.''')