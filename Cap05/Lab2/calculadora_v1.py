# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************")
def is_numero(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False
def verificaOperacao():
    while True:
        num1 = (input("Insira o primeiro numero: "))
        if is_numero(num1):
            pass 
        else: 
            print("Valor inválido. Tente novamente.")
            continue
        num2 = (input("Insira o segundo numero: "))
        if is_numero(num2): 
            pass 
        else: 
            print("Valor inválido. Tente novamente.")
            continue
        while True:
            operacaoResult = input("Selecione a operação (+, -, *, /): ")
            if operacaoResult in ['+', '-', '*', '/']:
                break
            else:
                print("Operador inválido. Tente novamente.")
        if operacaoResult == "+":
            resultado = num1 + num2
        elif operacaoResult == "-":
            resultado = num1 - num2
        elif operacaoResult == "*":
            resultado = num1 * num2
        elif operacaoResult == "/" and num2 != 0 :
            resultado = num1 / num2
        elif operacaoResult == "/" and num2 == 0 :
            print("Não é possivel dividir por 0, altere o calculo.")
            continue
        return resultado, operacaoResult, num1, num2

while True:
    resultado, operacaoResult, num1, num2 = verificaOperacao()
    print(num1, operacaoResult, num2, "=", resultado)