continuar = 'S'
homens = mulheres = 0
cont = 1
print ('=-='*9)
print ('    CADASTRO DE PESSOAS')
while continuar == 'S':
    print('=-=' * 9)
    print(F'        {cont}° PESSOA')
    print('=-=' * 9)
    age = int(input('Idade: '))
    sex = str(input('Sexo [F/M]: ')).strip().upper()
    cabelo = int(input('''[1] Preto
[2] Castanho
[3] Loiro
[4] Ruivo
Cor do cabelo: '''))
    continuacao = str(input('Deseja continuar [S/N]? ')).upper().strip()
    continuar = continuacao
    cont += 1
    if sex == 'M' and age > 18 and cabelo == 2:
        homens += 1
    if sex == 'F' and 25 < age < 30 and cabelo == 3:
        mulheres += 1
if homens > 1 and mulheres > 1:
    print(f"Temos {homens} homens com mais de 18 anos e cabelo castanho e "
          f"{mulheres} mulheres entre 25 e 30 anos com o cabelo loiro.")
elif homens > 1 and mulheres == 0:
    print(f"Temos {homens} homens com mais de 18 anos e cabelo castanho e "
          "nenhuma mulher entre 25 e 30 anos com o cabelo loiro.")
elif mulheres > 1 and homens == 0:
    print(f"Temos {mulheres} mulheres entre 25 e 30 anos com o cabelo loiro e "
          "nenhum homem com mais de 18 anos e cabelo castanho.")
elif homens == 1 and mulheres == 1:
    print("Temos um homem com mais de 18 anos e cabelo castanho e "
          "uma mulher entre 25 e 30 anos com o cabelo loiro.")
elif homens == 1 and mulheres == 0:
    print("Temos um homem com mais de 18 anos e cabelo castanho e "
          "nenhuma mulher entre 25 e 30 anos com o cabelo loiro.")
elif mulheres == 1 and homens == 0:
    print("Temos uma mulher entre 25 e 30 anos com o cabelo loiro e "
          "nenhum homem com mais de 18 anos e cabelo castanho.")
print('=-=' * 9)