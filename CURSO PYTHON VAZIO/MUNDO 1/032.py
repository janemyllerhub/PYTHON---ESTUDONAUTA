#[DESAFIO] Crie um jogo onde o computador vai sortear um número entre 1 e 5 o jogador vai tentar descobrir qual foi o valor sorteado.
from random import randint
computer = randint(1,5)
user = int(input('Vou pensar em número entre 1 e 5, você consegue adivinhar? '))
print ('=-='*16)
if user == computer:
    print ('Boa, você ACERTOU!')
if user != computer:
    print ('Que pena, você PERDEU.')
if user not in [1,2,3,4,5]:
    print ('Valor digitado incorretamente, programa finalizado.')
print ('=-='*16)
print (f'''Jogada do computador: {computer}
Jogada do usuário: {user}''')
print ('=-='*16)