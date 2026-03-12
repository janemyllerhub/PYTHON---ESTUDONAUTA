#Faça um programa usando a estrutura “faça enquanto” que leia a idade de várias pessoas. A cada laço, você deverá perguntar para o usuário se ele quer ou
#não continuar a digitar dados. No final, quando o usuário decidir parar, mostre na tela:
#a) Quantas idades foram digitadas
#b) Qual é a média entre as idades digitadas
#c) Quantas pessoas tem 21 anos ou mais.
continuacao = 'S'
cont = soma = maior_20 = 0
while continuacao == 'S':
    age = int(input('Idade: '))
    continuar = str(input('Deseja continuar [S/N]? ')).upper().strip()
    continuacao = continuar
    cont += 1
    soma += age
    if age >= 21:
        maior_20 += 1
print (f'''Foram digitadas um total de {cont} idades;
A média de todas as idade é igual a {soma / cont:.2f};
E temos {maior_20} pessoas com mais de 21 anos.''')