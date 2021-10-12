import math

def area(r):
    """Calcula a área de um círculo com raio 'r'. """
    return math.pi * (r ** 2)

print(area(2))
print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]

# Forma 1 - comum
areas = []
for r in raios:
    areas.append((area(r)))

print(areas)

# Forma 2 - Map
areas = map(area, raios)
print(list(areas))

# Forma 3 - Map com lambda
print(list(map(lambda r: math.pi * (r ** 2), raios)))

# Exemplo
cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27)]

# Conveter celsius para fahrenheit
c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)

print(list(map(c_para_f, cidades)))
