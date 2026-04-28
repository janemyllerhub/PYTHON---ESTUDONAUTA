#Escreva um programa que leia 15 números e guarde-os em um vetor. No final, mostre o vetor inteiro na tela e em seguida mostre em que posições foram digitados valores que são múltiplos de 10.
vetor = []
cont = 0
for c in range (0,10):
    nun = (int(input('Digite um número: ')))
    vetor.append(nun)
    cont += 1
print (vetor, end = ' - ' if cont < 10 else '\n')
print ('='*48)
print ('LISTAGEM DE NÚMEROS MULTIPLOS DE 10'.center(48))
print ('='*48)
for i in vetor:
    if len(str(i)).index(0) == 0:
        print (vetor, end = ' - ' if cont < 10 else '\n')
#descobrir como que eu mostro na tela sem duplicação
#centralizar essa merda