from random import randint
cont = 0
tupla = []
print ('Os valores sorteados foram: ', end = ' ')
while cont < 5:
    user = (randint(1, 10))
    tupla.append(user)
    print (f'{user}', end = ' ')
    cont += 1
print (f'\nO menor valor sorteado foi: {min(tupla)}')
print (f'O maior valor sorteado foi: {max(tupla)}')