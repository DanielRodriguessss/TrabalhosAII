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
