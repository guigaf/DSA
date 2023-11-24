# Exercício 8 - Considere os dois dicionários abaixo. 
# Crie um terceiro dicionário com as chaves do dicionário 1 e os valores do dicionário 2.
dict1 = {'a':1,'b':2}
dict2 = {'c':4,'d':5}

def trocaValores(d1, d2):
    dicTemp = {}
    
    for d1key, d2val in zip(d1,d2.values()):
        dicTemp[d1key] = d2val
    
    return dicTemp

dict3 = trocaValores(dict1, dict2)
print(dict3)