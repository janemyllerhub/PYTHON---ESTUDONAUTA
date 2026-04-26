#Faça um programa que leia 7 nomes de pessoas e guarde-os em um vetor. No final, mostre uma listagem com todos os nomes informados, na ordem inversa daquela em que eles foram informados.
vetor = []
cont = 1
for c in range (0,7):
    name = str(input('Digite o seu nome: ')).capitalize().strip()
    vetor.append(name)
print ('='*48)
print ('LISTAGEM DE PESSOAS CADASTRADAS'.center(48))
print ('='*48)
for d in range(0,7):
    print (f'{cont}:',vetor[-cont])
    cont += 1