numero = 0
contador = numero
lista = []
resultado = 1
continuar = 'S'
while continuar == 'S':
    nun = int(input('Digite um número: '))
    numero = nun
    contador = numero
    resultado = 1
    while contador != 0:
        print (f'{contador}', end = ' x ' if contador != 1 else ' = ')
        lista.append(contador)
        resultado *= contador
        contador -= 1
    print(f'{resultado}')
    cont = str(input('Deseja continuar [S/N]? ')).upper()
    continuar = cont


