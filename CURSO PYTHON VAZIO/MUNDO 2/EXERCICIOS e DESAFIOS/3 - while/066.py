soma = nun = quan = 0
lis = []

while True:
    nun = int(input('Digite um número [999 para finalizar]: '))
    if nun != 999:
        lis.append(nun)
        soma += nun
        quan += 1
    else:
        break
print(f'A soma dos {quan} números digitados é: {soma}')

#SEGUNDA MANEIRA

#lis = []
#while True:
#    nun = int(input('Digite um número [999 para finalizar]: '))
#    if nun == 999:
#       break
#    lis.append(nun)
#print(f'A soma dos {len(lis)} números digitados é: {sum(lis)}')
