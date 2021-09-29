arquivo = open('teste.txt', 'w')
x = int(input('Digite um número inicial: '))
y = int(input('Digite um número final: '))

num = list(range(x, y + 1))

if len(num) == 1:
    num = "0000" + num
    num = int(num)
elif len(num) == 2:
    num = "000" + num
    num = int(num)
elif len(num) == 3:
    num = "00" + num
    num = int(num)
else:
    len(num) == 4
    num = "0" + num
    num = int(num)

arquivo.write(str(num) + '\n')

arquivo.close
