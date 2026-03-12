print('\033[034m=-=\033[034m\033[0m' * 11)
print ('        TABUADA COM WHILE')
print('\033[034m=-=\033[034m\033[0m' * 11)
nun = 0
while True:
    nun = int(input('Qual número você quer? '))
    if nun <= 0:
        print('Programa finalizado devido o número ser negativo.')
        break
    cont = 1
    while cont <= 10:
        print (f'{nun} x {cont} = {nun * cont}')
        cont += 1