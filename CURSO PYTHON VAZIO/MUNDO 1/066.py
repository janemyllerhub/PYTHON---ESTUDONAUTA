#Escreva um programa que leia um número qualquer e mostre a tabuada desse número, usando a estrutura “para”.
nun = int(input('Digite um número: '))
cont = 1
while cont != 11:
    print (f'{nun} x {cont} = {nun * cont}')
    cont += 1