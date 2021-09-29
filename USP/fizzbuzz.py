valor = int(input('Digite um numero:'))
if (valor / 3):
    print('Fizz')
if (valor / 5):
    print('Buzz')
if (valor % 5) or (valor % 3):
    print(valor)
else :
    print("FizzBuzz")