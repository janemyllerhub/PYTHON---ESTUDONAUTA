#Desenvolva um programa que leia uma distância em metros e mostre os valores relativos em outras medidas.
#Ex:
#Digite uma distância em metros: 185.72
#A distância de 85.7m corresponde a:
#0.18572Km
#1.8572Hm
#18.572Dam
#1857.2dm
#18572.0cm
#185720.0mm

print ('=-='*20)
print ('                    CONVERSÃO DE MEDIDAS')
print ('=-='*20)
metros = float(input('Digite a distância em metros: '))
print (f'''A distância de {metros} m corresponde a:
{metros/1000} Km
{metros/100} Hm
{metros/10} Dam
{metros*10} dm
{metros*100} cm
{metros*1000} mm''')