# import random
#
#
# # Jogo de Craps. Faca um programa de implemente um jogo de Craps. O jogador
# # lanca um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada,
# # voce tirar 7 ou 11, voce tirou um "natural" e ganhou. Se voce tirar 2, 3 ou
# # 12 na primeira jogada, isto e chamado de "craps" e voce perdeu. Se, na
# # primeira jogada, voce fez um 4, 5, 6, 8, 9 ou 10,este e seu "Ponto". Seu
# # objetivo agora e continuar jogando os dados ate tirar este numero novamente.
# # Voce perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
# # Dica: para simular o lancamento do dado, utilize o metodos Random do Python.!
#
#
# def obter_valor_aleatorio():
#     return random.randint(2, 12)
#
#
# dados = ''
# jogada = 0
# ponto = 0
# print('Digite sair para SAIR DO JOGO\n'
#       'ou aperte ENTER para GERAR OS DADOS: ')
#
# while dados != 'sair':
#     jogada += 1
#     print(f'Jogada {jogada}')
#     dados = input('Escolha a ação: ')
#
#     if dados == 'sair':
#         print('Você saiu do jogo.')
#     else:
#         if jogada > 1:
#             print(f'Seu ponto é {ponto}')
#         valor = obter_valor_aleatorio()
#         print(f'O valor do dado é {valor}\n')
#         if jogada == 1:
#             if valor == 7 or valor == 11:
#                 print('NATURAL, PARABENS VOCÊ GANHOU!!!')
#                 exit()
#             elif valor == 2 or valor == 3 or valor == 12:
#                 print('CRAPS, você perdeu!!!')
#                 exit()
#             else:
#                 ponto = valor
#         else:
#             if valor == 7:
#                 print('VOCÊ PERDEU!!! Tirou um 7 antes de repetir seu ponto.')
#                 exit()
#             elif ponto == valor:
#                 print('PARABÉNS, conseguiu repetir seu ponto e GANHOU!!!')
#                 exit()

"""outra"""
# import random
#
# """
# Cristiano Vilela – RA: 9312110861
# Réder Augusto – RA: 9312110853
# """
#
#
# def valor_aleatorio():
#     """Obtendo um valor aleatório entre 2 e 12."""
#     return random.randint(2, 12)
#
#
# def dados_jogo():
#     """Recebe os dados do jogo."""
#     dados = ''
#     jogada = 0
#     ponto = 0
#     print('Digite sair para SAIR DO JOGO\n')
#     return dados, jogada, ponto
#
#
# def jogo():
#     """Recebe os dados e compara, executa o jogo."""
#     dados, jogada, ponto = dados_jogo()
#
#     while dados != 'sair':
#         jogada += 1
#         print(f'Jogada {jogada}')
#         dados = input('Aperte ENTER para continuar: ')
#
#         if dados == 'sair':
#             print('Você saiu do jogo.')
#         else:
#             if jogada > 1:
#                 print(f'Seu ponto é {ponto}')
#             valor = valor_aleatorio()
#             print(f'O valor do dado é {valor}\n')
#
#             if jogada == 1:
#                 if valor == 7 or valor == 11:
#                     print('NATURAL, PARABENS VOCÊ GANHOU!!!')
#                     exit()
#                 elif valor == 2 or valor == 3 or valor == 12:
#                     print('CRAPS, você perdeu!!!')
#                     exit()
#                 else:
#                     ponto = valor
#
#             else:
#                 if valor == 7:
#                     print('VOCÊ PERDEU!!! Tirou um 7 antes de repetir seu ponto.')
#                     exit()
#                 elif ponto == valor:
#                     print('PARABÉNS, conseguiu repetir seu ponto e GANHOU!!!')
#                     exit()
#
#
# def principal():
#     jogo()
#
#
# if __name__ == '__main__':
#     principal()

