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
