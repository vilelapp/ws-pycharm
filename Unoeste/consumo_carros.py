lista_Carro = [None] * 3
lista_Distancia = [None] * 3
lista_Consumo = [None] * 3
lista_Custo = [None] * 3

preco_Gasolina = 3.80
distancia = 600

for i in range(0, 3):
    print(f'Digite o nome do carro {i + 1}: ')
    lista_Carro[i] = input()

for x in range(0, 3):
    print(f'Digite o consumo carro {x + 1} (km por litro): ')
    lista_Consumo[x] = float(input())
    lista_Distancia[x] = distancia / lista_Consumo[x]
    lista_Custo[x] = lista_Distancia[x] * preco_Gasolina

for y in range(0, 3):
    print(f'Carro {y + 1}')
    print(f'Nome: {lista_Carro[y]}')
    print(f'Km por litro: {lista_Consumo[y]}')
    print()

for z in range(0, 3):
    print(f'{z+1} - {lista_Carro[z]} - {lista_Consumo[z]} - {(lista_Distancia[z])} litros - '
          f'R$ {(lista_Custo[z])}\n')
