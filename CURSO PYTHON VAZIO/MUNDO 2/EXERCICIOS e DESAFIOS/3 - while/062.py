print('\033[034m=-=\033[034m\033[0m' * 6)
print ('GERADOR DE PA')
print('\033[034m=-=\033[034m\033[0m' * 6)

termo1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

termo = termo1
cont = 0
mais = 10
total = 0
while mais != 0:
   total = total + mais
   while cont <= total:
        print (f'{termo}', end = " => ")
        termo += razao
        cont += 1
   print ('Pausa!')
   mais = int(input('Quantos termos você deseja a mais? '))
print ('fim')