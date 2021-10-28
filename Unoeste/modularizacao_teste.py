def calcula_imc(peso, altura):
    resultado = peso / (altura ** 2)
    return resultado

def dados_paciente():
    nome = input('Digite o nome do paciente: ')
    telefone = input('Digite o telefone do paciente: ')
    peso = float(input("Digite o peso do paciente: "))
    altura = float(input("Digite a altura do paciente: "))
    return nome, telefone, peso, altura

def principal():
    nome, telefone, peso, altura = dados_paciente()
    imc = calcula_imc(peso, altura)
    print(f"O imc do paciente {nome} é {round(imc)}")

if __name__ == '__main__':
    principal()

