def MinMax(temperaturas):
    print('A menor temperatura do mês foi: ', mínima(temperaturas), 'C.')
    print('A maior temperatura do mês foi: ', máxima(temperaturas), 'C.')

def mínima(temps):
    min = 0
    i = 0
    while i < len(temps):
        if temps[i] < min:
            min = temps[i]
        i = i + 1
    return min

def testa_mínima():
    print('Iniciando os testes')
    temp = [0]
    if mínima(temp) != 0:
        print('Valor errado para array', temp)
    temp = [0, 0, 0, 0, 0, 0]
    if mínima(temp) != 0:
        print('Valor errado para array', temp)
    temp = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    if mínima(temp) != 0:
        print('Valor errado para array', temp)
    temp = [30, 27, 25, 26, 29, 31, 32, 33, 30, 29, 24, 26]
    if mínima(temp) != 22:
        print('Valor errado para array', temp)
    temp = [-15, -12, 0 , 20, 30]
    if mínima(temp) != -15:
        print('Valor errado para array', temp)

    print('Finalizando os testes')
