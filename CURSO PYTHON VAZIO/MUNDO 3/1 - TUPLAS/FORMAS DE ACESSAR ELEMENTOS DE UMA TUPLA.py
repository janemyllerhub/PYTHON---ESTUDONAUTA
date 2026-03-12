lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print('=-=' * 18)
print('                        MODO 1')
print('=-=' * 18)
for c in lanche:
    print (f'Eu vou comer {c}')
print('=-=' * 18)
print('                        MODO 2')
print('=-=' * 18)
for cont in range(len(lanche)):
    print (f'Eu vou comer {lanche[cont]} na posição {cont}')
print('=-=' * 18)
print('                        MODO 3')
print('=-=' * 18)
for pos, c in enumerate(lanche):
    print (f'Eu vou comer {c} na posição {pos}')
print('=-=' * 18)
print('               MODO 4 (JUNTAR TUPLAS)')
print('=-=' * 18)
a = 1,2,3
b = 4,5,6
c = a+ b
print (c)
print (len(c)) #tamanho das duas tuplas juntas
print (c.count(5)) #quantas vezes aparece o 5 nas 2 tuplas
print (c.index(8)) #em que posição está o 8
print('=-=' * 18)
print('              MODO 5 (ORDEM ALFABÉTICA)')
print('=-=' * 18)
for c in lanche:
    print (f'Eu vou comer {sorted(lanche)}')
