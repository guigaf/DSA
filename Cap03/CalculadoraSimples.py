def verificaOperacao():
    while True:
        operacaoResult = input("Selecione a operação (+, -, *, /): ")
        if operacaoResult in ['+', '-', '*', '/']:
            return operacaoResult
        else:
            print("Operador inválido. Tente novamente.")

print("Bem-vindo ao calculador simples")
num1 = float(input("Insira o primeiro numero: "))
num2 = float(input("Insira o segundo numero: "))
operacao = verificaOperacao()

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    resultado = num1 / num2

print("O resultado final é: ", resultado)