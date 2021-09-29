import math

x1 = float(input('Digite a medida do ponto x1:'))
x2 = float(input('Digite a medida do ponto x2:'))

y1 = float(input('Digite a medida do ponto y1:'))
y2 = float(input('Digite a medida do ponto y2:'))

dxy = math.sqrt(((x1 - x2)**2) + ((y1 - y2)**2))

if dxy >= 10:
    print('longe')
else:
    print('perto')