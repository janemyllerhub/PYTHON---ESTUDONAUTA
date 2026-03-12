#Crie um aplicativo que mostre na tela a seguinte contagem: 0 3 6 9 12 15 18 Acabou!
#EX: FOR
#cont = 0
#for n in range (0, 19, 3):
#    print (f'{n}', end = ' > ')
#    cont += 1
#print ('FIM')

#EX: WILE
cont = 0
while cont <= 18:
    print (f'{cont}', end = ' > ')
    cont += 3
print ('FIM')