import pandas as pd
import numpy as np
df=pd.read_csv("..//data/Student.csv")
df['Total']=df.iloc[:].sum(axix=1)
df['avg']=df['Total']/5

df['Rank']=df['avg'].rank()
df['Result']=np.where((df['M1']>=35)& (df['M2']>=35)&(df['M3']>=35)&(df['M4']>=35)&(df['M5']>=35))
df.soft_values(by=['No'],inplace=True)
