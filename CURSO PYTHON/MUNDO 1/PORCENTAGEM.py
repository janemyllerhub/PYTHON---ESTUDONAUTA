produto = float(input('Qual o valor total dos produtos? R$  '))
taxa = (produto / 100) * 60
print (f'O valor dos produtos com a taxa ficam no total de: R$ {produto + taxa:.2f} sendo R$ {taxa:.2f} de taxa.')