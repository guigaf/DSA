listaDeValores = [9, 8, 5, 2, 7, 6, 4, 1, 3, 5, 7, 8, 4, 6, 11, 45, 24, 57, 84, 56, 25, 41, 23, 35, 11, 12, 31, 14, 15, 18, 19, 7, 2]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort(listaDeValores))