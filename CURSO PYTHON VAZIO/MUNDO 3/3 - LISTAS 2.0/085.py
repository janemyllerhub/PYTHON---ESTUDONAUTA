numeros = [[],[]]
for c in range (1,8):
    nun = int(input(f'Número {c}: '))
    if nun % 2 == 0:
        numeros[0].append(nun)
    else:
        numeros[1].append(nun)
numeros[0].sort()
numeros[1].sort()
print (f'''Números pares: {numeros[0]}
Números impares: {numeros[1]}''')