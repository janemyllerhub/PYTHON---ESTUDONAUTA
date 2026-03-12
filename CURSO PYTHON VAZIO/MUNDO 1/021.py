#Faça um algoritmo que leia um determinado ano e mostre se ele é ou não BISSEXTO.
ano = int(input('Qual ano você deseja verificar? '))
if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print (f'{ano} foi um ano bissexto!')
else:
    print (f'{ano} NÃO é um ano bissexto.')