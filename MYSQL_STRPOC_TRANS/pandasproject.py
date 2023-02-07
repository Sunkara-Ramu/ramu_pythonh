import pandas as pd
df=pd.read_csv("..//data/Student.csv")
df['Total']=df.iloc[:].sum(axis=1)
df['avg']=df['Total']/5
print(df)