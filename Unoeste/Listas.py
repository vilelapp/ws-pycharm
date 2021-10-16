t = [16, 24, 6, 14, 12, 15, 10, 7, 5, 3]

li = []
for x in t:
    li.append(x ** 2)
print(li)

# outra forma: li = [expressão for x in y condição]
li = [x ** 2 for x in t]
print(li)

# exemplo números pares de uma lista:
li = []
for x in t:
    if x % 2 == 0:
        li.append(x ** 2)
print(li)

# outra forma:
li = [x ** 2 for x in t if x % 2 == 0]
print(li)
