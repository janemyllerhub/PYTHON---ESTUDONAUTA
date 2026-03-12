#Crie um programa usando a estrutura “faça enquanto” que leia vários números. A cada laço, pergunte se o usuário
#quer continuar ou não. No final, mostre na tela:
#a) O somatório entre todos os valores
#b) Qual foi o menor valor digitado
#c) A média entre todos os valores
#d) Quantos valores são pares
continuacao = 'S'
soma = cont = pares = 0
lista = []
valores = []
while continuacao == 'S':
    nun = int(input('Digite um número: '))
    continuar = str(input('Deseja continuar? ')).upper().strip()
    continuacao = continuar
    soma += nun
    cont += 1
    lista.append(nun)
    if nun % 2 == 0:
        pares += 1
        valores.append(nun)
print (f'''O somatório de todos os valores é igual a: {soma};
O menor valor digitado: {min(lista)};
A média dos valores digitados: {soma / cont:.2f};
Temos {pares} valores pares é são:
{valores}''')