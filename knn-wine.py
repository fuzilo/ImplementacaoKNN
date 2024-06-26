from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

import numpy as np
import pandas as pd

from sklearn.metrics import accuracy_score

#  Lê um arquivo .csv e o transforma em um Dataframe
dados = pd.read_csv('wine-quality-normalizados.csv', sep=',')

#Exclui os registros que possuem atributos faltantes
dados.dropna(inplace=True)

# Seleciona apenas as colunas que você deseja normalizar (features)
colunas_para_normalizar = dados.columns[:-1]  # Seleciona todas as colunas exceto a última (supondo que a última seja a coluna de classes)

# Inicializa o objeto MinMaxScaler
scaler = MinMaxScaler()

# Normaliza os dados
dados[colunas_para_normalizar] = scaler.fit_transform(dados[colunas_para_normalizar])


#Cria uma matriz x e o vetor Y
x = np.array(dados.iloc[:, 0:-2])  #features
y = np.array(dados.iloc[:,-1])  #classes

#Divisão da base de treinamento e teste
X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.3, train_size=0.7)

#Escolha do modelo a ser utilizado
neighbor = 7
knn=KNeighborsClassifier(neighbor)
knn.fit(X_train,Y_train)
previsoes = knn.predict(X_test)

#Medida de desempenho do modelo: Acurácia

acuracia =  accuracy_score(Y_test, previsoes) *100
print("A acurácia foi %.2f%%" % acuracia)
