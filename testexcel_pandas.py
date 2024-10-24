import pandas as pd

df = pd.read_excel('CustIDtoLineID.xlsx',usecols='A,B')
print(df.dtypes)
print(df.CustomerID)

print(df.loc[df.CustomerID=='999'].LineID)
df.CustomerID = df.CustomerID.astype("string")
print(df.dtypes)
print(df.loc[df.CustomerID=='999'].LineID)
