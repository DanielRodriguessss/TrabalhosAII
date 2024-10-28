# Função para somar
def soma(x, y):
    return x + y


# Função principal
def calculadora():

    while True:
        print("Escolha a operação: ")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisao")
        print("5 - Sair")

        escolha= input("Digite sua escolha 1/2/3/4/5")
        if escolha == "1":
            print(f"Resultado:  {num1} + {num2} = {soma(num1, num2)}")
        elif escolha == "2":
            print(f"Resultado: {num1} - {num2} = {soma(num1, num2)}")
        elif escolha == "3":
            print(f"Resultado: {num1} * {num2} = {soma(num1, num2)}")
        elif escolha == "4":
            print(f"Resultado: {num1} / {num2} = {soma(num1, num2)}")

    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))
    result = soma(num1, num2)
    print("Resultado da soma:  " + str(result))


# Executa a calculadora
calculadora()


# Função para subtrair
def subtração(x, y):
    return x - y


# Função principal
def calculadora():
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))
    result = subtração(num1, num2)
    print("Resultado da subtração:  " + str(result))


# Executa a calculadora
calculadora()


# Função para multiplicar
def multiplicação(x, y):
    return x * y


# Função principal
def calculadora():
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))
    result = multiplicação(num1, num2)
    print("Resultado da multiplicação:  " + str(result))


# Executa a calculadora
calculadora()


# Função para dividir
def divisão(x, y):
    return x / y


# Função principal
def calculadora():
    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))
    result = divisão(num1, num2)
    print("Resultado da divisão:  " + str(result))



# Executa a calculadora
calculadora()

