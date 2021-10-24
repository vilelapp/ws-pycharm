import random

fila_um = random.sample(range(1, 30), 20)
fila_dois = random.sample(range(1, 30), 20)
# Ordena filas
fila_um.sort(reverse=False)
fila_dois.sort(reverse=False)

sobrepoe = [i for i in set(fila_um) if i in fila_dois]
fila_final = []

for i in sobrepoe:
    if i not in fila_final:
        fila_final.append(i)

# Imprime as filas

print('Fila um: ', fila_um)
print('Fila dois: ', fila_dois)
print('Números repetidos: ', fila_final)

'''
RESULTADO:

Fila um:  [1, 3, 4, 5, 6, 7, 10, 12, 13, 15, 17, 18, 21, 22, 23, 25, 26, 27, 28, 29]
Fila dois:  [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 17, 21, 22, 23, 24, 25, 26, 28, 29]
Números repetidos:  [1, 4, 5, 6, 7, 10, 12, 17, 21, 22, 23, 25, 26, 28, 29]

'''
