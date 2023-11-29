from os import system, name
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import patheffects
import seaborn as sns

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

# Pega dados do data_set
dados = sns.load_dataset("titanic")

# Ordena dados de forma crescente
dados_ordenados_age = dados.sort_values(by='age', ascending=False)

# Ordena dados de forma crescente
dados_ordenados_sex = dados.groupby(by='sex')

#print(list(dados_ordenados_sex))
print(dados.sample(5))

fig, ax = plt.subplots()
#ax.bar(dados_ordenados_sex['age'], dados_ordenados_sex['sex'], label='Dados de Exemplo')

# Definindo cores para cada sexo
cores = {'male': 'blue', 'female': 'red'}

# Criando um gráfico de barras para contar a quantidade de homens e mulheres que sobreviveram ou não
sns.countplot(x='survived', hue='sex', data=dados, palette=cores, ax=ax)

for p in ax.patches:
    ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 10), textcoords='offset points')

# Adicionando uma legenda
ax.legend(title='Survived', loc='upper right')

# Adicionando rótulos aos eixos
ax.set_xlabel('Sex')
ax.set_ylabel('Count')

# Exibindo o gráfico
plt.show()