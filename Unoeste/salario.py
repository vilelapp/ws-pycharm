valor_hora = float(input('Digite qual o valor que ganha por hora R$ : '))
horas_mes = int(input('Digite o número de horas trabalhadas no mês: '))
salario_bruto = valor_hora * horas_mes
imposto_renda = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salarioliquido = salario_bruto - imposto_renda - inss - sindicato

print(f'Salário bruto: R$ {salario_bruto}')
print(f'IR: R$ {imposto_renda}')
print(f'INSS: R$ {inss}')
print(f'Sindicato: R$ {sindicato}')
print(f'Salário Líquido: R$ {salarioliquido:.2f}')
