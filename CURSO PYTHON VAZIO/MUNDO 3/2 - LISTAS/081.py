continuar = 'S'
valores = []
valor = 0
while continuar == 'S':
    nun = int(input('Digite um valor: '))
    valores.append(nun)
    if nun == 5:
        valor += 2
    cont = str(input('Deseja continuar [S/N]? ')).upper().strip()
    continuar = cont
print (f'''Você digitou {len(valores)} elementos.
Os valores em ordem decrescente são {sorted(valores, reverse=True)}''')
if valor == 2:
    print ('O valor 5 faz parte da lista!')
else:
    print ('O valor 5 não foi encontrado na lista.')
