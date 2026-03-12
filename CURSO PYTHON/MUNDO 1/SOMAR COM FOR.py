contador = 0
soma = 0
for n in range (1,11):
    nun = int(input(f'{n}° número: '))
    soma += nun
    contador += 1
print (f'A soma de todos os números digitados é igual a: {soma}')