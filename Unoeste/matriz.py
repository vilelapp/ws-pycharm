lin = 3
col = 4
matriz = []

for l in range(lin):
    linMatriz = []
    for c in range(col):
        linMatriz.append((c+1)*l)
    matriz.append(linMatriz)
print(matriz)

matriz[0][1] = 9
for linMatriz in matriz:
    print(linMatriz)

print(matriz[1][2])
print(matriz[2][-1])

