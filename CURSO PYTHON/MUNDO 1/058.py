#Faça um algoritmo que leia a idade de vários alunos de uma turma. O programa vai parar quando for digitada a idade 999. No final, mostre quantos alunos
#existem na turma e qual é a média de idade do grupo.
idade = total = alunos = 0
while idade != 999:
    age = int(input('Sua idade: '))
    idade = age
    if age != 999:
        total += age
        alunos += 1
print (f'Temos {alunos} alunos na turma e a média de idade do grupo é de {total / alunos:.2f}')