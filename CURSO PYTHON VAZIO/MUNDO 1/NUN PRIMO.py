numero = 0
cont = numero
primo = divisivel = 0
continuacao = 'S'
while continuacao == 'S':
    nun = int(input('Digite um número: '))
    numero = nun
    cont = nun
    primo = divisivel = 0
    while cont != 0:
        if nun % nun == 0 and nun % cont != 0:
            primo += 1
        else:
            divisivel += 1
        cont -= 1
    if divisivel == 2:
        print (f'O número {nun} é primo!')
    else:
        print(f'O número {nun} NÃO é primo!')
    user = str(input('Deseja continuar [S/N]? ')).upper().strip()
    continuacao = user