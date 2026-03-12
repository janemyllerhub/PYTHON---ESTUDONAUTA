#Crie um programa que leia vários números pelo teclado e mostre no final o somatório entre eles.
#Obs: O programa será interrompido quando o número 1111 for digitado
nun = 0
soma = 0
while nun != 1111:
    nun = int(input('Digite um número ou [1111] para encerrar o programa: '))
    nun = nun
    if nun != 1111:
        soma += nun
print (f'A soma total dos números digitados é igual a: {soma}')