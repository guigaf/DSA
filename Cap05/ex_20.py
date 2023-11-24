# Exercício 10 - 
# Faça um programa que conte quantas vezes a letra "r" aparece na frase abaixo. 
# Use um placeholder na sua instrução de impressão

# “A gratidão é a virtude das almas nobres. O quão feliz é uma pessoa depende da profundidade de sua gratidão.” 

frase = str("A gratidão é a virtude das almas nobres. O quão feliz é uma pessoa depende da profundidade de sua gratidão.")
contadorR = 0
#contadorR = frase.count('r')
for caracter in frase:
    if caracter == "r":
        contadorR += 1

print("O numero de caracteres R encontrados foram {}".format(contadorR))
print(f"O numero de caracteres R encontrados foram {contadorR}")
print("O numero de caracteres R encontrados foram %s" %contadorR)