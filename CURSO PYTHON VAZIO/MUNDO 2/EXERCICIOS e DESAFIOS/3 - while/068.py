from random import randint

print('\033[034m=-=\033[034m\033[0m' * 20)
print ('                        PAR ou ÍMPAR')
print('\033[034m=-=\033[034m\033[0m' * 20)

cont = 0

while True:
    computer = randint(0, 10)
    nun = int(input('Qual o número? '))
    ip = str(input('Par ou Ímpar [P/I]? ')).upper()
    if ip not in ['P','I']:
        print("Entrada inválida! Digite apenas P ou I.")
        continue
    if (nun + computer) % 2 != 0 and ip == "P" or (nun + computer) % 2 == 0 and ip == "I":
        if cont < 1:
            print('\033[034m=-=\033[034m\033[0m' * 20)
            print('GAMER OVER')
            print(F'Você não ganhou nenhuma vez do computador :(')
            print('\033[034m=-=\033[034m\033[0m' * 20)
        if cont == 1:
            print('\033[034m=-=\033[034m\033[0m' * 20)
            print('GAMER OVER')
            print(F'Você ganhou {cont} vez do computador!')
            print('\033[034m=-=\033[034m\033[0m' * 20)
        if cont > 1:
            print('\033[034m=-=\033[034m\033[0m' * 20)
            print('GAMER OVER')
            print(F'Você ganhou {cont} vezes do computador!')
            print('\033[034m=-=\033[034m\033[0m' * 20)
            print(f'Número do jogador: {nun}, jogada: {ip}')
            print('\033[034m=-=\033[034m\033[0m' * 20)
        if ip == "I":
            print(f'Número do COMPUTADOR: {computer}, jogada: P')
            print('\033[034m=-=\033[034m\033[0m' * 20)
        else:
            print(f'Número do COMPUTADOR: {computer}, jogada: I')
            print('\033[034m=-=\033[034m\033[0m' * 20)
        break
    cont += 1
    print('''Você VENCEU!
Vamos tentar novamente...''')
    print('\033[034m=-=\033[034m\033[0m' * 20)
    print(f'Número do jogador: {nun}, jogada: {ip}')
    print('\033[034m=-=\033[034m\033[0m' * 20)
    if ip == "I":
        print(f'Número do COMPUTADOR: {computer}, jogada: P')
        print('\033[034m=-=\033[034m\033[0m' * 20)
    else:
        print(f'Número do COMPUTADOR: {computer}, jogada: I')
        print('\033[034m=-=\033[034m\033[0m' * 20)