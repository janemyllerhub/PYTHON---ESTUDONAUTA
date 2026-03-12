lista = []
for c in range (0,5):
        nun = int(input('Digite um valor: '))
        if nun > lista[4]:
            lista.pop(4)
            lista.insert(4, nun)
            print ('Adicionado ao final da lista')
            print(lista)
        elif nun < lista[1]:
            lista.pop(0)
            lista.insert(0, nun)
            print('Adicionado na posição 1 da lista')
            print (lista)


