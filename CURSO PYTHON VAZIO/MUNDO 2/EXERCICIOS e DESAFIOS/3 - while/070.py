print('\033[034m==\033[034m\033[0m' * 17)
print ('       COTAÇÃO DE MATERIAIS')
print('\033[034m==\033[034m\033[0m' * 17)

lis = []
total = prod = 0
while True:
    produto = str(input('Nome do produto: ')).strip()
    preco = int(float(input('Preço: ')))
    total += preco
    print('\033[034m==\033[034m\033[0m' * 17)
    lis.append((produto, preco))
    conti = str(input('Possui mais algum produto [S/N]? ')).strip().upper()
    print('\033[034m==\033[034m\033[0m' * 17)
    if preco > 1000:
        prod += 1
    if conti not in 'N':
        continue
    else:
        break
menor = min(lis, key = lambda x: x[1])
print ('ANALISE DE LISTA DE COMPRAS FEITAS')
print('\033[034m==\033[034m\033[0m' * 17)
print (f'O total da compra foi de R$ {total:.2f}')
if prod > 1:
    print (f'Temos {prod} produtos valendo mais de R$ 1000.00')
if prod == 1:
    print(f'Temos apenas {prod} produto valendo mais de R$ 1000.00')
if prod == 0:
    print(f'Não temos nenhum produto valendo mais de R$ 1000.00')
print (f'O produto mais barato foi {menor[0]} valendo R$ {menor[1]:.2f}')


