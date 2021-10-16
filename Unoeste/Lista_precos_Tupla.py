listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for item in range(0, len(listagem)):
    if item % 2 == 0:
        print(f'{listagem[item]:.<30}', end='')
    else:
        print(f'R${listagem[item]: >7.2f}')
print('-' * 40)

# impressão:
'''
----------------------------------------
           LISTAGEM DE PREÇOS           
----------------------------------------
Lápis.........................R$   1.75
Borracha......................R$   2.00
Caderno.......................R$  15.90
Estojo........................R$  25.00
Transferidor..................R$   4.20
Compasso......................R$   9.99
Mochila.......................R$ 120.32
Canetas.......................R$  22.30
Livro.........................R$  34.90
----------------------------------------
'''