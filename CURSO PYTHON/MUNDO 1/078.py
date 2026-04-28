#Escreva um programa que leia 15 números e guarde-os em um vetor. No final, mostre o vetor inteiro na tela e em seguida mostre em que posições foram digitados valores que são múltiplos de 10.
vetor = []
cont = 1
for c in range (0,10):
    nun = (int(input('Digite um número: ')))
    vetor.append(nun)
    cont += 1
print (vetor, end = ' - ' if cont < 10 else '\n')
print ('='*48)
print ('LISTAGEM DE NÚMEROS MULTIPLOS DE 10'.center(48))
print ('='*48)
for numeros in vetor:
    for unidades in str(numeros):
        if str(unidades) in '0':
            print (f'\033[034m[{numeros}]\033[034m\033[0m', end = ' ')
        if str(unidades) not in '0':
            print (f'{numeros}', end = ' ')
#descobrir como que eu mostro na tela sem duplicação
#centralizar essa merda