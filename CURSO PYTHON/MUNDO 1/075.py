#Crie um programa que preencha automaticamente (usando lógica, não apenas atribuindo diretamente) um vetor numérico com 15 posições com os primeiros
#elementos da sequência de Fibonacci:
a = 1
b = 1
c = a+b
vetor = [a,b,c]
for i in range (0,13):
    a = b
    b = c
    c = a+b
    vetor.append(c)
print (vetor, end = '')