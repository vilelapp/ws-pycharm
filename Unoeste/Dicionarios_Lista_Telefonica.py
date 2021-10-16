lista_telefonica = {}

def incluir(nome, numero):
    lista_telefonica[nome] = numero

def excluir(nome):
    resp = lista_telefonica.pop(nome, 'Erro')
    if resp == 'Erro':
        return f'{nome} não pode ser excluido.'
    else:
        return f'{nome} excluído com sucesso'

def pesquisar(nome):
    if nome in lista_telefonica:
        return f'O número de {nome} é {lista_telefonica[nome]}'
    else:
        return f'{nome} não encontrado na lista.'

incluir('Mauricio', 997654321)
incluir('Marcelo', 987654321)
incluir('Matheus', 999654321)
print(lista_telefonica)
print(excluir('Mario'))
print(excluir('Matheus'))
print(pesquisar('Mauricio'))
print(pesquisar('Mauro'))
print(lista_telefonica)
