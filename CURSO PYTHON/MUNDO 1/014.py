#A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
#quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar, sabendo que o carro custa R$90 por dia e R$0,20 por Km rodado.
km = float(input('Quantos KMs o carro percorreu? '))
dias = int(input('Por quantos dias o carro esteve alugado? '))
print (f'O valor total a ser cobrado será R$ {dias * 90 + km * 0.20:.2f} sendo R$ {dias * 90:.2f} das diárias alugadas + R$ {km * 0.20:.2f} pelos KMs rodados.')