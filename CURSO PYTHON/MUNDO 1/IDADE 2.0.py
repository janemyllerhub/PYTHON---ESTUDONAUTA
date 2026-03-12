import datetime

data = datetime.datetime.now()
ano = data.year
nascimento = int(input('Em que ano você nasceu? '))
idade = ano - nascimento
if idade >= 18:
    print (f'Você possui {idade} anos e já alcançou a maior idade!')
else:
    print (f'Você possui {idade} anos e ainda não alcançou a maior idade!')