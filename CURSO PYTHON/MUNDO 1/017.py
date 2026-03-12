#Escreva um programa que pergunte a velocidade de um carro. Caso ultrapasse 80Km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba
#o valor da multa, cobrando R$5 por cada km acima da velocidade permitida.
velocidade = int(input('Velocidade do carro: '))

if velocidade > 80:
    print(f'Você foi MULTADO por passar do limite de velocidade e tera que pagar R$ {(velocidade - 80) * 5:.2f}')
if velocidade <= 80:
    print(f'Parabéns, com uma velocidade de {velocidade} KMs infelizmente não poderemos lhe multar, mas continue assim!.')
