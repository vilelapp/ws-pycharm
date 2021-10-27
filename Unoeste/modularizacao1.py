#Parte 01 - sem usar modularização
# Num1 = 0
# while Num1 <=0:
#     try:
#         Num1 = int(input('Informe um número inteiro: '))
#     except:
#         print('Informe um número inteiro positivo: ')
# print('Número 1 = ', Num1)

# Parte 02 - com modularização
# def LerInteiroPositivo(msg):
#     '''Esta função realiza a entrada de números inteiros positivo'''
#     Num = 0
#     while Num <= 0:
#         try: # Usuário informar letras ou caracteres especiais
#             Num = int(input(msg))
#         except:
#             print('Informe um número inteiro positivo: ')
#     return (Num)
#
# def LerDecimal(msg):
#     '''Esta função realiza a entrada de números com casas decimais'''
#     Num = 0.0
#     try: # Usuário informar letras ou caracteres especiais
#         Num = float(input(msg))
#     except:
#         print('Número inválido: ')
#     return (Num)
#
# def media(v1, v2):
#     '''Função que calcula a média de 2 valores'''
#     m = (v1 + v2) / 2
#     return m
#
# # Parte Inicial do programa
# Idade = LerInteiroPositivo('Informe a sua idade: ')
# print(f'A idade é {Idade} anos')
# Mes = LerInteiroPositivo('Informe o mês atual: ')
# print(f'O mês é {Mes}')
#
# salario = LerDecimal('Informe seu salário: ')
# print(f'O salário é US$ {salario:.2f}')

# Parte 3 - Escopo de variáveis
def EstudaEscopo():
    global X # indica para o programa que a variável X modificada é a GLOBAL
    X = 40 # Modifica o valor da variável GLOBAL
    Y = X * 2
    print('X local existe DENTRO da função: valor =', X)
    print('Y local existe DENTRO da função: valor =', Y)

# Parte do Início do programa
print('Início do Programa')
X = 10
print('X global existe FORA da função: valor =', X)
#print('Y local existe DENTRO da função: valor =', Y) -> a variavel Y não existe na memória fora da função.
EstudaEscopo()
print('Fim do Programa')
