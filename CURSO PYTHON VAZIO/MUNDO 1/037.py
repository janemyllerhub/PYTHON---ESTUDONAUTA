#Uma empresa precisa reajustar o salário dos seus funcionários, dando um aumento de acordo com alguns fatores. Faça um programa que leia o salário atual,
#o gênero do funcionário e há quantos anos esse funcionário trabalha na empresa. No final, mostre o seu novo salário, baseado na tabela a seguir:
# Mulheres
# menos de 15 anos de empresa: +5%
# de 15 até 20 anos de empresa: +20%
# mais de 20 anos de empresa: +40%
# Homens
# menos de 20 anos de empresa: +3%
# de 20 até 30 anos de empresa: +13%
# mais de 30 anos de empresa: +25

salario = int(input('Qual o seu salário atual? R$ '))
sexo = str(input('Qual o seu gênero [F/M]? ')).upper().strip()
anos = int(input('A quantos anos você se escraviza nesta empresa? '))
media = 0
if sexo == 'F':
    if anos < 15:
        media = (salario / 100) * 5
    if 15 < anos < 20:
        media = (salario / 100) * 20
    if anos > 20:
        media = (salario / 100) * 40
elif sexo == 'M':
    if anos < 20:
        media = (salario / 100) * 3
    if 20 < anos < 30:
        media = (salario / 100) * 13
    if anos > 30:
        media = (salario / 100) * 25
print (f'Parabéns!!! Com {anos} anos de empresa o seu sálario de R$ {salario:.2f} passa a ser R$ {salario + media:.2f} por mês.')