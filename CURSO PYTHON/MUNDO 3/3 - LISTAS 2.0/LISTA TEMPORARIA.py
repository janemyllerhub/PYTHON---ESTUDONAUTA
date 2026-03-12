galera = list()
dado = list() #lista temporária que só recebe dados enquanto tiver pessoas para cadastrar
pessoas = 'S'
print ('=-='*15)
while pessoas == 'S':
    dado.append(str(input('Nome: ')).capitalize().strip()) #manda os nomes para o dado
    dado.append(int(input('Idade: '))) #manda as idades para o dado
    pessoas = str(input('Ainda tem pessoas para cadastrar? ')).upper().strip()
    galera.append(dado[:]) #manda os dados armazenados em dado para a variável galera, temporariamente devido o [:]
    dado.clear()
print ('=-='*15)
print (f'{"PESSOAS CADASTRADAS":^45}') #pode usar um .center(45) para centralizar também
print ('=-='*15)
n = 1
for p in galera:
    print (f'{n}° pessoa: {p[0]} com {p[1]} anos de idade.')
    n += 1
print ('=-='*15)