# Exercício 9 - Considere a lista abaixo e retorne apenas os elementos cujo índice for maior que 5.
lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

listaIndice = [x for x in lista if lista.index(x) > 4]

print(listaIndice)