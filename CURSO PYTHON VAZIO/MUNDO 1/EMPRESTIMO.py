valor = float(input('Qual o valor do emprestimo? R$ '))
juros = (valor / 100) * 20
parcela = int(input('Você deseja parcelar em quantas vezes? '))
total = (valor + juros) / parcela
print (f'''Com os juros você precisa devolver o valor total de R$ {valor + juros:.2f}.
Dividindo em {parcela} parcelas fica R$ {total:.2f} durante {parcela} meses.''')