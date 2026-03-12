#Crie um programa que leia duas notas de um aluno e calcule a sua média, mostrando uma mensagem no final, conforme a média atingida:
#Média até 4,9: REPROVADO
#Média entre 5,0 e 6,9: RECUPERAÇÃO
#Média 7,0 ou superior: APROVADO

nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
media = (nota1 + nota2) / 2
if media <= 4.9:
    print (f'A sua média é de {media}, você está REPROVADO.')
if 5.0 < media < 6.9:
    print (f'A sua média é de {media}, você está de RECUPERAÇÃO.')
if media >= 7:
    print (f'A sua média é de {media}, você está de APROVADO.')