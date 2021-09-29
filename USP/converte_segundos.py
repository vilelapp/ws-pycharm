segundos = input('Digite o número de segundos que gostaria de converter ')
seg_int = int(segundos)

horas = seg_int // 3600
seg_restante = seg_int % 3600
minutos = seg_restante // 60
seg_restante_final = seg_restante % 60

print(horas, 'horas', minutos, 'minutos e ', seg_restante_final, 'segundos')
