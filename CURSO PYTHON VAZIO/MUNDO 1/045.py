#O programa acima vai ter um problema quando digitarmos o primeiro valor maior que o último. Resolva esse problema com um código que funcione em qualquer situação.
#EX: FOR
#primeiro = int(input('Digite o primeiro valor: '))
#ultimo = int(input('Digite o ultimo valor: '))
#incremento = int(input('Digite o incremento: '))
#cont = 0
#if primeiro < ultimo:
#    for n in range (primeiro,ultimo,incremento):
#        print (f'{n}', end = ' > ')
#        cont += 1
#else:
#    for n in range (primeiro,ultimo,-incremento):
#        print (f'{n}', end = ' > ')
#        cont += 1
#print ('FIM')

#EX: WHILE
primeiro = int(input('Digite o primeiro valor: '))
ultimo = int(input('Digite o ultimo valor: '))
incremento = int(input('Digite o incremento: '))
cont = primeiro
cont2 = primeiro
if primeiro < ultimo:
    while cont < ultimo:
        print (f'{cont}', end = ' > ')
        cont += incremento
else:
    while cont2 > ultimo:
        print (f'{cont2}', end = ' > ')
        cont2 -= incremento
print ('FIM')