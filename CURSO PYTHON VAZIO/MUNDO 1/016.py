#[DESAFIO] Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dias e quantos anos ele
#já fumou. Considere que um fumante perde 10 min de vida a cada cigarro. Calcule quantos dias de vida um fumante perderá e exiba o total em dias.
cigarros = int(input('Quantos cigarros você fumava por dia? '))
anos = int(input('Por quantos anos você sustentou esse vício insalubre? '))

total_cigarros = cigarros*365*anos
tempo_perdido = total_cigarros * 10
dias = tempo_perdido / (60*24)

print (f'A quantidade de dias perdidos será de : {dias:.2f} dias.')
