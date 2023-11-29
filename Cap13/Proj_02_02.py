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

# Amostra dos dados - Inicio
print("######################## Inicio dos dados ########################")
print(df_dsa.sample(10))

# Amostra dos dados - Amostra
#print("######################## Amostra dos dados ########################")
#print(df_dsa.sample(5))

# Amostra dos dados - Fim
#print("########################## Fim dos dados ##########################")
#print(df_dsa.tail())

# Colunas do conjunto de dados
#print("########################## Colunas do conjunto de dados ##########################")
#print(df_dsa.columns)

# Verificando o tipo de dado de cada coluna
#print("########################## Verificando o tipo de dado de cada coluna ##########################")
#print(df_dsa.dtypes)

# Resumo estatístico da coluna com o valor de venda
#print("########################## Resumo estatístico da coluna com o valor de venda ##########################")
#print(df_dsa['Valor_Venda'].describe())

# Verificando se há registros duplicados
#print("########################## Verificando se há registros duplicados ##########################")
#print(df_dsa[df_dsa.duplicated()])

# Verificando de há valores ausentes
#print("########################## Verificando de há valores ausentes ##########################")
#print(df_dsa.isnull().sum())

### Qual o Total de Vendas Por Data do Pedido?
### Demonstre o resultado através de um gráfico de barras.
print("########################## Exercicio 02 ##########################")
# Convertendo a coluna 'Data_Pedido' para o tipo de data
df_dsa['Data_Pedido'] = pd.to_datetime(df_dsa['Data_Pedido'], format='%d/%m/%Y')

# Agrupa pela data do pedido
data_Pedido = df_dsa.groupby('Data_Pedido')

# Soma o "Valor_Venda" de todas as vendas referentes aquela data
data_Pedido_Soma = data_Pedido['Valor_Venda'].sum()

# Altera o nome da coluna
data_Pedido_Soma = data_Pedido_Soma.reset_index(name='Soma_Valor_Venda')

# Ordena o data frame pela Data_Pedido
data_Pedido_Soma_Sort = data_Pedido_Soma.sort_values(by='Data_Pedido')

# Criando um gráfico de barras horizontal
plt.barh(y=data_Pedido_Soma_Sort['Data_Pedido'], width=data_Pedido_Soma_Sort['Soma_Valor_Venda'], color="blue", label="Dados de Exemplo")

# Adicionando rótulos aos eixos
plt.xlabel('Soma Valor de Venda')
plt.ylabel('Data do Pedido')

# Adicionando um título ao gráfico
plt.title('Soma de Valor de Venda por Data de Pedido')

# Adicionando uma legenda
plt.legend()

# Exibindo o gráfico
plt.show()