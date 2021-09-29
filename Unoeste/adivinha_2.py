from random import randint

nome = input('Qual o seu nome? ')
print(f'Olá, {nome}')

ramdom = randint(0, 20)
chute = 0
chance = 6
while chute != ramdom:
    chute = int(input('Digite um número entre 0 e 20: '))
    if 0 <= chute <= 20:
        chute = chute - 1
        if chute == ramdom:
            print(f'Parabéns, {nome} você acertou!!! O número era {ramdom}. ')
            break
        else:
            if chute > ramdom:
                print(f'{nome}, você não acertou. Dica: tente um número menor')
            else:
                print(f'{nome}, você não acertou. Dica: tente um número maior')
            print(f'Você ainda tem mais {chance} chance(s)')
        if chance == 0:
            print('Você perdeu!!!')
            break
