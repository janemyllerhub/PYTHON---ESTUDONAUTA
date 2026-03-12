continuar = 'S'
soma = 0
while continuar == 'S':
    nun = int(input('Digite um número: '))
    soma += nun
    continuacao = str(input('Deseja continuar? ')).upper().strip()
    continuar = continuacao
print (f'A soma de todos os itens é igual a {soma}')