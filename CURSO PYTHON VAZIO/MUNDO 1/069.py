#[DESAFIO] Desenvolva um programa que leia o primeiro termo e a razão de uma PA (Progressão Aritmética).
termo = int(input('Primeiro termo: '))
razao = int(input('Digite a razão: '))
cont = 0
while cont < 10:
    print (f'{termo}', end = '...' if cont != 9 else '!\n')
    termo += razao
    cont += 1


