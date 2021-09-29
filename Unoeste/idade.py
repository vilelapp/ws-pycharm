anonasc = int(input('Digite o ano de nascimento: '))
anoatual = int(input('Digite o ano atual: '))

idade = anoatual - anonasc

print('Idade: ', idade)

if idade > 18:
    print('Maior idade')

else:
    print('Menor idade')
