times = (
    "Flamengo", "Palmeiras", "Santos", "Corinthians", "Grêmio", "Internacional",
    "São Paulo", "Vasco da Gama", "Botafogo", "Fluminense",
    "Atlético Mineiro", "Cruzeiro", "Bahia"
)
print ('=-='*70)
print (f'Lista de times brasileiros: {times}')
print ('=-='*70)
print (f'Os cinco primeiros são: {(times[:5])}')
print ('=-='*70)
print (f'Os quatro ultimos são: {(times[-4:])}')
print ('=-='*70)
print (f'Times em ordem alfabetica: {sorted(times)}')
print ('=-='*70)
print (f'O Flamengo está na {times.index('Flamengo')+1}° posição!')
print ('=-='*70)