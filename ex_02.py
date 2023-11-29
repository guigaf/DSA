from os import system, name
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import patheffects
import seaborn as sns
import random as rd

# Limpa tela
def limpa_tela():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")
    pass

limpa_tela()

# Verifica os dada_sets disponiveis para uso
print(sns.get_dataset_names())

# Gerando dados aleatórios para duas variáveis (X e Y)
np.random.seed(42)
dados_X = np.random.rand(100)
dados_Y = 2 * dados_X + 1 + 0.1 * np.random.randn(100)  # Adicionando um pouco de ruído aos dados

# Ajustando uma linha de tendência (polinômio de primeiro grau)
coeficientes = np.polyfit(dados_X, dados_Y, 1)
linha_tendencia = np.poly1d(coeficientes)

# Criando um gráfico de dispersão
plt.scatter(dados_X, dados_Y, label="Dados de Exemplo", color="blue")

# Adicionando uma linha de tendência
plt.plot(dados_X, linha_tendencia(dados_X), color='red', label='Linha de Tendência')

# Adicionando rótulos aos eixos
plt.xlabel('Variável X')
plt.ylabel('Variável Y')

# Adicionando um título ao gráfico
plt.title('Gráfico de Dispersão')

# Adicionando uma legenda
plt.legend()

# Exibindo o gráfico
plt.show()