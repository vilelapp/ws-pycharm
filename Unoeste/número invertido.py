#em python#

numero = int(input('Digite um número de 4 digitos: '))
milhar = numero//1000
centena = (numero%1000)//100
dezena = (numero%100)//10
unidade = numero%10
print(f'O número invertido é {unidade}{dezena}{centena}{milhar}.')
