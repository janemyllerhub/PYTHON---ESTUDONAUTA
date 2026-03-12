#Desenvolva um programa que mostre na tela a seguinte contagem: 100 95 90 85 80 ... 0 Acabou!
#EX: FOR
#cont = 0
#for n in range (100, -5, -5):
#    print (f'{n}', end = ' > ')
#    cont -= 5
#print ('FIM')

#EX: WHILE
cont = 100
while cont >= 0:
    print (f'{cont}',end = ' > ')
    cont -= 5
print ('FIM')