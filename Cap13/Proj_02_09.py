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

### Pergunta de Negócio 9 (Desafio Nível Master Ninja):
### Qual o Média de Vendas Por Segmento, Por Ano e Por Mês?
### Demonstre o resultado através de gráfico de linha.
print("########################## Exercicio 09 ##########################")
df_dsa['Data_Pedido'] = pd.to_datetime(df_dsa['Data_Pedido'], dayfirst = True)
df_dsa['Ano'] = df_dsa['Data_Pedido'].dt.year
df_dsa['Mes'] = df_dsa['Data_Pedido'].dt.month
segmento_Por_Ano_Mes = df_dsa.groupby(['Ano', 'Mes', 'Segmento'])['Valor_Venda'].agg([np.sum, np.mean, np.median])
print(segmento_Por_Ano_Mes)
anos = segmento_Por_Ano_Mes.index.get_level_values(0)
meses = segmento_Por_Ano_Mes.index.get_level_values(1)
segmentos = segmento_Por_Ano_Mes.index.get_level_values(2)

plt.figure(figsize=(12, 6))
sns.set()
fig1 = sns.relplot(kind ='line',
                   data = segmento_Por_Ano_Mes,
                   y = 'mean',
                   x = meses,
                   hue = segmentos,
                   col = anos,
                   col_wrap = 2)
plt.show()