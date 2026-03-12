import statistics
print ('=-='*20)
port = float(input('Escreva a sua nota de PORTUGUÊS: '))
mat = float(input('Escreva a sua nota de MATEMÁTICA: '))
cie = float(input('Escreva a sua nota de CIÊNCIAS: '))
his = float(input('Escreva a sua nota de HISTORIA: '))
geo = float(input('Escreva a sua nota de GEOGRAFIA: '))
lis = [port,mat,cie,his,geo]
media = statistics.median(lis)
print ('=-='*20)
if port < 5:
    print ('Você foi REPROVADO em PORTUGUÊS')
elif port == 5:
    print ('Você está de RECUPERAÇÃO em PORTUGUÊS')
elif port > 5:
    print ('Você foi APROVADO em PORTUGUÊS')
if mat < 5:
    print ('Você foi REPROVADO em MATEMÁTICA')
elif mat == 5:
    print ('Você está de RECUPERAÇÃO em MATEMÁTICA')
elif mat > 5:
    print ('Você foi APROVADO em MATEMÁTICA')
if cie < 5:
    print ('Você foi REPROVADO em CIÊNCIAS')
elif cie == 5:
    print ('Você está de RECUPERAÇÃO em CIÊNCIAS')
elif cie > 5:
    print ('Você foi APROVADO em CIÊNCIAS')
if his < 5:
    print ('Você foi REPROVADO em HISTORIA')
elif his == 5:
    print ('Você está de RECUPERAÇÃO em HISTORIA')
elif his > 5:
    print ('Você foi APROVADO em HISTORIA')
if geo < 5:
    print ('Você foi REPROVADO em GEOGRAFIA')
elif geo == 5:
    print ('Você está de RECUPERAÇÃO em GEOGRAFIA')
elif geo > 5:
    print ('Você foi APROVADO em GEOGRAFIA')
print ('=-='*20)
if media < 5:
    print (f'Sua média é de {media} e infelizmente você foi REPROVADO')
if media == 5:
    print (f'Sua média é de {media} e infelizmente você está de RECUPERAÇÃO')
if media > 5:
    print (f'Sua média é de {media} e você está APROVADO!!!')
print ('=-='*20)
#VOCE ESCREVE O SEU CODIGO AQUI E BOTA ELE PARA RODAR
