import pandas as pd
import numpy as np
df=pd.read_csv("..//data/submission (1).csv")
#print(df)
#print(df.shape)
df.drop(['Cabin'],axis=1,inplace=True)
df.fillna(method='ffill',inplace=True)
#print(df.isna().sum())
#print(df.groupby(['Sex','Survived'])['Survived'].count())
print(pd.pivot_table(df,index=['Sex','Age'],aggfunc=np.sum))
print(df.sort_values(by=['Pclass','Age'],ascending=False))