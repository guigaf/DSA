# Exercício 4 - 
# Crie duas funções
# Uma para elevar um número ao quadrado 
# Outra para elevar ao cubo 
# Aplique as duas funções aos elementos da lista abaixo. 
# Obs: as duas funções devem ser aplicadas simultaneamente.
lista = [0, 1, 2, 3, 4]

def square(l):
    el_2 = [x**2 for x in l]
    return el_2
def cube(l):
    el_3 = [x**3 for x in l]
    return el_3

print(square(lista))
print(cube(lista))
