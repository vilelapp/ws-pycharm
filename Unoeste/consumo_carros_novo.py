listaCarros = []
listaConsumo = []

distancia = 600
gasolina = 3.80

for i in range(0, 3):
    carros = input(f'Digite o nome do carro {i + 1}: ')
    kmLitro = int(input(f'Digite o consumo do carro {i + 1} (Km por litro): '))
    listaCarros.append(carros)
    listaConsumo.append(kmLitro)

for y in range(0, 3):
    consumo = int(distancia / listaConsumo[y])
    custoDistancia = consumo * gasolina
    print(f'{listaCarros[y].upper()} - {listaConsumo[y]} km/litro - {consumo} litros - R$ {custoDistancia:.2f}')
