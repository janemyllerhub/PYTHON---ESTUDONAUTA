#Crie um programa que preencha automaticamente (usando lógica, não apenas atribuindo diretamente) um vetor numérico com 10 posições, conforme abaixo:
vetor = []
for c in range (0,10):
    if len(vetor) % 2 == 0:
        vetor.append(5)
    else:
        vetor.append(3)
print (vetor, end = '')