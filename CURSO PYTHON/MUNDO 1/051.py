#Faça um aplicativo que leia o preço de 8 produtos. No final, mostre na tela qual foi o maior e qual foi o menor preço digitados.
#EX: FOR
#precos = []
#for n in range (1, 9):
#    produtos = float(input(f'Valor do {n}° produto: R$  '))
#    precos.append(produtos)
#print (f'O menor preço foi no valor de R$ {min(precos):.2f} e o maior foi no valor de R$ {max(precos):.2f}')

#EX: WHILE
cont = 1
precos = []
while cont < 9:
    produtos = float(input(f'Valor do {cont}° produto: R$ '))
    precos.append(produtos)
    cont += 1
print (f'O menor preço foi no valor de R$ {min(precos):.2f} e o maior no valor de R$ {max(precos):.2f}')