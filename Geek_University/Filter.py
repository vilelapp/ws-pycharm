import statistics

# Dados coletados de um sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Modo simples
media = (sum(dados) / len(dados))
print(media)

# Calculando média utilizando a função mean()
media = statistics.mean(dados)
print(media)

# Filter
res = filter(lambda x: x > media, dados)
print(list(res))

# Dados vazios
paises = ['', 'Argentina', '', 'Brasil', '', 'Chile', '', 'Colombia', 'Equador']
print(paises)

res = filter(None, paises)
print(list(res))

# Exemplo mais complexo
usuarios = [
    {'username': 'Samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {'username': 'Carla', 'tweets': ['Eu amo meu gato']},
    {'username': 'Jeff', 'tweets': []},
    {'username': 'Bob123', 'tweets': []},
    {'username': 'doggo', 'tweets': ['Eu gosto de cachorros', 'Vou sair hoje']},
    {'username': 'gal', 'tweets': []}
]

# Filtrar usuários inativos no Twitter

# Forma 1
inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))
print(inativos)

# Forma 2
inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))
print(inativos)

# Combinar filter() e map()
nomes = ['Vanessa', 'Ana', 'Maria']
# Criar uma lista contendo 'Sua instrutora é' + nome, desde que cada nome tenha menos de 5 caracteres
lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))
print(lista)
