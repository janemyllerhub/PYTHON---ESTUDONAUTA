#Faça um algoritmo que leia a largura e altura de uma parede, calcule e mostre a área a ser pintada e a quantidade de tinta necessária para o serviço,
#sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
print ('=-='*20)
largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
print ('=-='*20)
area = largura * altura
litros = area / 2
print (f'Com uma área de {area:.2f}m, você ira precisar de {litros:.2f} litros de tinta para pintar toda a parede!')
print ('=-='*20)
