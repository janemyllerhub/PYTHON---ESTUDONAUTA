#Faça um algoritmo que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0.50 por km para
#viagens até 200Km e R$ 0.45 para viagens mais longas.

distancia = float(input('Qual distância você deseja percorrer? '))
if distancia <= 200:
    print (f'Percorrendo {distancia} km a passagem fica no valor de R$ {distancia * 0.50:.2f}')
else:
    print (f'Percorrendo {distancia} km a passagem fica no valor de R$ {distancia * 0.45:.2f}')
