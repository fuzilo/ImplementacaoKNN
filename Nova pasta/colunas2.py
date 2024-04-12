import pandas as pd

df = pd.read_csv('qsar.csv', sep=';')
numero_de_colunas = len(df.columns)

print(f'O arquivo possui {numero_de_colunas} colunas.')
