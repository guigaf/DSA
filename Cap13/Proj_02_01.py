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

### Qual Cidade com Maior Valor de Venda de Produtos da Categoria 'Office Supplies'?
print("########################## Exercicio 01 ##########################")

office_Supplies = df_dsa.query('Categoria == "Office Supplies"')

cidade_groupBy_Sum = office_Supplies.groupby(['Cidade'])['Valor_Venda'].sum()
print(cidade_groupBy_Sum)
cidade = cidade_groupBy_Sum.idxmax()
print("A cidade com Maior Valor de Venda de Produtos da Categoria Office Supplies é: ", cidade)