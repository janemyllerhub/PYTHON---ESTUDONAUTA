print ('Lista normal'.center(36, '='))
nun = [3,2,1,4]
nun.append(5)
nun.insert(0,0)
nun.sort()
print (nun)
print (len(nun), 'valores')
print ('Usando RANGE'.center(36, '='))
valores = list(range(0,6))
print (valores)
print ('Usando NUMERATE'.center(36, '='))
valores = []
valores.append(27)
valores.append(11)
valores.append(2005)
for v in valores:
    print(f'{v} ', end='/' if v != 2005 else '\n')
for c,v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
