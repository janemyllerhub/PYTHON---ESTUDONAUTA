#Crie um programa que leia o nome e o salário de um funcionário, mostrando no
#final uma mensagem.
#Ex:
#Nome do Funcionário: Maria do Carmo
#Salário: 1850,45
#O funcionário Maria do Carmo tem um salário de R$ 1850,45 em junho.

nome = str(input('Qual o seu nome? ')).strip().upper()
salario = str(input('Qual o seu salário? ')).strip()
print (f'A funcionaria {nome} tem um sálario de R$ {salario} em junho.')