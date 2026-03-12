pesos = []
for nun in range (1,7):
    peso = float(input(f'Qual o peso da {nun}° pessoa: '))
    pesos.append(peso)
maiorpeso = max(pesos)
menorpeso = min(pesos)
print (f'A pessoa mais gorda do grupo tem {maiorpeso} kg e a pessoa mais magra do grupo tem {menorpeso} kg.')