# Imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

df_dsa = pd.read_csv('C:/Geral/DEV/DSA/Cap14/dataset.csv')

print(df_dsa.shape)

print(df_dsa.columns)

print(df_dsa.head())

print(df_dsa.info())

print(df_dsa.isnull().sum())

print(df_dsa.describe())

print(df_dsa["valor_aluguel"].describe())

# Histograma da variável alvo
sns.histplot(data = df_dsa, x = "valor_aluguel", kde = True)
plt.show()
# Correlação entre as variáveis
print(df_dsa.corr())

# Vamos analisar a relação entre a variável de entrada area_m2 e a variável alvo valor_aluguel
sns.scatterplot(data = df_dsa, x = "area_m2", y = "valor_aluguel")
plt.show()

print(df_dsa.head())
# Definimos a variável dependente
y = df_dsa["valor_aluguel"]
# Definimos a variável independente
X = df_dsa["area_m2"]
# O Statsmodels requer a adição de uma constante à variável independente
X = sm.add_constant(X)
# Criamos o modelo
modelo = sm.OLS(y, X)
# Treinamento do modelo
resultado = modelo.fit()
print(resultado.summary())

# Plot
plt.figure(figsize = (12, 8))
plt.xlabel("area_m2", size = 16)
plt.ylabel("valor_aluguel", size = 16)
plt.plot(X["area_m2"], y, "o", label = "Dados Reais")
plt.plot(X["area_m2"], resultado.fittedvalues, "r-", label = "Linha de Regressão (Previsões do Modelo)")
plt.legend(loc = "best")
plt.show()