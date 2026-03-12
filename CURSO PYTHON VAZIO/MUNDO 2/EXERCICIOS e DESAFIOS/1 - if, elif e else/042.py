one = int(input('Primeiro segmento: '))
two = int(input('Segundo segmento: '))
tre = int(input('Terceiro segmento: '))
form = one + two > tre and two + tre > one and one + tre > two
if form:
  if one == two == tre:
      print (f'Os segmentos {one}, {two} e {tre} formam um triangulo EQUILATERO!')
  if one == two or two == tre or one == tre:
      print (f'Os segmentos {one}, {two} e {tre} formam um triangulo ISÓSCELES!')
  if one != two != tre:
      print (f'Os segmentos {one}, {two} e {tre} formam um triangulo ESCALENO!')
elif one != form and two != form and tre != form:
    print (f'Os segmentos {one}, {two} e {tre} NÃO FORMAM um triangulo.')


