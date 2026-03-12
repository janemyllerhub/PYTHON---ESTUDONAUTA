#Faça um algoritmo que mostre na tela a seguinte contagem: 10 9 8 7 6 5 4 3 Acabou!
#EX: FOR
#cont = 0
#for n in range (10, 2, -1):
#    print (f'{n}', end = ' > ')
#    cont += 1
#print ('FIM')

#EX: WHILLE
cont = 10
while cont >= 3:
    print (f'{cont}', end = ' > ')
    cont -= 1
print ('FIM')