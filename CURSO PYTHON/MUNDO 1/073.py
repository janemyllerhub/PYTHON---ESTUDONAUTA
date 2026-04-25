#Crie um programa que preencha automaticamente (usando lógica, não apenas atribuindo diretamente) um vetor numérico com 10 posições, conforme abaixo:
vetor = []
cont = 9
for c in range (0,10):
    vetor.append(cont)
    cont -= 1
print (vetor, end='')