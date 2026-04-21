numeros = 0
lista = list()
for c in range(1,8):
    nun = int(input(f'{c}°: Digite um valor: '))
    numeros = nun
    if nun / 2 == 0:
        lista.append(numeros[:])
    else:
        lista.append(numeros[:])
print (f'Os valores pares digitados foram: {lista[0]}')
print (f'Os valores ímpares digitados foram: {lista[1]}')
