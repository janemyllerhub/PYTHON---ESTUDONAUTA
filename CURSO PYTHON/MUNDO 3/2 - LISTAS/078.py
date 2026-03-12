numeros = []
posi_ma = 0
posi_me = 0
for c in range (1,6):
    nun = int(input('Digite um valor: '))
    numeros.append(nun)
maior = max(numeros)
menor = min(numeros)
for v,m in enumerate(numeros,start=1):
    if maior == m:
        posi_ma = v
    if menor == m:
        posi_me = v
print (f'O maior número digitado foi o {maior} que está na posição {posi_ma} '
       f'e o menor foi o {menor} que está na posição {posi_me} ')
