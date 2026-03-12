#Faça um programa que leia a largura e o comprimento de um terreno retangular, calculando e mostrando a sua área em m². O programa também
#deve mostrar a classificação desse terreno, de acordo com a lista abaixo:
# Abaixo de 100m² = TERRENO POPULAR
# Entre 100m² e 500m² = TERRENO MASTER
# Acima de 500m² = TERRENO

largura = float(input('Largura do terreno: '))
comprimento = float(input('Comprimento do terreno: '))
area = largura*comprimento
if area < 100:
    print (f'Com uma área de {area:.0f}m² o seu terreno é classificado como POPULAR')
if 100 < area < 500:
    print (f'Com uma área de {area:.0f}m² o seu terreno é classificado como MASTER')
if area > 500:
    print (f'Com uma área de {area:.0f}m² o seu terreno é classificado como TERRENO')
