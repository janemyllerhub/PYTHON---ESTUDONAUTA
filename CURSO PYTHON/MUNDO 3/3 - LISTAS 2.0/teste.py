lista_primaria = list()
for c in range(1,3):
    nome = str(input('Digite o seu nome: '))
    idade = int(input('Digite a sua idade: '))
    lista_primaria.append((nome, idade))
for p in lista_primaria:
    print(f'Nome: {p[0]} --- {p[1]}')