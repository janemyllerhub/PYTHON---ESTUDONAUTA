pro = float(input('Preço total dos produtos: '))
print ('FORMAS DE PAGAMENTO')
print ('[1] PIX')
print ('[2] à vista no cartão')
print ('[3] 2x no cartão')
print ('[4] 3x ou mais no cartão')
op = int(input('Qual a opção escolhida? '))
if op == 1:
    print (f'Parabens, passando no PIX voce recebe 10% de deconto totalizando: R$ {pro - (pro / 100 * 10):.2f}')
elif op == 2:
    print (f'Parabens, passando À VISTA NO CARTÃO voce recebe 5% de desconto totalizando: R$ {pro - (pro / 100 * 5):.2f}')
elif op == 3:
    print (f'Passando de 2X NO CARTÃO voce paga o preço normal do produto: R$ {pro}')
elif op == 4:
    parc = int(input('Em quantas vezes voce ira parcelar? '))
    if parc >= 3:
      print (f'Passando em {parc} VEZES voce paga 20% de juros totalizando: R$ {pro + (pro / 100 * 20):.2f}')