soma = 0
velho = []
cont = 0
for person in range (1,3):
        print (F'----- {person}° PESSOA -----')
        none = str(input('Nome: ')).strip()
        age = int(input('Idade: ').strip())
        sex = str(input('Sexo [F/M]: ')).upper().strip()
        soma += age
        if sex == 'M':
            velho.append((none, age))
        if age < 20 and sex == 'F':
            cont += 1
homemvelho = max (velho, key=lambda x: x[1])
mediaage = soma / 4
print (f'A média de idade do grupo é de {mediaage:.1f} anos de idade.')
print (f'O homem mais velho do grupo se chama {homemvelho[0]} e a sua idade é de {homemvelho[1]} anos.')
if cont >= 2:
    print (f'O grupo possui {cont} mulheres com menos de 20 anos de idade.')
else:
    print(f'O grupo possui apenas uma mulher com menos de 20 anos de idade.')