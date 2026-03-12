mon = float(input('Qual o valor da casa? '))
sal = float(input('Qual seria o seu sálario mensal? '))
anos = int(input('Em quantos anos voce pretende comprar? '))
cal = mon // (anos * 12)
cal2 = (sal // 100)*30
print (f'Voce precisara pagar R$ {cal:.2f} por mês para conseguir conquistar a sua moradia em {anos} anos.')
if cal > cal2:
    print (f'\033[1;40mEmprestimo negado devido ultrapassar 30% do seu sálario mensal.\033[1;40m\033[0;00m')
elif cal < cal2:
    print (f'\033[1;40mEmprestimo aprovado, parabéns!!!!\033[1;40m\033[0;00m')