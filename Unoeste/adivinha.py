from random import randint

print('-----------------------')
print('---JOGO DE ADIVINHAR---')
print('-----------------------')
print('')
nome = input('Digite seu nome para começar: ')
print('')
print(f'Olá, {nome}, você tem 6 tentativas.')

random = randint(0, 20)
palpite = 0
tentativas = 6
while palpite != random:
    palpite = int(input('Digite um número entre 0 a 20: '))
    if 0 <= palpite <= 20:
        tentativas = tentativas - 1
        if palpite == random:
            print('')
            print(f'Parabéns, {nome} você acertou! O número era {random}.')
            print('')
            break
        else:
            print('')
            if palpite > random:
                print('Você errou! Dica: tente um número menor')
            else:
                print('Você errou! Dica: Tente um número maior')
            print(f'Você ainda possui {tentativas} tentativa(s).')
            print('')
        if tentativas == 0:
            print('')
            print(f'Suas tentativas acabaram {nome}, você perdeu!')
            print('')
            break

print('-----------------------')
print('------FIM DE JOGO------')
print('-----------------------')
