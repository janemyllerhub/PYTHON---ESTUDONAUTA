par_impar = [[],[]]
for c in range(0,7):
    nun = int(input(f'{c}° - Digite um número: '))
    if nun % 2 == 0:
        par_impar[0].append(nun)
    else:
        par_impar[1].append(nun)
print (f'''Números pares: {sorted(par_impar[0])}
Números impares: {sorted(par_impar[1])}''')