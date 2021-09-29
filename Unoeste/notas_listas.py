lista = []
qtde_nota = 10

for i in range(qtde_nota):
    nota = float(input('Digite a nota: '))
    lista.append(nota)

for i in range(qtde_nota):
    print('nota[', i, '] = ', lista[i], sep='')

print(f'A maior nota é {max(lista)} e a menor nota é {min(lista)}')
