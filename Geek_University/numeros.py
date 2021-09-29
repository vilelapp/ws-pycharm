print()
print('Programa para gerar números, by CRISTIANO VILELA')
print()
arquivo = open('numeros.txt', 'w')
x = int(input('Digite um número inicial: '))
y = int(input('Digite um número final: '))

for num in range(x, y + 1):
    arquivo.write('{:0>4}'.format(num) + '\n')
arquivo.close
print()
print('Arquivo <numeros.txt> salvo no mesmo diretório do programa')
