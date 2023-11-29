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

print("########################## Exercicio 06 ##########################")
# Dividindo a string da coluna 'Data_Pedido' usando '/'
df_dsa['Ano'] = df_dsa['Data_Pedido'].str.split('/').str[2]

# Agrupa pelo Segmento
segmento_Por_Ano = df_dsa.groupby(['Ano', 'Segmento'])

# Faz a somatoria do Valor_Venda
segmento_Por_Ano_Soma = segmento_Por_Ano['Valor_Venda'].sum()

print(segmento_Por_Ano_Soma)
