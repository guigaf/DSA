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

print("########################## Exercicio 03 ##########################")
# Agrupa pela data do pedido
estado = df_dsa.groupby('Estado')['Valor_Venda'].sum().reset_index()

plt.figure(figsize=(16, 6))
sns.barplot(data = estado,
            y = 'Valor_Venda',
            x = 'Estado').set(title = 'Vendas Por Estado')
plt.xticks(rotation=80)
plt.show()
