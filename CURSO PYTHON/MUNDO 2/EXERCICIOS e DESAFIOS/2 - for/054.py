maiorage = 0
menorage = 0
for nun in range (1,8):
    age = int(input(f'Qual a idade da {nun}° pessoa: '))
    if age >= 18:
        maiorage += 1
    else:
        menorage += 1
print (f'Temos {maiorage} adultos no grupo e {menorage} crianças.')