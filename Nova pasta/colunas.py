import pandas as pd

# Leia o arquivo CSV original
df = pd.read_csv('qsara.csv')

# Substitua as vírgulas por ponto e vírgula
#df = df.replace(';', ',', regex=True)

df = df.replace('"', '')

# Salve o novo arquivo CSV com ponto e vírgula como separador
df.to_csv('qsar3.csv', index=False)

print(f'O novo arquivo foi criado com ponto e vírgula como separador: seuarquivo_ponto_virgula.csv')

