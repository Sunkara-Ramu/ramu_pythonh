import pandas as pd
d={'Team':["India","Austrlia","Pakistan","Srilanka","England"],'Rank':[1,2,3,4,],'win_per':['60%','55%','45%','35%']}
df=pd.DataFrame(d)
df.rename(columns={"Rank":"Ranking"},inplace=True)
print(df.iloc[:,[0,1]])