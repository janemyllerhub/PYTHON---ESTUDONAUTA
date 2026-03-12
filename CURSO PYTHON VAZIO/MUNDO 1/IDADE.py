import datetime
calendar = datetime.datetime.now()
atual = calendar.year
nascimento = int(input('Em qual ano você nasceu? '))
print (f'Você possui {atual - nascimento} anos')