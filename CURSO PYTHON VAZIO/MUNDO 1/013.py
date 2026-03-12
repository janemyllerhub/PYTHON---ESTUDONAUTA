#Faça um algoritmo que leia o salário de um funcionário, calcule e mostre o seu novo salário, com 15% de aumento.
salario = float(input('Qual o seu salário atual? R$ '))
aumento = salario / 100 * 15
print (f'O seu sálario no valor de R$ {salario:.2f} com um aumento de 15% passa a ser R$ {salario+aumento:.2f}')