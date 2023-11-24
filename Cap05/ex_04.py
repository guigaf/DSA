# Exercício 4 - Crie uma função que receba um argumento formal e uma possível lista de elementos. 
# Faça duas chamadas à função, com apenas 1 elemento e na segunda chamada com 4 elementos


def funcao(arr1, *arr2):
    print(arr1)
    for i in arr2:
        print(i)
    return

funcao(1)
funcao("maça", "limão", "mamão")