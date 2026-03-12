#[DESAFIO] Refaça o algoritmo 25, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais
# ESCALENO: todos os lados diferentes

seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))

if seg1 < (seg2+seg3) and seg2 < (seg1+seg3) and seg3 < (seg1+seg2):
    if seg1 == seg2 == seg3:
        print ('Temos um triângulo EQUILÁTERO.')
    if seg1 == seg2 or seg2 == seg3 or seg1 == seg1:
        print ('Temos um triângulo ISÓSCELES.')
    if seg1 != seg2 != seg3:
        print('Temos um triângulo ESCALENO.')
else:
    print ('Os segmentos NÃO formam um triângulo.')