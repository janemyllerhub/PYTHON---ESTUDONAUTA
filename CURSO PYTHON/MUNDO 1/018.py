#Faça um programa que leia o ano de nascimento de uma pessoa, calcule a idade dela e depois mostre se ela pode ou não votar.

import datetime
data_atual = datetime.datetime.now()
ano_atual = data_atual.year
ano = int(input('Em qual ano você veio ao mundo? '))
idade = ano_atual - ano
votar = 16-idade
if idade < 16 and votar > 1:
    print (f'Com {idade} anos de idade infelizmente você ainda não pode votar, mas daqui {votar} anos você podera votar!')
if idade < 16 and votar == 1:
    print (f'Com {idade} anos de idade infelizmente você ainda não pode votar, mas daqui {votar} ano você podera votar!')
if idade >= 16:
    print (f'Se diriga a uma urna para votar!')