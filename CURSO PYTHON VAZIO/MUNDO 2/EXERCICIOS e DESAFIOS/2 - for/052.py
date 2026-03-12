n = int(input('Digite um número: '))
total = 0
print ('\033[35m=\033[0m'*60)
print ('\033[35m  VAMOS IDENTIFICAR SE UM NÚMERO É PRIMO OU NÃO?\033[0m')
print ('\033[35m=\033[0m'*60)
print ('\033[33m[01]\033[0m Números divisiveis.')
print ('\033[31m[02]\033[0m Números \033[31mNÃO\033[0m divisiveis.')
print ('\033[35m=\033[0m'*60)
for c in range (1,n+1):
        if n % c == 0:
            total += 1
            print ('\033[33m', end = ' ')
        else:
            print('\033[31m', end=' ')
        print(f'{c}',end = ' ')
if total == 2:
    print (f'\n\033[0mO número {n} foi divisivel {total} vezes, portanto ele é um número primo.')
else:
    print (f'\n\033[0mO número {n} foi divisivel {total} vezes, portanto ele NÃO É um número primo.')