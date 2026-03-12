#Crie um programa que leia o preço de um produto, calcule e mostre o seu PREÇO PROMOCIONAL, com 5% de desconto.
produto = float(input('Digite o valor do produto: R$ '))
desconto = produto / 100 * 5
print (f'O produto com um desconto de 5%, passa de R$ {produto:.2f} para R$ {produto-desconto:.2f}!!!!')