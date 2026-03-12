#Escreva um programa que leia o ano de nascimento de um rapaz e mostre a sua situação em relação ao alistamento militar.
#Se estiver antes dos 18 anos, mostre em quantos anos faltam para o alistamento.
#Se já tiver depois dos 18 anos, mostre quantos anos já se passaram do alistamento.
import datetime
data_atual = datetime.datetime.now()
ano = data_atual.year
nascimento = int(input('Em qual ano você nasceu? '))
age = ano - nascimento
if age < 18 and 18 - age > 1:
    print (f'''Você possui {age} anos de idade.
E poderá se alistar daqui {18-age} anos.''')
if age < 18 and 18 - age == 1:
    print (f'''Você possui {age} anos de idade.
E poderá se alistar daqui {18-age} ano.''')
if age >= 18 and age - 18 > 1:
    print (f'''Você possui {age} anos de idade.
E já poderia ter se alistado a {age-18} anos.''')
if age >= 18 and age - 18 == 1:
    print (f'''Você possui {age} anos de idade.
E já poderia ter se alistado a {age-18} ano.''')
if age == 18 :
    print (f'''Você possui {age} anos de idade.
E você já pode se alistar no ano atual de {ano}.''')