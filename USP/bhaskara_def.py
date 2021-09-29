import math

def delta( a, b, c ):
    return b ** 2 - 4 * a * c

def main():
    a = int(input('Digite um valor para A: '))
    b = int(input('Digite um valor para B: '))
    c = int(input('Digute um valor para C: '))
    imprime_raizes(a, b, c)

def imprime_raizes(a, b, c):
    d = delta(a, b, c)
    if d == 0:
        raiz1 = (-b + math.sqrt(d)) / (2 * a)
        print('A única raiz é: ', raiz1)
    else:
        if d < 0:
            print('Esta equação não possui raízes reais')
        else:
            raiz1 = (-b + math.sqrt(d)) / (2 * a)
            raiz2 = (-b - math.sqrt(d)) / (2 * a)
            print('A primeira raiz é: ', raiz1)
            print('A segunda raiz é: ', raiz2)
