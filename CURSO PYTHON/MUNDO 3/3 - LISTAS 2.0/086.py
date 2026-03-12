lista = '[0,0]','[0,1]','[0,2]','[1,0]','[1,1]','[1,2]','[2,0]','[2,1]','[2,2]'
l = [],[],[],[],[],[],[],[],[]
for c in range (0,9):
    nun = str(input(f'Digite um valor para {lista[c]}: '))
    l[c].append(nun)
linha1 = f"[{str(l[0][0]):^5}] [{str(l[1][0]):^5}] [{str(l[2][0]):^5}]"
linha2 = f"[{str(l[3][0]):^5}] [{str(l[4][0]):^5}] [{str(l[5][0]):^5}]"
linha3 = f"[{str(l[6][0]):^5}] [{str(l[7][0]):^5}] [{str(l[8][0]):^5}]"
moldura = "-=-" * 15
print(moldura)
print(linha1.center(len(moldura)))
print(linha2.center(len(moldura)))
print(linha3.center(len(moldura)))
print(moldura)


