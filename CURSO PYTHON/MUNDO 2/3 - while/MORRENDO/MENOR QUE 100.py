print('\033[034m=-=\033[034m\033[0m' * 16)
print ('     O RESULTADO NÃO PODE EXCEDER DOS 100')
print('\033[034m=-=\033[034m\033[0m' * 16)
total = 0
nun = int(input('Digite um número: '))
total += nun
while total < 100:
    if total > 100:
        print (f'''O total da soma foi excedido...
Valor excedido: {total}''')
        break
    else:
        nun = int(input('Digite um número: '))
        total += nun
print (f'''O total da soma foi excedido...
Valor excedido: {total}''')