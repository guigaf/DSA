# Exercício 1 - Crie uma lista de 3 elementos e calcule a terceira potência de cada elemento.
lista = [2, 3, 4]

resultado = [x**3 for x in lista if x**3 > 10]

print(resultado)