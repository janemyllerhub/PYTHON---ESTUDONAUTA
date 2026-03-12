print('\033[034m==\033[034m\033[0m' * 18)
print ('       VAMOS ATRAVESSAR A RUA?')
print('\033[034m==\033[034m\033[0m' * 18)

print ('Olhe para o lado ESQUERDO e para o lado DIREITO da rua!')
car = str(input('Está vindo carro de algum dos lados [S/N]? ')).upper().strip()

if car == 'N':
    print (f'Considerando que você olhou para os lados e NÃO ESTÁ vindo carro algum:')
    print ('É seguro atravessar a rua!')
    print ('ATRAVESSANDO...')
    print ('Parabéns, rua atravessada!')
else:
    print(f'Considerando que você olhou para os lados e ESTÁ vindo carro de um dos lados:')
    print('Espere o carro atravessar a rua para a sua segurança!')