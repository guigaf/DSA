xy = [[100, 0], [1, 1], [0, 0], [0, 2], [2, 0], [1, 2], [2, 1], [1, 0], [2, 2], [0, 1], [0, 100]]


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
# Printa os valores antes de modificar
print(xy)

# Passa a lista "xy" para a função bubble_sort() para ordenar em ordem crescente os valores da lista
bubble_sort(xy)

# Printa os valores após ordenar de forma crescente
print(xy)

# Adiciona um novo valor no final da lista xy
xy.append([0, 55])

# Printa os valores após adicionar novo valor na lista
print(xy)