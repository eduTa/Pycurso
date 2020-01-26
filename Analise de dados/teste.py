# -*- coding: utf-8 -*-
import  pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('servicos.csv')

df['Divisão'].describe()
quant = []

df = df.drop('CPC', axis=1)
df = df.drop('Subclasse', axis=1)
print(df['Divisão'])
dados =  []
for i in df['Divisão']:
    print(i)
    dados.append(i)
    
unico = []

for i in dados:
    if not i in unico:
        unico.append(i)

print(unico)
valor = 0;
quant.clear()
for i in range(0, len(unico)):
    valor = 0
    for h in dados:
        if unico[i] == h:
            valor += 1
    quant.append(valor)
plt.plot(unico, quant)
plt.ylabel('quantidade vendida em reais')
plt.xlabel('produtos')
plt.show()
print(quant)    
df['Divisão'].count()