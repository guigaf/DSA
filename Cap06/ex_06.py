# Exercício 6 - 
# Considerando o range de valores abaixo, use a função filter() para retornar 
# apenas os valores negativos.

def verificaNegativo(x):
    return x < 0

lista = (list(range(-5, 5)))
listaNova = list(filter(verificaNegativo, lista))

print(listaNova)

print(list(filter((lambda x: x < 0), range(-5, 5))))
