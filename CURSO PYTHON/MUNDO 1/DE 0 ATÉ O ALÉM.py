nun = int(input('Até qual número você quer que eu mostre? '))
salto = int(input('Qual o valor do salto? '))
contador = 0
for n in range(0,nun+1,salto):
    contador += 1
    print (f'{n}',end = ' > ')
print ('FIM')