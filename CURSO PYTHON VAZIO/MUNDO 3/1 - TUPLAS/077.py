print ('DETECTANDO VOGAIS'.center(33, '='))
print (f'{'-'*33}')
tupla = ('APRENDER',
         'PROGRAMAR',
         'LINGUAGEM',
         'PYTHON',
         'CURSO',
         'GRATIS',
         'ESTUDAR',
         'PRATICAR',
         'TRABALHAR',
         'MERCADO',
         'PROGRAMADOR',
         'FUTURO')
for itens in tupla:
    print (f'A palavra {itens} possui ', end = '')
    for letra in itens:
        if letra in 'AEIOU':
            print (f'{letra.lower()}',end = '')
    print (f'\n{'-'*33}')
print (f'{'='*33}')