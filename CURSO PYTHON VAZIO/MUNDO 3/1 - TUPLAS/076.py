print ('-'*40)
print ('           LISTAGEM DE PREÇOS')
print ('-'*40)
tupla = (('Lápis',1.75),
         ('Borracha',2.00),
        ('Caderno',15.90),
        ('Estojo',25.00),
        ('Transferidor',4.20),
        ('Compasso',9.99),
        ('Mochila',120.32),
        ('Canetas',22.30),
        ('Livro',34.90))
for item, preco in tupla:
    print (f'{item:.<30}R${preco:>7}')
print ('-'*40)