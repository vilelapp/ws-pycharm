from random import randint    # primeiro importamos as bilbliotecas

def insetionSort(A):
    # aqui sua função que já está ok
    pass

A=[]                          # define que A é uma lista vazia
for i in range(1,A + 1):       # laço que se repete de 1 a 1000
    print (A)              # imprime a lista gerada

insetionSort(A)               # chama a função para ordenar A

print (A)                     # imprime A ordenado
f = open('r_insertionsort.txt','w')
f.write (str(A))
f.write ('\n')
f.close()