nun = int(input('Digite um número: '))
contador = nun
lista = []
resultado = 1

while contador != 0:
    print (f'{contador}', end = ' x ' if contador != 1 else ' = ')
    lista.append(contador)
    resultado *= contador
    contador -= 1
print (f'{resultado}')
