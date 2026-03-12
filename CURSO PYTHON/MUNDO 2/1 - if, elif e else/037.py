n = int(input('Escreva um número: '))
print ('\033[34m[01]\033[34m\033[0;00m para \033[34mBINÁRIO\033[34m\033[0;00m')
print ('\033[0;34m[02]\033[0;34m\033[0;00m para \033[0;34mOCTAL\033[0;34m\033[0;00m')
print ('\033[0;34m[03]\033[0;34m\033[0;00m para \033[0;34mHEXAGONAL\033[0;34m\033[0;00m')
n2 = int(input('Como você deseja converte-lo? '))
if n2 == 1:
    print (f'O seu número inteiro convertido para binário fica: \033[0;34m{bin(n)}\033[0;34m\033[0;00m')
elif n2 == 2:
    print (f'O seu número inteiro convertido para octal fica: {oct(n)}')
elif n2 == 3:
    print (f'O seu número convertido para hexadecimal fica: {hex(n2)}')
