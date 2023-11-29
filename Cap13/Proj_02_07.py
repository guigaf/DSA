# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

# Carrega o dataset
df_dsa = pd.read_csv('C:/Geral/DEV/DSA/Cap13/dados/dataset.csv')

# Shape
df_dsa.shape

### Pergunta de Negócio 7 (Desafio Nível Júnior):
### Os gestores da empresa estão considerando conceder diferentes faixas de descontos e gostariam de fazer uma simulação com base na regra abaixo:
### - Se o Valor_Venda for maior que 1000 recebe 15% de desconto.
### - Se o Valor_Venda for menor que 1000 recebe 10% de desconto.
### Quantas Vendas Receberiam 15% de Desconto?
print("########################## Exercicio 07 ##########################")

df_dsa['Valor_Desconto'] = 0.0
df_dsa['Valor_Venda_Com_Desconto'] = 0.0
df_dsa['Valor_Desconto'] = np.where(df_dsa['Valor_Venda'] <= 1000, df_dsa['Valor_Venda'] * 0.10, df_dsa['Valor_Venda'] * 0.15)
df_dsa['Valor_Venda_Com_Desconto'] = df_dsa['Valor_Venda'] - df_dsa['Valor_Desconto']

Valor_Venda_Desconto_10 = df_dsa.query('Valor_Venda <= 1000.0')
Valor_Venda_Desconto_15 = df_dsa.query('Valor_Venda > 1000.0')

print("O numero de vendas que receberiam 10", "%",  "de desconto é: ", len(Valor_Venda_Desconto_10))
print("O numero de vendas que receberiam 15", "%",  "de desconto é: ", len(Valor_Venda_Desconto_15))

### Pergunta de Negócio 8 (Desafio Nível Master):
### Considere Que a Empresa Decida Conceder o Desconto de 15% do Item Anterior. Qual Seria a Média do Valor de Venda Antes e Depois do Desconto?