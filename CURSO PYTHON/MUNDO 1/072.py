# Crie um programa que preencha automaticamente (usando lógica, não apenas atribuindo diretamente) um vetor numérico com 10 posições, conforme abaixo:

vetor = []
cont = -5
for c in range (0,10):
    cont += 5
    vetor.append(cont+5)
print (vetor, end = '')