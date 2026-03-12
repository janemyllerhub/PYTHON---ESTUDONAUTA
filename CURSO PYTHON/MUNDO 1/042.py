#Faça um algoritmo que pergunte ao usuário um número inteiro e positivo qualquer e mostre uma contagem até esse valor:
#Ex: Digite um valor: 35
#Contagem: 1 2 3 4 5 6 7 ... 33 34 35 Acabou!
#EX: FOR
#cont = 0
#nun = int(input('Digite algum valor: '))
#for nun in range (0, nun):
#    print (f'{nun+1}', end = ' > ')
#    cont += 1
#print ('FIM')

#EX: WHILE
cont = 0
nun = int(input('Digite um valor: '))
while cont < nun:
    print (f'{cont+1}', end = ' > ')
    cont += 1
print ('FIM')