def dadosPaciente():
    nome = input("Digite o nome do paciente: ")
    telefone = input("Digite o telefone do paciente: ")
    return nome, telefone

def calculoImc():
    peso = float(input("Digite o peso do paciente: "))
    altura = float(input("Digite a altura do paciente: "))
    imc = peso / (altura ** 2)
    print(f"O imc do paciente é {imc}")

dadosPaciente()
calculoImc()

