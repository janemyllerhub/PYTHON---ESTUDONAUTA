#Numa promoção exclusiva para o Dia da Mulher, uma loja quer dar descontos para todos, mas especialmente para mulheres. Faça um programa que leia nome,
#sexo e o valor das compras do cliente e calcule o preço com desconto. Sabendo que:
#Homens ganham 5% de desconto
#Mulheres ganham 13% de desconto

nome = str(input('Qual o seu nome? ')).capitalize()
sexo = str(input('Mulher ou Homem [F/M]? ')).upper()
valor = float(input('Qual seria o valor total da sua compra? '))
desconto_h = valor / 100 * 5
desconto_f = valor / 100 * 13
if sexo == 'F':
    print (f'Parabens, {nome}! Nesse dia especial do dias das mulheres você ganha um desconto de 13% em suas compras e a sua compra que valia R$ {valor:.2f} passa a valer agora R$ {valor - desconto_f:.2f}!!!!')
elif sexo == 'M':
    print (f'Opa, {nome}. Como você é um homem lhe daremos um descontinho mixuruca de 5% e a sua compra que valia R$ {valor:.2f} vai passar a valer R$ {valor - desconto_h:.2f}')
else:
    print ('Sexo escrito de maneira incorreta, sem desconto!')