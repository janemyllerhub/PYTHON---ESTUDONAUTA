from datetime import date
ano = int(input('Em que ano você nasceu? '))
atual = date.today().year
cal = atual - ano
cal2 = 18 - cal
cal3 = cal - 18
if cal < 18:
    print ('Você ainda não possui idade suficiente para se alistar.')
    print (f'Ainda faltam {cal2} anos para você se alistar!')
    print (f'Seu alistamento será em {atual + cal2}')
elif cal > 18:
    print ('Já passou da hora em amigão? ')
    print (f'Era para você ter se alistado a {cal3} anos atrás em {atual - cal3}!')
elif cal == 18:
    print (f'Quem nasceu em {ano} tem {cal} anos em {atual}...')
    print ('\033[1;33m️⚠️!!!!Você precisa se alistar imediatamente!!!!⚠️\033[1;33m\033[0;00m')



