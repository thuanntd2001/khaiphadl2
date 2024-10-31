import pandas as pd
import random
df = pd.read_csv('data.csv')
f=open("data.csv")

#1:Phi,2:Uc,3:Au,4:A
lstxoa=[]

for i in range(753):

    if df.iloc[i, 8] != 7:
        lstxoa.append(i)
    
    df2=df.drop(lstxoa)
    print(lstxoa)


    
df2.to_csv('tienxuly/dataucphi.csv', encoding='utf-8', index=False)
