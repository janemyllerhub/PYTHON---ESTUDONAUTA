#O Índice de Massa Corpórea (IMC) é um valor calculado baseado na altura e no peso de uma pessoa. De acordo com o valor do IMC, podemos classificar o
#indivíduo dentro de certas faixas.
# abaixo que 18,5: Abaixo do peso
# entre 18,5 e 25: Peso ideal
# entre 25 e 30: Sobrepeso
# entre 30 e 40: Obesidade
# acima de 40: Obesidade mórbida

peso = float(input('Peso: '))
altura = float(input('Altura: '))
imc = peso / (altura**2)

if imc < 18.5:
    print ('Abaixo do peso')
if 18.5 < imc < 25:
    print ('Peso ideal')
if 25 < imc < 30:
    print ('Sobrepeso')
if 30 < imc < 40:
    print ('Obesidade')
if imc > 40:
    print ('Obesidade mórbida')