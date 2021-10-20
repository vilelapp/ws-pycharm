l_alunos = []
l_alunos.append('Regina')
l_alunos.append('Marcelo')
l_alunos.append('Rafael')
l_alunos.append('Eriton')

l_alunos.sort()
l_alunos.extend(['Junior', 'Vanessa'])
l_alunos.insert(10, 'Renato')

try:
    l_alunos.remove('Eriton')
    l_alunos.remove('Luiz')
except:
    print('Algum dos nomes não foram excluídos da lista')

l_alunos.pop(3)

for i in range(len(l_alunos)):
    print(i, '->', l_alunos[i])

print(l_alunos.index('Regina'))




