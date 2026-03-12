fra = str(input('Digite uma frase: ')).upper().replace(" ", "")
va = fra[::-1]
print (f'A frase "{fra}" invertida fica "{va}"')
if fra == va:
    print ('A sua frase é um palíndromo!')
else:
    print('A sua frase NÃO é um palíndromo!')