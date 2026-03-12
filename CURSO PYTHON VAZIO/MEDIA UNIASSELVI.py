print ('\033[33m=-='*23)
print (f'MÉDIA UNIASSELVI [7]'.center(69))
print ('=-='*23)
soma_notas = 0
cont = 0
lista = []
s = 'S'
while s == 'S':
    nota = int(input(f'Qual a nota da sua {cont + 1}° prova? '))
    if cont == 3:
        print('=-=' * 23)
    soma_notas += nota
    lista.append(nota)
    cont += 1
    if cont < 4:
        prova = str(input(f'Você realizou a {cont + 1 if cont < 5 else cont}° prova [S/N]? ')).upper().strip()
        print('=-=' * 23)
        s = prova
    else:
        break
media = soma_notas / len(lista)
if len(lista) < 4:
    print (f'''Você está indo bem! 
Realize as outras provas para saber se foi aprovado ou não.''')
else:
    print(f'A sua média é de: {media}')
    if media == 7:
        print ('Passou por pouco em...')
    elif media > 7:
        print ('Parabéns, aprovadíssimo(a)')
    elif media < 7:
        print ('Reprovado(a)!')
print ('=-='*23)
