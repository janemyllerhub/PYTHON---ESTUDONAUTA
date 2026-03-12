pilha = []
cont = 0
while cont == 0:
    expressao = str(input('Digite a sua expressão: '))
    cont = 0
    pilha = []
    for tri in expressao:
        if tri == '(':
            pilha.append('(')
        elif tri == ')':
            if len(pilha) > 0:
                pilha.pop()
                cont += 1
            else:
                pilha.append(tri)
            break
    if len(pilha) == 0:
        print ('Parabéns! A sua expressão está correta!')
    else:
        print ('A sua expressão não está correta, tente novamente...')