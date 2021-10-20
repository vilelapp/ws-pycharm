amigo = {}
amigo['nome'] = 'Cristiane'
amigo['idade'] = 25
amigo['sexo'] = 'F'

print(amigo)
print(f'A professora', amigo['nome'], 'tem', amigo['idade'], 'anos')

amigo.update({'altura': '1.70', 'peso': 62})
print(amigo)

l_amigos = []
l_amigos.append(amigo)
amigo2 = {}
amigo2['nome'] = 'Aglaê'
amigo2['idade'] = 23
amigo2['sexo'] = 'F'
amigo2['altura'] = 1.6
amigo2['peso'] = 55

l_amigos.append(amigo2)
print(l_amigos)

for miga in l_amigos:
    print(f'A professora', miga['nome'], 'tem', miga['idade'], 'anos')
