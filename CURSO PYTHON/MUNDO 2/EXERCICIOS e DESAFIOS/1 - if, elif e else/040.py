print ('AGORA É A HORA DA VERDADE, PASSOU OU NÃO?')
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
if media > 7:
    print (f'Com as notas {n1} e {n2} a sua média é {media}')
    print (f'\033[1;33mPARABÉNS, VOCÊ FOI APROVADO!!!\033[1;33m\033[0;00m')
elif media < 5:
    print (f'Com as notas {n1} e {n2} a sua média é {media}')
    print ('\033[1;33mVOCÊ FOI REPROVADO :( \033[1;33m\033[0;00m')
elif 5.1 <= media <= 6.9:
    print (f'Com as notas {n1} e {n2} a sua média é {media}')
    print (f'\033[1;33mVOCÊ ESTÁ DE RECUPERAÇÃO :(\033[1;33m\033[0;00m')




