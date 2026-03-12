# Desenvolva uma lógica que leia os valores de A, B e C de uma equação do segundo grau e mostre o valor de Delta.
a = float(input('Digite o valor A: '))
b = float(input('Digite o valor B: '))
c = float(input('Digite o valor C: '))
delta = b**2 - 4*a*c
print (f'O delta dos valores {a}, {b} e {c} é igual a: {delta:.1f}')