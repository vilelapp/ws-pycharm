produtos = {
    123: 'Camisa estampada',
    124: 'Camisa social manga longa',
    125: 'Calça jeans'
}

venda = [
    (123, 3, 25.55),
    (124, 2, 79.99),
    (125, 1, 99.99)
]

item = 0
valor_total = 0
print('-' * 46)
print('C U P O M  F I S C A L'.center(46, ' '))
print('ITEM CÓDIGO DESCRIÇÃO QTD.UN.VL_UNIT(R$) ST VL')
print('-' * 46)

for indice in range(0, len(venda)):
    subtotal = 0
    item += 1
    produto = produtos.get(venda[indice][0])
    quantidade = venda[indice][1]
    valor = venda[indice][2]
    subtotal += quantidade * valor
    valor_total += subtotal
    print(f'{str(item).ljust(4)}'
          f'{venda[indice][0]}'
          f'{produto.rjust(37)}')

    print(f'{str(quantidade).rjust(11)}UN X '
          f'{str(valor).ljust(6)}'
          f'{str(subtotal).rjust(23)}')

print('-' * 46)
print('TOTAL R$', str(valor_total).rjust(36))

''' 
----------------------------------------------
            C U P O M  F I S C A L            
ITEM CÓDIGO DESCRIÇÃO QTD.UN.VL_UNIT(R$) ST VL
----------------------------------------------
1   123                     Camisa estampada
          3UN X 25.55                   76.65
2   124            Camisa social manga longa
          2UN X 79.99                  159.98
3   125                          Calça jeans
          1UN X 99.99                   99.99
----------------------------------------------
TOTAL R$                               336.62
'''