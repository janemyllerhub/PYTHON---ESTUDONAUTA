continu = 'S'
valores = []
while continu == 'S':
    valor = int(input('Digite um valor: '))
    if valor in valores:
        print('Valor duplicado! Não adicionado.')
    else:
        print('Valor digitado com sucesso...')
        valores.append(valor)
    cont = str(input('Deseja continuar [S/N]? ')).upper()
    continu = cont
valores.sort()
print (f'Você digitou os valores {valores}')


