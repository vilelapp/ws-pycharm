import random


def menu_opcoes():
    entrada_principal()
    opcao = int(input('1- JOGAR\n'
                      '2- SAIR\n'
                      'Selecione a opção: '))
    if opcao == 1:
        entrada_jogo()
    else:
        exit('FIM DE JOGO')


def entrada_principal():
    print('-' * 90)
    print('-' * 24, 'BEM-VINDO AO JOGO DA PALAVRA EMBARALHADA', '-' * 24)
    print('-' * 90)


def entrada_jogo():
    print('+' * 90)
    print('-' * 24, '  VOU SORTEAR UMA PALAVRA EMBARALHADA  ', '-' * 24)
    print('-' * 23, '  TENTE ACERTAR, VOCÊ TEM 6 CHANCES!!!  ', '-' * 23)
    print('+' * 90)
    executar_jogo()


def lista():
    lista_palavras = ['elefante', 'bola', 'peixe', 'futebol',
                      'basquete', 'gato', 'golfe', 'tesoura',
                      'colher', 'galinha', 'sapo', 'espirro',
                      'martelo', 'pinguim', 'chorar', 'piada',
                      'celular', 'cachorro', 'pato', 'cicatriz',
                      'cobertor', 'noiva', 'natal', 'notebook']
    sorteio = random.choice(lista_palavras)
    palavra = list(sorteio)
    return lista_palavras, sorteio, palavra


def executar_jogo():
    lista_palavras, sorteio, palavra = lista()

    random.shuffle(palavra)
    palavra = ''.join(palavra)
    chances = 6
    vezes = 1
    print(f'\nVOCÊ TEM 6 CHANCES. QUAL É A PALAVRA: "{palavra}"\n')

    while chances:
        vezes += 1
        chances += -1
        palavra_embaralhada = input('ESCREVA O NOME DA PALAVRA: ').lower()

        if palavra_embaralhada == sorteio:
            print(f'PARABÉNS!!! A PALAVRA É: {sorteio} \n')
            chances = 0

        if chances == 1:
            print('-' * 50)
            print('\nÚLTIMA CHANCE!!!\n')
            print('-' * 50)

        if chances > 1:
            print('-' * 50)
            print(f'\nCHANCE Nº {vezes}, PALAVRA INCORRETA, TENTE NOVAMENTE! \n')
            print('-' * 50)

        if vezes == 7:
            print('-' * 50)
            print('\nSUAS CHANCES ACABARAM, VOCÊ PERDEU!!!')
            exit('FIM DE JOGO')

        if palavra_embaralhada == sorteio and chances == 0:
            print('\nVOCÊ GANHOU!!!')
            exit('FIM DE JOGO')
