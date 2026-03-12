#Faça um programa que leia a idade e o sexo de 5 pessoas, mostrando no final:
#a) Quantos homens foram cadastrados
#b) Quantas mulheres foram cadastradas
#c) A média de idade do grupo
#d) A média de idade dos homens
#e) Quantas mulheres tem mais de 20 anos
#EX: FOR
#homens = mulheres = mulher_20 = soma = 0
#idades = []
#men = []
#homem = 0
#for n in range (1,6):
#    age = int(input('Qual a sua idade: '))
#    sex = str(input('Qual a sua sexualidade [F/M]? ')).strip().upper()
#    soma += age
#    idades.append(age)
#    if sex == 'M':
#        homens += 1
#        men.append(age)
#        homem += age
#    if sex == 'F':
#        mulheres += 1
#    if age > 20 and sex == 'F':
#        mulher_20 += 1
#if mulheres and homens > 1:
#    print (f'''Temos {mulheres} mulheres cadastradas {homens} homens cadastrados.
#A média de idade do grupo é de {soma / 5:.0f};
#A média de idade dos homens é de {homem / homens:.0f};
#E temos {mulher_20} nulheres com mais de 20 anos.''')
#if mulheres > 1 and homens == 0:
#    print (f'''Temos {mulheres} mulheres cadastradas e nenhum homem cadastrado.
#A média de idade do grupo é de {soma / 5:.0f};
#E temos {mulher_20} mulheres com mais de 20 anos.''')
#if homens > 1 and mulheres == 0:
#    print(f'''Temos {homens} homens cadastrados e nenhuma mulher cadastrada.
#A média de idade do grupo é de {soma / 5:.0f};
#A média de idade dos homens é de {homem / homens:.0f}.''')

#EX WHILE
cont = homens = mulheres = soma = soma_homens = mulheres_20 = 0
while cont < 5:
    age = int(input('Qual seria a sua idade: '))
    sex = str(input('Digite o seu sexo (F/M): ')).strip().upper()
    cont += 1
    soma += age
    if sex == 'F':
        mulheres += 1
    if sex == 'M':
        soma_homens += age
        homens += 1
    if sex == 'F' and age > 20:
        mulheres_20 += 1
if mulheres > 1 and homens > 1:
    print (f'''Temos {homens} homens e {mulheres} mulheres cadastrados.
A média das idades informadas equivalem a: {soma / 5:.0f} e media de idade dos homens é de: {soma_homens / homens:.0f}, 
e no total temos {mulheres_20} mulheres com mais de 20 anos.''')
if mulheres > 1 and homens == 0:
    print(f'''Temos {mulheres} mulheres cadastrados e nenhum homem cadastrado.
A média das idades informadas equivalem a: {soma / 5:.0f}, 
e no total temos {mulheres_20} mulheres com mais de 20 anos.''')
if homens > 1 and mulheres == 0:
    print(f'''Temos {homens} homens cadastrados e nenhuma mulher.
A media de idade dos homens cadastrados é de: {soma_homens / homens:.0f}.''')