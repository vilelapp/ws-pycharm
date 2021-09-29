segundos = input('Digite o número de segundos que gostaria de converter ')
seg_int = int(segundos)

horas = seg_int // 3600
dias = horas // 86400
seg_restante = seg_int % 3600
minutos = seg_restante // 60
seg_restante_final = seg_restante % 60

if (horas >= 24):

	dias = int(horas / 24)
	horas = int(horas % 24)

print(dias, 'dias,', horas, 'horas,', minutos, 'minutos e', seg_restante_final, 'segundos.')