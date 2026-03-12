#Desenvolva um algoritmo que leia o nome, a idade e o sexo de várias pessoas. O programa vai perguntar se o usuário quer ou não continuar. No final, mostre:
#a) O nome da pessoa mais velha
#b) O nome da mulher mais jovem
#c) A média de idade do grupo
#d) Quantos homens tem mais de 30 anos
#e) Quantas mulheres tem menos de 18 anos
cont = 1
jovem = idade = []
lista_geral = []
continuacao = 'S'
velha = age_jovem = ''
homens = mulheres = 0
print ('=-='*9)
print ('    CADASTRO DE PESSOAS')
while continuacao == 'S':
    print('=-=' * 9)
    print(F'        {cont}° PESSOA')
    print('=-=' * 9)
    name = str(input('Nome: ' )).title().strip()
    age = float(input('Idade: '))
    sex = str(input('Sexo [F/M]: ')).upper().strip()
    continuar = str(input('Deseja continuar [S/N]? ')).upper().strip()
    continuacao = continuar
    cont += 1
    idade.append(age)
    lista_geral.append((name, age))
    people = max(lista_geral, key=lambda x: x[1])
    velha = people
    if sex == 'F':
        jovem.append((name, age))
        age = min(jovem, key=lambda x: x[1])
        age_jovem = age
    if sex == 'M' and age > 30:
        homens += 1
    if sex == 'F' and age > 18:
        mulheres += 1
if homens > 1 and mulheres > 1:
    print (f'''O nome da pessoa mais velha se chama "{velha[0]}" e a mulher mais jovem se chama "{age_jovem[0]}";
A média de idade do grupo é de {(sum(idade)) / cont:.0f};
Temos {homens} homens com mais de 30 anos e {mulheres} mulheres com mais de 18 anos.''')
if homens > 1 and mulheres == 0:
    print (f'''O nome da pessoa mais velha se chama "{velha[0]}";
A média de idade do grupo é de {(sum(idade)) / cont:.0f};
Temos {homens} homens com mais de 30 anos.''')
if homens == 0 and mulheres > 1:
    print(f'''O nome da pessoa mais velha se chama "{velha[0]}" e a mulher mais jovem se chama "{age_jovem[0]}";
A média de idade do grupo é de {(sum(idade)) / cont:.0f};
Temos {mulheres} mulheres com mais de 18 anos.''')
if homens == 1 and mulheres == 0:
    print (f'Temos apenas um homem cadastrado!')
if mulheres == 1 and homens == 0:
    print (f'Temos apenas uma mulher cadastrada!')
