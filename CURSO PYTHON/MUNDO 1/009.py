#Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$) e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,45.
reais = float(input('Quantos R$ você possui? R$ '))
print (f'Convertido em dolar você teria $ {reais/3.45:.2f}')