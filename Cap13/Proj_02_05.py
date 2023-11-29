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

### Qual Segmento Teve o Maior Total de Vendas?
### Demonstre o resultado através de um gráfico de pizza.
print("########################## Exercicio 05 ##########################")
# Agrupa pelo Segmento
segmento = df_dsa.groupby('Segmento')["Valor_Venda"].sum().reset_index()

plt.figure(figsize=(16, 6))

# Monta um grafico de pizza
plt.pie(segmento['Valor_Venda'], 
        labels=segmento['Segmento'], 
        autopct='%1.1f%%', 
        startangle=90, 
        colors=['red', 'green', 'blue'])
center_circle = plt.Circle((0, 0), 0.82, fc = 'white')
fig = plt.gcf()
fig.gca().add_artist(center_circle)

plt.annotate(text = 'total de vendas: ' + '$ ' + str(int(sum(df_dsa['Valor_Venda']))), xy = (-0.25, 0))
plt.title('Titulo')
plt.show()