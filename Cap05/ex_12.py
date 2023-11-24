# Exercício 2 - Crie uma lista de 5 frutas e verifique se a fruta 'Morango' faz parte da lista

frutas = ["pessego", "abacaxi", "banana", "pêra", "melancia"]

def verifica_se_contem(fruta):
    if fruta in frutas:
        tem = True
    else:
        tem = False
    return tem

print(verifica_se_contem("morango"))