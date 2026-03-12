print ('=-='*6)
print ('       MENU')
print ('=-='*6)
print ('''[1] De 1 a 10
[2] De 10 a 1
[3] Sair''')
print ('=-='*6)
user = 2
crescente = 1
decrescente = 10
while user != 3:
    crescente = 1
    decrescente = 10
    res = int(input('Qual a sua opção: '))
    user = res
    if user not in (3, 2, 1):
        print('Opção invalida, tente novamente!')
    else:
        if user == 1:
            while crescente < 11:
                print (f'{crescente}', end = '... ' if crescente != 10 else '\n')
                crescente += 1
        if user == 2:
            while decrescente != 0:
                print (f'{decrescente}', end = '... ' if decrescente != 1 else '\n')
                decrescente -= 1