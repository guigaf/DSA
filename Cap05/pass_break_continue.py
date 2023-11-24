import timeit

def my_function():
    valor =0
    while valor < 10:
        if valor == 4:
            print("break")
            break # quebra o codigo nessa linha, pulando para fora do loop
        elif valor == 3:
            print("continue")
            valor += 1
            continue # continua o codigo para a proxima iteração, ignorando o proximo else
        else:
            print("pass")
            pass # não faz nada, apenas continua o codigo normalmente
        print(valor)
        valor += 1
    pass


# Medindo o tempo de execução
elapsed_time = timeit.timeit(my_function, number=1)
print(f"Tempo de execução: {elapsed_time} segundos")