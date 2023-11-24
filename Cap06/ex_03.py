# Exercício 3 - Calcule a matriz transposta da matriz abaixo.
# Caso não saiba o que é matriz transposta, visite este link: https://pt.wikipedia.org/wiki/Matriz_transposta
# Matriz transposta é um conceito fundamental na construção de redes neurais artificiais, base de sistemas de IA.
matriz = [[1, 2],
          [3, 4],
          [5, 6],
          [7, 8]]

num_colunas = len(matriz[0])

transpose = [[row[i] for row in matriz] for i in range(num_colunas)]

print("Minha matriz é: ", matriz)
print("Minha matriz transposta é: ", transpose)
