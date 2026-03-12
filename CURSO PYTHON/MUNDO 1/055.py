# [DESAFIO] Vamos melhorar o jogo que fizemos no exercício 32. A partir de agora, o computador vai sortear um número entre 1 e 10 e o jogador vai ter 4
#tentativas para tentar acertar.
import random
from random import randint
cont = 1
jogada = 0
computer = randint(1,10)
print ('Vou pensar em um número entre 1 e 10! Tente adivinhar qual é em 4 tentativas...')
while cont < 5 and jogada != computer:
        jogada = int(input(f'Qual a sua {cont}° jogada? '))
        jogada = jogada
        cont += 1
        if jogada == computer:
            print(f'''Parabens! Você ganhou...
Número escolhido pelo computador: {computer} 
Número escolhido pelo jogador: {jogada}''')
        else:
            print ('Tente novamente!')
if cont == 5 and jogada != computer:
    print ('4 Tentativas encerradas sem pontuação.')