numero = 0,'zero',1,'um',2,'dois',3,'tres',4,'quatro',5,'cinco',6,'seis',7,'sete',8,'oito',9,'nove',10,'dez'
nun = int(input('Digite um número entre 1 e 10: '))
while nun > 10 or nun < 0:
    if nun > 10 or nun < 0:
        print('Errado! Tente novamente.')
        user = int(input('Digite um número entre 1 e 10: '))
        nun = user
    else:
        break
if nun < 10:
    posicao = numero.index(nun)
    print ('Você digitou o número',numero[posicao+1])
