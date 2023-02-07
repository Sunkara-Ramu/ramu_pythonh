import pandas as pd
data=pd.read_csv("../data/tips.csv")
#print(data)
#tips_male_fm=data.filter(['tip','sex'])
#print(tips_male_fm.groupby('sex').sum())
#print(tips_male_fm.sex,value_counts())
print(pd.crosstab(index=data['sex'],columns=data['smoker']))
day_wise=data.filter(['tip','day'])
print(day_wise.groupby('day').sum())