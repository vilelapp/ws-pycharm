
print("Cálculo do fatorial de um número\n")


n = int(input("Digite o valor de n: "))
i = 1
n_fat = 1

while i <= n:
    n_fat = n_fat * i
    i = i + 1

print(n_fat)
