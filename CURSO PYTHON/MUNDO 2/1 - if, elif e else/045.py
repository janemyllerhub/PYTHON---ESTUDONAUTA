import random
import time

print('\033[0;33m=-=\033[0;33m\033[0;00m' * 80)
print('Vamos brincar de Pedra, Papel ou Tesoura? Escolha uma opção:')
print('\033[0;33m=-=\033[0;33m\033[0;00m' * 80)
print('[1] PEDRA')
print('[2] PAPEL')
print('[3] TESOURA')

jog1 = int(input('Qual é a sua jogada? '))
print('JO...')
time.sleep(0.7)
print('KEN...')
time.sleep(0.7)
print('PÔ!')
time.sleep(0.7)

lis = ['PEDRA', 'PAPEL', 'TESOURA']
lira = random.choice(lis)
jog = lis[jog1 - 1]

if lira == jog:
    print('\033[0;33m=-=\033[0;33m\033[0;00m' * 80)
    print(f'Computador jogou {lira} e você jogou {jog}.')
    print('\033[0;33m=-=\033[0;33m\033[0;00m' * 80)
    print('Vocês empataram!')
elif (jog == 'PEDRA' and lira == 'TESOURA') or \
     (jog == 'PAPEL' and lira == 'PEDRA') or \
     (jog == 'TESOURA' and lira == 'PAPEL'):
    print('\033[0;33m=-=\033[0;33m\033[0;00m' * 80)
    print(f'Computador jogou {lira} e você jogou {jog}.')
    print('\033[0;33m=-=\033[0;33m\033[0;00m' * 80)
    print('Parabéns!! Você venceu! 🎉')
else:
    print('\033[0;33m=-=\033[0;33m\033[0;00m' * 80)
    print(f'Computador jogou {lira} e você jogou {jog}.')
    print('\033[0;33m=-=\033[0;33m\033[0;00m' * 80)
    print('Você perdeu... 😢')