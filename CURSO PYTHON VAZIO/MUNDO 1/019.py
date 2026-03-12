#Crie um algoritmo que leia o nome e as duas notas de um aluno, calcule a sua média e mostre na tela. No final, analise a média e mostre se o aluno teve ou
#não um bom aproveitamento (se ficou acima da média 7.0).

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2

if media > 7:
    print (f'Parabéns!!! A sua média foi de {media} tendo um otimo aproveitamento!')
if media == 7:
    print (f'Foi por pouco em! Mas a sua média foi de {media} tendo um aproveitamento mediano!')
if media < 7:
    print (f'Reprovado! Com uma média de {media} você não conseguiu passar.')
