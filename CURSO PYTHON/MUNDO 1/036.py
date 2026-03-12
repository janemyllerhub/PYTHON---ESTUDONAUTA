#Um programa de vida saudável quer dar pontos de atividades físicas que podem ser trocados por dinheiro. O sistema funciona assim:
# Cada hora de atividade física no mês vale pontos
# até 10h de atividade no mês: ganha 2 pontos por hora
# de 10h até 20h de atividade no mês: ganha 5 pontos por hora
# acima de 20h de atividade no mês: ganha 10 pontos por hora
# A cada ponto ganho, o cliente fatura R$0,05

horas = int(input('Quantas horas você se exercitou este mês? '))
pontos = 0
if horas <= 10:
    pontos = horas * 2
if 10 < horas < 20:
    pontos = horas * 5
if horas > 20:
    pontos = horas * 10
print (f'Com {pontos} pontos você ganha R$ {pontos * 0.05:.2f} em dinheiro.')