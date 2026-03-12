lado1 = int(input('Qual o primeiro lado: '))
lado2 = int(input('Qual o segundo lado: '))
lado3 = int(input('Qual o terceiro lado: '))

if lado1 != lado2 and lado2 != lado3:
    print ('Temos um triângulo ESCALENO')
if lado1 == lado2 and lado3 != lado1 and lado2 or lado2 == lado3 and lado1 != lado2 and lado3 or lado1 == lado3 and lado2 != lado1 and lado3:
    print('Temos um triângulo ISÓSCELES')
if lado1 == lado2 and lado2 == lado3:
    print ('Temos um triângulo EQUILATERO')
