sex = ''
while sex != 'F' and sex != 'M':
    sex = str(input('Digite o seu sexo (F/M): ')).upper()
    if sex not in ['F', 'M']:
        print ('Sexo não identificado, por favor, digite corretamente.')
if sex == 'F':
    print ('Sexo feminino registrado com sucesso!')
if sex == 'M':
    print('Sexo masculino registrado com sucesso!')