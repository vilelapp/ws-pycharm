# Parte 01
#
# frase1 = "Hoje veremos string na aula do módulo 3 de estruturas dados e algoritimos. Depois vocês implementaraão em " \
#          "um jogo."
# frase2 = """                   Hoje veremos string na aula do módulo 3 de estruturas dados e algoritimos.
#          Depois vocês implementaraão em um jogo."""
#
# print(frase1)
# print(frase2)
#

# Parte 02

# nomeDisc = 'Estrutura de Dados e Algoritimos'
# print(nomeDisc[3])
#
# for i in nomeDisc:
#     print(i)

# lista = ['Estrutura', 'de', 'Dados', 'e', 'Algoritimos']
#
# lista[1] = 'xxxx'
# print(lista)
#
# nomeDisc = 'Núcleo de Educação'
# print(nomeDisc)

# Parte 3
#
# str1 = 'Maria'
# str2 = 'MARIA'
# print(str1*5)
# str1 = str1*2
# print(str1)
# print(str1+str1+str1+' da Silva')
#
# if str1 > str2:
#     print(str1, 'é maior que', str2)
# else:
#     print(str2, 'é maior que', str1)

# for i in range(0, 256):
#     print(f'{i} = {chr(i)}')

# Parte 4

# valor = '0100'
# print(int(valor))
#
# print(type(valor))
#
# teste = 'a123456z'
# try:
#     print(int(teste))
# except:
#     print('Não foi possível executar o comando')

# Parte 5 - Slicing (fatiamento)

# nome = 'José Oliveira da Silva'
# print(nome[5:13])
# print(nome[::-1]) # inverter
#
# nome = '  Cristiano    '
# print(nome.strip() + '!!!') # remove espaços

# Parte 6
# frase = 'Cristiano Fernando Vilela'
# print(frase.upper())
# print(frase.lower())
# print(frase.capitalize())
# print(frase.strip())

# Parte 7 - Exercicio

def data_por_extenso(dia, mes, ano):
    # Tupla com os meses: 0-Janeiro, 1-fevereiro, 2-março
    meses = ("janeiro", "fevereiro", "marco", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro")
    extenso = 'Data inválida'
    if ((type(dia) is int and type(mes) is int and type(ano) is int) and (dia >=1 and dia <=31) and (mes >= 1 and mes <=12) and (ano > 1900)):
        extenso = '%02d de %s de %04d' % (dia, meses[mes-1], ano)
    return extenso

print(data_por_extenso(5,11,2021)) # 5 de novembro de 2021
