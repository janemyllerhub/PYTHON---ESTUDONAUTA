#[DESAFIO] Crie um jogo de JoKenPo (Pedra-Papel-Tesoura)
import random
import time
print ('=-='*15)
print ('           PEDRA, PAPEL ou TESOURA')
print ('=-='*15)
itens = ['PEDRA', 'PAPEL','TESOURA']
computer = random.choice(itens)
user = int(input('''[1] PEDRA
[2] PAPEL
[3] TESOURA
Sua jogada: '''))
print ('=-='*15)
print ('JO')
time.sleep(0.5)
print ('KEN')
time.sleep(0.5)
print ('PO')
time.sleep(0.5)
print ('=-='*15)
print (f'Jogada do computador: {computer}')
if user == 1:
    print ('Jogada do usuário: PEDRA')
if user == 2:
    print ('Jogada do usuário: PAPEL')
if user == 3:
    print ('Jogada do usuário: TESOURA')
print ('=-='*15)
if computer == 'PEDRA' and user == 2 or computer == 'PAPEL' and user == 3 or computer == 'TESOURA' and user == 1:
    print ('Parabéns, você GANHOU!')
elif computer == 'PEDRA' and user == 1 or computer == 'PAPEL' and user == 2 or computer == 'TESOURA' and user == 3:
    print ('Vocês estão EMPATADOS.')
elif computer == 'PEDRA' and user == 3 or computer == 'PAPEL' and user == 1 or computer == 'TESOURA' and user == 2:
    print ('Você PERDEU.')
else:
    print ('Escolha do usuário digitada incorretamente, programa finalizado!')
print ('=-='*15)