#Faça um programa que leia as duas notas de um aluno em uma matéria e mostre na tela a sua média na disciplina.
#Ex:
#Nota 1: 4.5
#Nota 2: 8.5
#A média entre 4.5 e 8.5 é igual a 6.5

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
print (f'A média entre as notas {nota1} e {nota2} é {(nota1 + nota2) / 2}')