#PRIMEIRA MANEIRA

soma = cont = quan = 0
lis = []

while True:
    if cont != 999:
        nun = int(input('Digite um número [999 para finalizar]: '))
        lis.append(nun)
        quan += 1
        if nun != 999:
            soma += nun
            cont = nun
        else:
            break
print(f'A soma dos {quan-1} números digitados é: {soma}')


#SEGUNDA MANEIRA (USAR NA AULA 15)

#lis = []
#quan = 0
#while True:
#    nun = int(input('Digite um número [999 para finalizar]: '))
#    if nun == 999:
#       break
#    lis.append(nun)
#    quan += 1
#print(f'A soma dos {quan-1} números digitados é: {sum(lis)}')