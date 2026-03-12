from datetime import date
dat = date.today().year
age = int(input('Em que ano você nasceu? '))
age2 = dat - age
if 15 <= age2 <= 19:
    print (f'Idade: \033[1;33m{age2} ANOS\033[1;33m\033[0;00m')
    print (f'Classificação: \033[1;33mJUNIOR\033[1;33m\033[0;00m')
elif age2 <= 9:
    print (f'Idade: \033[1;33m{age2} ANOS\033[1;33m\033[0;00m')
    print(f'Classificação: \033[1;33mMIRIM\033[1;33m\033[0;00m')
elif 18<= age2 <= 25:
    print (f'Idade: \033[1;33m{age2} ANOS\033[1;33m\033[0;00m')
    print(f'Classificação: \033[1;33mSÊNIOR\033[1;33m\033[0;00m')
elif 10 <= age2 <= 14:
    print (f'Idade: \033[1;33m{age2} ANOS\033[1;33m\033[0;00m')
    print(f'Classificação: \033[1;33mINFANTIL\033[1;33m\033[0;00m')
elif age2 > 25:
    print (f'Idade: \033[1;33m{age2} ANOS\033[1;33m\033[0;00m')
    print ('Classificação: \033[1;33mMASTER\033[1;33m\033[0;00m')