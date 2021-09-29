print('Vamos calcular seu IMC?')
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura**2)

print(imc)
if imc <= 18.5:
    print('Abaixo do peso')

elif 18.5 <= imc <= 25:
    print('Peso normal')

elif 25 <= imc <= 30:
    print('Acima do peso')

else:
    print('Obeso')
