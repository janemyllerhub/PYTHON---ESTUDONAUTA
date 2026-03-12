#Escreva um algoritmo que leia dois números inteiros e compare-os, mostrando na tela uma das mensagens abaixo:
#O primeiro valor é o maior
#O segundo valor é o maior
#Não existe valor maior, os dois são iguais

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print (f'O número {n1} é maior do que o número {n2}.')
if n2 > n1:
    print (f'O número {n2} é maior do que o número {n1}.')
if n1 == n2:
    print (f'Os números {n1} e {n2} são iguais.')

