import random
"""
Cristiano Vilela – RA: 9312110861
Réder Augusto – RA: 9312110853
"""


def gerar_aleatorio():
    """Obtendo um valor aleatório entre 2 e 12."""
    return random.randint(2, 12)


def gerar_dados():
    """Recebe os dados do jogo."""
    dados = ''
    jogada = 0
    ponto = 0
    print('Digite sair para SAIR DO JOGO\n')
    return dados, jogada, ponto


def executar_jogo():
    """Recebe os dados e compara, executa o jogo."""
    dados, jogada, ponto = gerar_dados()

    while dados != 'sair':
        jogada += 1
        print(f'Jogada {jogada}')
        dados = input('Aperte ENTER para continuar: ')

        if dados == 'sair':
            print('Você saiu do jogo.')
        else:
            if jogada > 1:
                print(f'Seu ponto é {ponto}')
            valor = gerar_aleatorio()
            print(f'O valor do dado é {valor}\n')

            if jogada == 1:
                if valor == 7 or valor == 11:
                    print('NATURAL, PARABENS VOCÊ GANHOU!!!')
                    exit()
                elif valor == 2 or valor == 3 or valor == 12:
                    print('CRAPS, você perdeu!!!')
                    exit()
                else:
                    ponto = valor

            else:
                if valor == 7:
                    print('VOCÊ PERDEU!!! Tirou um 7 antes de repetir seu ponto.')
                    exit()
                elif ponto == valor:
                    print('PARABÉNS, você repetiu o seu ponto e GANHOU!!!')
                    exit()


def principal():
    """Função principal, chama a função que executa o jogo."""
    executar_jogo()


if __name__ == '__main__':
    principal()
