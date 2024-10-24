import pandas as pd

df = pd.read_excel('CustIDtoLineID.xlsx',sheet_name='CustIDtoLineID',usecols='A,B')
#print(df.dtypes)
#print(df.CustomerID)
#print(df.iloc[:,0])

#print(df.loc[df.CustomerID=='999'].LineID)
#df.CustomerID = df.CustomerID.astype("string")
print(df[df.columns[0:2]])
df[df.columns[0:2]] = df[df.columns[0:2]].astype("string")
print(df.dtypes)
print(df.loc[df.CustomerID=='999'].LineID)

print(df.loc[df.iloc[:,0]=='999'].iloc[0,1])
print(df.loc[df.iloc[:,0]=='99'])

if df.loc[df.iloc[:,0]=='99'].empty : print("None")
else: print("value")
