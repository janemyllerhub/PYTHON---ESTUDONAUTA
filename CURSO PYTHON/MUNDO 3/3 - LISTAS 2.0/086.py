valores = [], [], [], [], [], [], [], [], []
sla = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
cont = 0
while cont < 9:
    for p in sla:
        nun = int(input(f'Digite um valor para {p}: '))
        valores[cont].append(nun)
        cont += 1
print(f'{print(*valores[0])}{print(*valores[1])}{print(*valores[2])}')