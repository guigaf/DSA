# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Carrega o dataset
df_dsa = pd.read_csv('C:/Geral/DEV/DSA/Cap15/dataset.csv')
print("###########################################################################################################################################################################################################")
print("Shape: ", df_dsa.shape)

print("###########################################################################################################################################################################################################")
print("Colums: ", df_dsa.columns)

print("###########################################################################################################################################################################################################")
print("Head: ", df_dsa.head())

print("###########################################################################################################################################################################################################")
print("Info: ", df_dsa.info())

print("###########################################################################################################################################################################################################")
print("Is null: ", df_dsa.isnull().sum())

print("###########################################################################################################################################################################################################")
print("Correlação: ", df_dsa.corr())


print("###########################################################################################################################################################################################################")
print("Describe: ", df_dsa.describe())

print("###########################################################################################################################################################################################################")
print("Describe - horas estudo mês: ", df_dsa["horas_estudo_mes"].describe())

sns.histplot(data = df_dsa, x = "horas_estudo_mes", kde = True)

X = np.array(df_dsa['horas_estudo_mes'])
print("###########################################################################################################################################################################################################")
print("Array - horas estudo mês: ", X)

X = X.reshape(-1, 1)
print("###########################################################################################################################################################################################################")
print("Reshape - horas estudo mês: ", X)

y = df_dsa['salario']
print("###########################################################################################################################################################################################################")
print("Salario: ", y)

plt.scatter(X, y, color = "blue", label = "Dados Reais Históricos")
plt.xlabel("Horas de Estudo")
plt.ylabel("Salário")
plt.legend()
plt.show()

X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size = 0.2, random_state = 42)

print("###########################################################################################################################################################################################################")
print("Shape de X_treino: ", X_treino.shape)

print("###########################################################################################################################################################################################################")
print("Shape de X_teste: ", X_teste.shape)

print("###########################################################################################################################################################################################################")
print("Shape de y_treino: ", y_treino.shape)

print("###########################################################################################################################################################################################################")
print("Shape de y_teste: ", y_teste.shape)

modelo = LinearRegression()

modelo.fit(X_treino, y_treino)

plt.scatter(X, y, color = "blue", label = "Dados Reais Históricos")
plt.plot(X, modelo.predict(X), color = "red", label = "Reta de Regressão com as Previsões do Modelo")
plt.xlabel("Horas de Estudo")
plt.ylabel("Salário")
plt.legend()
plt.show()

score = modelo.score(X_teste, y_teste)
print(f"Coeficiente R^2: {score:.2f}")

print("###########################################################################################################################################################################################################")
print("Deploy do Modelo")

def verifica_horas_estudo():
    while True:
        try:
            horas_de_estudo_int = int(input("Quantas horas de estudo foram realizadas? "))
            return  horas_de_estudo_int
        except ValueError:
            print("Por favor, digite um número inteiro válido.")
            continue

while True:
    horas_estudo_novo = np.array([[verifica_horas_estudo()]])

    salario_previsto = modelo.predict(horas_estudo_novo)

    print(f"Se você estudar cerca de", horas_estudo_novo, "horas por mês seu salário pode ser igual a", salario_previsto)