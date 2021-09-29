listaGabarito=[]
listaRespostas=[]
acertos=0
nome=input("Informe o nome do(a) aluno(a) para a correção: ")
print("Informe as respostas do Gabarito")

for gabarito in range(10):
    gabarito = input("Pergunta %d, resposta informada: " % int(gabarito + 1)).lower()
    listaGabarito.append(gabarito)

print("\nInforme as respostas do(a) aluno(a) %s" %nome)

for resp in range(10):
    res=input("Pergunta %d, resposta informada: " % int(resp+1)).lower()
    listaRespostas.append(res)

for i in range(len(listaGabarito)):
    if listaGabarito[i]==listaRespostas[i]:
        acertos=acertos+1
print("A quantidade de acertos do(a) aluno(a) %s é: " %nome, acertos)
