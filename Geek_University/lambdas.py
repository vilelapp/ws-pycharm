nome_completo = (lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title())
print(nome_completo('Cristiano', 'Vilela'))

autores = ['Issac Asimov', 'Ray Bradbury', 'Orson Scott Card', 'Douglas Adams', 'H. G. Well', 'Leigh Brackett']

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)


# Função Quadrática
def geradora_funcao_quadratica(a, b, c):
    return lambda x: a * x ** 2 + b * x + c


teste = geradora_funcao_quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))

print(geradora_funcao_quadratica(3, 0, 1)(2))
