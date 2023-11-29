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

### Quais São as 10 Cidades com Maior Total de Vendas?
### Demonstre o resultado através de um gráfico de barras.
print("########################## Exercicio 04 ##########################")
# Agrupa pela Cidade
cidade = df_dsa.groupby('Cidade')['Valor_Venda'].sum().reset_index().sort_values(by='Valor_Venda', ascending=False).head(10)

plt.figure(figsize=(16, 6))
sns.set_palette('coolwarm')
sns.barplot(data = cidade,
            y = 'Valor_Venda',
            x = 'Cidade').set(title = 'Top 10 vendas por Cidade')
plt.xticks(rotation=60)
plt.show()

