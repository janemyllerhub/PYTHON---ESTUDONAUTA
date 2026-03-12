#Crie um programa que leia sexo e peso de 8 pessoas, usando a estrutura “para”. No final, mostre na tela:
#a) Quantas mulheres foram cadastradas
#b) Quantos homens pesam mais de 100Kg
#c) A média de peso entre as mulheres
#d) O maior peso entre os homens
cont = 1
mulheres = homens = 0
media = []
pes = []
while cont != 9:
    print('=-=' * 9)
    print (F'        {cont}° PESSOA')
    print ('=-='*9)
    sex = str(input('Sexo [F/M]: ')).upper().strip()
    peso = float(input('Peso: '))
    cont += 1
    if sex == 'F':
        mulheres += 1
        media.append(peso)
    else:
        pes.append(peso)
    if sex == 'M' and peso > 100:
        homens += 1
print (f'''Foram cadastradas {mulheres} mulheres e {homens} homens pesando mais de 100Kg;
A média de peso entre as mulheres é de {(sum(media)/mulheres):.2f}Kg e o maior peso entre os homens é de {max(pes):.2f}Kg.''')