import timeit

def my_function():
    primos = []
    for num in range (2, 31):
        eh_primo = True
        i = 2
        while i <= num // 2:
            if num % i == 0:
                eh_primo = False
                break
            i += 1
        if eh_primo:
            primos.append(num)
    print(primos)
    pass


# Medindo o tempo de execução
elapsed_time = timeit.timeit(my_function, number=1)
print(f"Tempo de execução: {elapsed_time} segundos")