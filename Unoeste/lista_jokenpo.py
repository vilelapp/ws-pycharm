import random

jogadas = ['pedra', 'papel', 'tesoura']

def jogar(ultima_jogada=None):
    if ultima_jogada is None:
        return random.choice(jogadas)
    indice = jogadas.index(ultima_jogada) + 1
    return jogadas[indice % len(jogadas)]

print(jogar())
print(jogar('pedra'))
print(jogar('papel'))
print(jogar('tesoura'))
