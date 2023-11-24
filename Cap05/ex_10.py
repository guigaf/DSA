# Exercício 10 - Crie uma list comprehension que imprima os números menores que 5 em um intervalo de 1 a 10


nova_lista = [x for x in range(11) if x < 5]

print(list(nova_lista))