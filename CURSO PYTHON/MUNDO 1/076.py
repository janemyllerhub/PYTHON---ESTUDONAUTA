#Crie um programa que preencha automaticamente um vetor numérico com 7 números gerados aleatoriamente pelo computador e depois mostre os valores gerados na tela.
import random
vetor = []
for c in range (0,7):
    nun = random.randint(0,100)
    vetor.append(nun)
print (vetor, end='')