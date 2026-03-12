#Desenvolva um programa que leia o nome de um funcionário, seu salário, quantos anos ele trabalha na empresa e mostre seu novo salário, reajustado de
#acordo com a tabela a seguir:
# Até 3 anos de empresa: aumento de 3%
# Entre 3 e 10 anos: aumento de 12.5%
# 10 anos ou mais: aumento de 20%

nome = str(input('Nome: ')).capitalize().strip()
salario = int(input('Salário: '))
anos = int(input('Anos na empresa: '))
print(f'{nome}, com um tempo de {anos} anos na empresa o seu salário que era R$ {salario:.2f} passa a ser de ',end = '')
if anos <= 3:
    media = salario / 100 * 3
    print (f'R$ {salario + media:.2f} com 3% de acrescimo.',end = '')
if 3 < anos < 10:
    media = salario / 100 * 12.5
    print(f'R$ {salario + media:.2f} com 12.5% de acrescimo.',end = '')
if anos >= 10:
    media = salario / 100 * 20
    print(f'R$ {salario + media:.2f} com 20% de acrescimo.',end = '')
