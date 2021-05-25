import pandas as pd
from pandas import Series
a = pd.read_excel('./masksaledata.xlsx')
print(a.head(8))
print(a)
# a.to_csv('./datamasksale.csv')