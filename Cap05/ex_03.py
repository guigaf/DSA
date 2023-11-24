# Exercício 3 - Crie uma função que receba como parâmetro uma lista de 4 elementos, adicione 2 elementos a lista e 
# imprima a lista
lista = ["elemento_01", "elemento_02", "elemento_03", "elemento_04"]

def funcao(el1):
    el1.append("Elemento_05")
    el1.append("Elemento_06")
    print(lista)

funcao(lista)