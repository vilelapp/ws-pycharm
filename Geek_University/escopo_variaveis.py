'''
Escopo de variaveis
Dois casos de escopo

1- Variaveis Globais
   - reconhecida em todo programa
2- Variaveis Locais
   - reconhecido apenas no bloco

Para declarar variavel em python
nome_da_variavel = valor_da_variavel

Linguagem C e Java

int numero = 42;
'''

numero = 42 # exemplo global
print(numero)

numero = 42 # exemplo locais (por bloco)
if numero > 10:
    novo = numero + 10
    print(novo)

