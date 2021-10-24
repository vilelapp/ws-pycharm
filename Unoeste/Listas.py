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

'''
O tipo de dado lista tem ainda mais métodos. Aqui estão apresentados todos os métodos de objetos do tipo lista:

list.append(x)
Adiciona um item ao fim da lista. Equivalente a a[len(a):] = [x].

list.extend(iterable)
Prolonga a lista, adicionando no fim todos os elementos do argumento iterable passado como parâmetro. 
Equivalente a a[len(a):] = iterable.

list.insert(i, x)
Insere um item em uma dada posição. O primeiro argumento é o índice do elemento antes do qual será feita a inserção, 
assim a.insert(0, x) insere um elemento na frente da lista e a.insert(len(a), x) e equivale a a.append(x).

list.remove(x)
Remove o primeiro item encontrado na lista cujo valor é igual a x. Se não existir valor igual, uma exceção ValueError 
é levantada.

list.pop([i])
Remove um item em uma dada posição na lista e o retorna. Se nenhum índice é especificado, a.pop() remove e devolve o 
último item da lista. (Os colchetes ao redor do i na demonstração do método indica que o parâmetro é opcional, 
e não que é necessário escrever estes colchetes ao chamar o método. Você verá este tipo de notação frequentemente 
na Biblioteca de Referência Python.)

list.clear()
Remove todos os itens de uma lista. Equivalente a del a[:].

list.index(x[, start[, end]])
Devolve o índice base-zero do primeiro item cujo valor é igual a x, levantando ValueError se este valor não existe.

Os argumentos opcionais start e end são interpretados como nas notações de fatiamento e são usados para limitar a 
busca para uma subsequência específica da lista. O índice retornado é calculado relativo ao começo da sequência 
inteira e não referente ao argumento start.

list.count(x)
Devolve o número de vezes em que x aparece na lista.

list.sort(*, key=None, reverse=False)
Ordena os itens na lista (os argumentos podem ser usados para personalizar a ordenação, veja a função sorted() para 
maiores explicações).

list.reverse()
Inverte a ordem dos elementos na lista.

list.copy()
Devolve uma cópia rasa da lista. Equivalente a a[:].
'''