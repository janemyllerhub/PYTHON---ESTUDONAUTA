#A Sequência de Fibonacci é uma série numérica onde cada termo é a soma dos dois anteriores,
#começando geralmente com 0 e 1 (ou 1 e 1), resultando em 0, 1, 1, 2, 3, 5, 8, 13, 21,
#e assim por diante...

print('\033[034m=-=\033[034m\033[0m' * 8)
print (' SEQUÊNCIA DE FIBONACCI')
print('\033[034m=-=\033[034m\033[0m' * 8)

termo = int(input('Digite quantos termos você deseja: '))

t1 = 0
t2 = 1
cont = 3
print (f'{t1} > {t2}',end = " > ")
while cont <= termo:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print (f'{t3}',end = " > ")
    cont += 1
print ('FIM')
