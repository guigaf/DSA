import sklearn
from sklearn.datasets import load_iris
import pandas as pd
from os import system, name
import matplotlib.pyplot as plt
import seaborn as sns

# Limpa tela
def limpa_tela():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")
    pass

limpa_tela()
######################################################################################################################################################
fatias = [7, 2, 2, 13]
atividades = ['dormir', 'comer', 'passear', 'trabalhar']
cores = ['olive', 'lime', 'violet', 'royalblue']
plt.pie(fatias, labels=atividades, colors=cores, startangle=90, shadow=False, explode=(0, 0.2, 0, 0))
plt.show()
######################################################################################################################################################

######################################################################################################################################################
dados = sns.load_dataset("tips")
print(dados.head())
sns.set_theme(style="darkgrid")

sns.jointplot(x="total_bill", y="tip", data=dados, kind="reg", truncate=False, xlim=(0, 60), ylim=(0, 12), color="m", height=7)
plt.show()

sns.lmplot(x="total_bill", y="tip", data=dados, col="day")
plt.show()
######################################################################################################################################################