print ('=-='*16)
print ('                 CAÚCULO IMC')
print ('=-='*16)

peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))
imc = peso / (altura ** 2)
if imc < 18.5: # IMC abaixo de 18.5
    print (f'''Com um IMC de {imc:.2f} a sua classificação é \033[034mMAGREZA:\033[034m\033[0m
Aumentado para doenças relacionadas à \033[034mDESNUTRIÇÃO.\033[034m\033[0m''')
if 18.5 < imc <= 24.9: # IMC é maior que 18.5 e ao mesmo tempo é menor ou igual a que 24.9
    print (f'''Com um IMC de {imc:.2f} a sua classificação é \033[034mPESO NORMAL:\033[034m\033[0m
\033[034mBAIXO \033[034m\033[0mrisco.''')
if 25.0 < imc <= 29.9:
    print (f'''Com um IMC de {imc:.2f} a sua classificação é \033[034mSOBREPESO:\033[034m\033[0m
Risco aumentado para \033[034mDOENÇAS CRÔNICAS.\033[034m\033[0m''')
if 30.0 < imc <= 34.9:
    print (f'''Com um IMC de {imc:.2f} a sua classificação é \033[034mOBESIDADE GRAU I:\033[034m\033[0m
Risco \033[034mMODERADO.\033[034m\033[0m''')
if 35.0 < imc <= 39.9:
    print (f'''Com um IMC de {imc:.2f} a sua classificação é \033[034mOBESIDADE GRAU II:\033[034m\033[0m
Risco \033[034mALTO.\033[034m\033[0m''')
if imc >= 40: # IMC acima ou igual a 40
    print (f'''Com um IMC de {imc:.2f} a sua classificação é \033[034mOBESIDADE GRAU III:\033[034m\033[0m
Risco \033[034mMUITO ALTO.\033[034m\033[0m''')