import timeit

lista = ["banana", "abacate", "melancia", "cereja", "manga", "ama"]
nova_lista = []

def my_function_01():
    for x in lista:
        if "m" in x:
            nova_lista.append(x)
    print(nova_lista)


lista = ["banana", "abacate", "melancia", "cereja", "manga", "ama"]
nova_nova_lista = []

def my_function_02():
    nova_nova_lista = [x for x in lista if "m" in x]
    print(nova_nova_lista)

elapsed_time_01 = timeit.timeit(my_function_01, number=1)
print(f"Tempo de execução: {elapsed_time_01} segundos")

elapsed_time_02 = timeit.timeit(my_function_02, number=1)
print(f"Tempo de execução: {elapsed_time_02} segundos")