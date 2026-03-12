#[DESAFIO] Faça um programa que mostre os 10 primeiros elementos da Sequência de Fibonacci:
#0 1 1 2 3 5 8 13 21...
a = 0
b = 1
c = a + b
cont = 0
print (f'{a}... {b}... {c}', end = '... ')
while cont < 7:
    a = b
    b = c
    c = a + b
    print (f'{c}', end = '... ' if cont < 6 else '!')
    cont += 1