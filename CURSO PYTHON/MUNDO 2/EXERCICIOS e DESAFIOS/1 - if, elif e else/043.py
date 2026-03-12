alt = float(input('Sua altura: '))
pes = float(input('Seu peso: '))
form = pes / (alt **2)
if form < 18.5:
    print (F'Com um IMC de {form:.1f} você está ABAIXO DO PESO, vai uma proteina ai?')
elif 18.5 <= form <= 25:
    print (f'Parabens! Com um IMC de {form:.1f} você está no peso ideal!!!')
elif 25 <= form <= 30:
    print (f'Com um IMC de {form:.1f} você está com SOBREPESO e precisa procurar um nutricionista.')
elif 30 <= form <= 40:
    print (f'Com um IMC de {form:.1f} você está com OBESIDADE e precisa urgentemente de um medico.')
elif form > 40:
    print (f'Com um IMC de {form:.1f} você está com OBESIDADE MORBIDA, o número do SAMU é 190!')


