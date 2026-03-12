#Faça um programa que leia 7 números inteiros e no final mostre o somatório entre eles.
#EX: FOR
#soma = 0
#for n in range (1,8):
#     nun = int(input(f'{n}° número: '))
#     soma += nun
#print (f'A soma dos números digitados é igual á: {soma}')

#EX: WHILE
soma = 0
cont = 1
while cont < 8:
    nun = int(input(f'{cont}° número: '))
    soma += nun
    cont += 1
print (f'O resultado da soma dos números digitados é igual á: {soma}')