#Crie um programa que leia o sexo e a idade de várias pessoas. O programa vai perguntar se o usuário quer continuar ou não a cada pessoa. No final, mostre:
#a) qual é a maior idade lida
#b) quantos homens foram cadastrados
#c) qual é a idade da mulher mais jovem
#d) qual é a média de idade entre os homens
continuar = 'S'
cont = 1
lista_age = lista_mulher = []
homens = 0
soma_homens = sex_mulher = 0
while continuar == 'S':
    print ('=-='*10)
    print (f'    CADASTRO DA {cont}° PESSOA')
    print('=-=' * 10)
    age = int(input('Idade: '))
    sex = str(input('Sexo [F/M]: ')).upper().strip()
    lista_age.append(age)
    if sex == 'M':
        homens += 1
        soma_homens += age
    if sex == 'F':
        lista_mulher.append(age)
        sex_mulher += 1
    continuar = str(input('Deseja continuar? ')).upper().strip()
    cont += 1
    continuar = continuar
if sex_mulher >= 1 and homens >= 1:
    print (f'''A maior idade lida é de {max(lista_age)} anos;
Foram cadastrados no total {homens} homens;
A idade da mulher mais jovem é de {min(lista_mulher)} anos;
A média de idade dos homens é de {(soma_homens / homens):.2f}''')
if sex_mulher >= 1 and homens == 0:
    print(f'''A maior idade lida é de {max(lista_age)} anos;
A idade da mulher mais jovem é de {min(lista_mulher)} anos.''')
if sex_mulher == 0 and homens >= 1:
    print(f'''A maior idade lida é de {max(lista_age)} anos;
Foram cadastrados no total {homens} homens;
A média de idade dos homens é de {(soma_homens / homens):.2f}''')