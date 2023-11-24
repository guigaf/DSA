# Exercício 2 - Reescreva o código abaixo, usando a função map(). O resultado final deve ser o mesmo!
palavras = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil.'.split()
resultado = [[w.upper(), w.lower(), len(w)] for w in palavras]
for i in resultado:
    print (i)


# Função Python que retorna um número ao quadrado
def splitStr(arr1:str):
    return [arr1.upper(), arr1.lower(), len(arr1)]

palavras = "A Data Science Academy oferce os melhores cursos de análise de dados do Brasil.".split()

resultado = list(map(splitStr, palavras))

print(resultado)

