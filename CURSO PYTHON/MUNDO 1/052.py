#Crie um algoritmo que leia a idade de 10 pessoas, mostrando no final:
#a) Qual é a média de idade do grupo
#b) Quantas pessoas tem mais de 18 anos
#c) Quantas pessoas tem menos de 5 anos
#d) Qual foi a maior idade lida
#EX: FOR
#maior_18 = menos_5 = 0
#idades = []
#soma = 0
#for n in range (1,11):
#    age = int(input(f'{n}: Qual seria a sua idade: '))
#    idades.append(age)
#    soma += age
#    if age > 18:
#        maior_18 += 1
#    if age < 5:
#        menos_5 += 1
#print (f'''A média de idade do grupo é de {soma / 10:.0f};
#Temos {maior_18} pessoas maiores de 18 anos;
#Temos {menos_5} pessoas menores de 5 anos;
#E a maior idade do grupo é de {max(idades)}.''')

#EX: WHILE
maior_18 = menor_5 = soma = 0
cont = 1
idades = []
while cont < 11:
    age = int(input(f'{cont} - Sua idade: '))
    cont += 1
    soma += age
    idades.append(age)
    if age > 18:
        maior_18 += 1
    if age < 5:
        menor_5 += 1
print (f'''A média de idade do grupo é de {soma / 10:.0f};
Temos {maior_18} pessoas maiores de 18 anos;
Temos {menor_5} pessoas menores de 5 anos;
E a maior idade do grupo é de {max(idades)}.''')