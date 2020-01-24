# -*- coding: utf-8 -*-
import  pandas as pd

df = pd.read_csv('servicos.csv')

df.describe()

df.count()

df = df.drop('CPC', axis=1)
df = df.drop('Subclasse', axis=1)

df.columns

