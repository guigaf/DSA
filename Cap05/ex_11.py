# Exercício 1 - Crie uma estrutura que pergunte ao usuário qual o dia da semana. 
# Se o dia for igual a Domingo ou a sábado, imprima na tela "Hoje é dia de descanso", 
# caso contrário imprima na tela "Você precisa trabalhar!"
teste = False
while teste == True:
    dia_da_semana = str(input("que dia é hoje?: "))

    if (dia_da_semana == "domingo") or (dia_da_semana == "sabado"):
        print("BORA DESCANÇAR!!!")
    else:
        print("com sua vida miseravel voce deve trabalhar :(")


