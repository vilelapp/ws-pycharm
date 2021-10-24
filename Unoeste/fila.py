import queue

fila = queue.Queue()

fila.put(12)
fila.put(40)
fila.put(33)
fila.put(15)
fila.put(21)
fila.put(100)
fila.put(17)

print(list(fila.queue))
# Resultado : [12, 40, 33, 15, 21, 100, 17]

print(list(fila.queue))
print(fila.qsize())
print(fila.empty())
print(fila.full())
fila.put(5)
print(list(fila.queue))
fila.put_nowait(55)
print(list(fila.queue))
fila.get(15)
print(list(fila.queue))
fila.get_nowait()
print(list(fila.queue))
