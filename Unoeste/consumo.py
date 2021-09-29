racao = int(input('Digite a quantidade de ração comprada (em quilos):' ))
cachorro1 = int(input('Digite a quantidade de ração consumida Cachorro 1 (em gramas) por dia:'))
cachorro2 = int(input('Digite a quantidade de ração consumida Cachorro 2 (em gramas) por dia:'))
Consumo_cachorro1 = cachorro1 / 1000
Consumo_cachorro2 = cachorro2 / 1000
Total_consumo_dia = Consumo_cachorro1 + Consumo_cachorro2
Dias = racao / Total_consumo_dia
print('Total de dias de duração da ração comprada : ' , Dias)
