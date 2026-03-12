print('\033[034m==\033[034m\033[0m' * 16)
print ('       PÁGINA DE CADASTRO')
print('\033[034m==\033[034m\033[0m' * 16)

lis = []
con = ''
cont = mai = men = mue = 0
while True:
        age = int(input('Idade: '))
        sex = str(input('Sexo [F/M]: ')).strip().upper()
        if sex not in ['F', 'M']:
            print ('Não entendi, digite o [SEXO] novamente com [F] ou [M]! ')
        else:
            print('\033[034m==\033[034m\033[0m' * 16)
            con = str(input('Quer continuar [S/N]? ').strip().upper())
            print('\033[034m==\033[034m\033[0m' * 16)
            lis.append((age, sex))
            if age >= 18:
                mai += 1
            if sex == 'M':
                men += 1
            if age < 20 and sex == 'F':
                mue += 1
            if con not in ['N']:
                continue
            else:
                break
if mai > 1:
    print (f'Temos um total de {mai} pessoas maiores de 18 anos.')
if mai == 1:
    print(f'Temos apenas {mai} pessoa maior de 18 anos.')
if mai == 0:
    print(f'Não temos maiores de 18 anos cadastrados')
if men > 1:
    print (f'Ao todo temos {men} homens cadastrados. ')
if men == 1:
    print(f'Temos apenas {men} homem cadastrado. ')
if men == 0:
    print(f'Não temos homens cadastrados')
if mue > 1:
    print (f'E temos {mue} mulheres com menos de 20 anos.')
if mue == 1:
    print(f'E temos apenas {mue} mulher com menos de 20 anos.')
if mue == 0:
    print(f'Não temos mulheres com menos de 20 anos cadastradas')


