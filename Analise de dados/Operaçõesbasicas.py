import pandas as pd

data = {
        'alunos':['Eduardo', 'Lucas', 'Guilherme', 'Leozinho', 'Gabriel', 'Enrique'],
        'idade':[24, 26, 20, 22, 20, 26],
        'notas':[10, 10, 8, 7, 10, 6]
        }


df = pd.DataFrame(data, columns=['alunos', 'idade','notas'])


df.describe()


df.drop(5)

df = df.drop(5)



df.drop('idade', axis=1)


df.count()

df.columns

df.shape


df.max()

df['idade'].max()

df.min()

df.mean()

df.median()

df.sum()


df['notas'].add(10)



df['notas'].sub(10)


df['notas'].mul(10)


df['notas'].div(10)


notaparamostrar = df['notas'][0]

print(notaparamostrar)

