lista = list()
pessoas = 'S'
cont = 0
print ('=-='*20)
while pessoas == 'S':
    nome = (str(input('Nome: '))).capitalize().strip()
    peso = (float(input('Peso: ')))
    pessoas = str(input('Mais pessoas para cadastrar? ')).upper().strip()
    lista.append((nome,peso))
    cont += 1
pesada = max(lista, key=lambda p: p[1])
leve = min(lista, key=lambda p: p[-1])
nome_pesada = lista.index(pesada)
nome_leve = lista.index(leve)
print ('=-='*20)
print (f'Temos {cont} pessoas cadastradas')
for p in lista:
    if p[1] > 1:
        print (f'''O maior peso do grupo de pessoas é de {pesada[1]}Kg. Peso de {lista[nome_pesada][0]}!
        Enquanto menor é de {leve[1]}Kg. Peso de {lista[nome_leve][0]}!''')

#descobrir como que eu faço quando tem pesos iguais