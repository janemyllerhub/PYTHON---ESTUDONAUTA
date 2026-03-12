#[DESAFIO] Crie um programa que leia o tamanho de três segmentos de reta. Analise seus comprimentos e diga se é possível formar um triângulo com essas
#retas. Matematicamente, para três segmentos formarem um triângulo, o comprimento de cada lado deve ser menor que a soma dos outros dois.

seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))
if seg1 < (seg2+seg3) and seg2 < (seg1+seg3) and seg3 < (seg1+seg2):
    print (f'As retas {seg1}, {seg2} e {seg3} formam um triângulo!!!')
else:
    print (f'As retas {seg1}, {seg2} e {seg3} NÃO formam um triângulo!!!')
