#Escreva um programa para aprovar ou não o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e
#em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

casa = int(input('Valor da casa: '))
salario = int(input('Salário atual: '))
anos = int(input('Em quantos anos você pretende pagar? '))

mensalidade = casa / (anos * 12)
media = (salario / 100) * 30

if anos > 1:
    print (f'O valor da mensalidades divididas em {anos} anos ({anos * 12} meses) fica R$ {mensalidade:.2f}/mês')
if anos == 1:
    print (f'O valor da mensalidades divididas em {anos} ano ({anos * 12} meses) fica R$ {mensalidade:.2f}/mês')
if mensalidade > media:
    print ('Empréstimo NEGADO')
if mensalidade <= media:
    print ('Empréstimo ACEITO')