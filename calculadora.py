# Função para somar
def soma(x, y):
    return x + y

# Função para subtrair
def subtração(x, y):
    return x - y

# Função para multiplicar
def multiplicação(x, y):
    return x * y

# Função para dividir
def divisão(x, y):
    return x / y

#Função para exibir histórico das últimas duas operações
def ver_historico(historico):
    print("\nHistórico das últimas cinco operações:")
    for operacao in historico:
        print(operacao)
    if not historico:
        print("Nenhuma operação realizada ainda.")
    print()

# Função principal
def calculadora():
    historico = []

    while True:
        print("Escolha a operação: ")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisao")
        print("5 - Sair")
        print("6 - Histórico")

        escolha= input("Digite sua escolha 1/2/3/4/5/6:")

        if escolha != "6":
            num1 = int(input("Digite o primeiro numero: "))
            num2 = int(input("Digite o segundo numero: "))

        if escolha == "1":
            print(f"Resultado:  {num1} + {num2} = {soma(num1, num2)}")
            historico.append(f"{num1} + {num2} = {soma(num1, num2)}")
        elif escolha == "2":
            print(f"Resultado: {num1} - {num2} = {subtração(num1, num2)}")
            historico.append(f"{num1} - {num2} = {subtração(num1, num2)}")
        elif escolha == "3":
            print(f"Resultado: {num1} * {num2} = {multiplicação(num1, num2)}")
            historico.append(f"{num1} * {num2} = {multiplicação(num1, num2)}")
        elif escolha == "4":
            print(f"Resultado: {num1} / {num2} = {divisão(num1, num2)}")
            historico.append(f"{num1} / {num2} = {divisão(num1, num2)}")
        if len(historico) > 5:
            historico.pop(0)
        elif escolha == "6":
            ver_historico(historico)
        elif escolha == "5":
            print("A encerrar a calculadora")
            break

# Executa a calculadora
calculadora()
