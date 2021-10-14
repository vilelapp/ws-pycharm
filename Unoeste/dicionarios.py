'''
lista = ['Arroz', 'Feijão', 'Massa', 'Açúcar', 'Sal']

i = 0
while i < len(lista):
    if lista[i] == 'Feijão':
        lista[1] = 'Lentilha'
    print(lista[i])
    i += 1

for item in lista:
    print(item)
'''

dicionario = {'123': 'Maurício', '125': 'Maria', '131': 'Manoela'}

print(dicionario.get('123'))

dicionario.update({'109': 'João', '144': 'Betânia'})

dicionario['125'] = 'Ana'
print(dicionario)

nome = dicionario.pop('141', 'Não encontrado para excluir')
print(nome) #Não existe a chave 141 para excluir
#Saída: Não encontrado para excluir
nome = dicionario.pop('142', 'Não encontrado para excluir')
print(dicionario) #Excluiu o Pedro
#Saída: {'123': 'Maurício', '125': 'Ana', '109': 'João',
# '144': 'Betânia'}

for chave in dicionario:
    print(chave, dicionario[chave], sep=' - ')

#As funções keys, values e items retornam, respectivamente,
# as chaves, os valores e as tuplas de cada elemento do dicionário.
print(dicionario.keys())
print(dicionario.values())
print(dicionario.items())
