#lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#for i in lista:
#    print("I: ", i)
#    print("Lista: ", lista[i-1])

matriz = [[42,   23,   34], 
          [100,  215,  144], 
          [10.1, 98.7, 12.3]]
maior_numero =0

for linha in matriz:
    #print("linha: ", linha)
    for num in linha:
        #print("num: ", num)
        if num > maior_numero:
            maior_numero = num
            print("Maior numero é: ", maior_numero)
