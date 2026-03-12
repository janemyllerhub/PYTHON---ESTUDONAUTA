#Desenvolva um aplicativo que leia o peso e a altura de 7 pessoas, mostrando no final:
#a) Qual foi a média de altura do grupo
#b) Quantas pessoas pesam mais de 90Kg
#c) Quantas pessoas que pesam menos de 50Kg tem menos de 1.60m
#d) Quantas pessoas que medem mais de 1.90m pesam mais de 100Kg.

#EX: FOR
#mais_90 = menos_50 = mais_100 = soma = 0
#for n in range (1,8):
#    print('=-=' * 10)
#    print (f'           PESSOA {n}')
#    print('=-=' * 10)
#    peso = float(input('Peso: '))
#    altura = float(input('Altura: '))
#    soma += altura
#    if peso > 90:
#        mais_90 += 1
#    if peso < 50 and altura < 1.60:
#        menos_50 += 1
#    if peso > 100 and altura > 1.90:
#        mais_100 += 1
#print (f'''A média de altura do grupo é de {soma / 7:.2f}
#Temos {mais_90} pessoas pesando mais de 90kg, {menos_50} pessoas pesando menos de 50kg e tendo menos de 1.60m de altura e
#{mais_100} pessoas pesando mais de 100kg com mais de 1.90m de altura.''')

#a) Qual foi a média de altura do grupo
#b) Quantas pessoas pesam mais de 90Kg
#c) Quantas pessoas que pesam menos de 50Kg tem menos de 1.60m
#d) Quantas pessoas que medem mais de 1.90m pesam mais de 100Kg.

soma = mais_90 = menos_50 = mais_100 = 0
cont = 1
while cont < 8:
    print('=-=' * 10)
    print (f'           PESSOA {cont}')
    print('=-=' * 10)
    peso = float(input('Peso: '))
    altura = float(input('Altura: '))
    cont += 1
    soma += altura
    if peso > 90:
        mais_90 += 1
    if peso < 50 and altura < 1.60:
        menos_50 += 1
    if altura > 1.90 and peso > 100:
        mais_100 += 1
print (f'''A média de altura do grupo é de {soma / 7:.2f}
Temos {mais_90} pessoas pesando mais de 90kg, {menos_50} pessoas pesando menos de 50kg e tendo menos de 1.60m de altura e
{mais_100} pessoas pesando mais de 100kg com mais de 1.90m de altura.''')
