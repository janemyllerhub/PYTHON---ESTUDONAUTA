#Crie um programa que leia o número de dias trabalhados em um mês e mostre o salário de um funcionário, sabendo que ele trabalha 8 horas por dia e ganha R$25
#por hora trabalhada.
dias = int(input('Dias trabalhados: '))
hora = dia = 8
print (f'''Considerando que você trabalhou por {dias} dias, você possui acumuladas {hora*dias} horas. '
O seu sálario será R$ {(hora * 25) * dias:.2f} esse mês.''')