#Desenvolva um aplicativo que leia o salário e o sexo de vários funcionários. No final, mostre o total de salários pagos aos homens e o total pago às
#mulheres. O programa vai perguntar ao usuário se ele quer continuar ou não sempre que ler os dados de um funcionário.
total_homens = total_mulheres = 0
continuacao = 'S'
sex = ''
while continuacao == 'S':
    salario = int(input('Salário: R$ '))
    sex = str(input('Sexo [F/M]: ')).strip().upper()
    continuar = str(input('Deseja continuar [S/N]? ')).strip().upper()
    continuacao = continuar
    if sex == 'F':
        total_mulheres += salario
    else:
        total_homens += salario
print (f'''Total de salários pagos aos homens: R$ {total_homens}
Total de salários pagos as mulheres: R$ {total_mulheres}''')
