import pandas as pd
import random
df = pd.read_csv('dataTongHop.csv')


#1:Phi,2:Uc,3:Au,4:A
lstxoa=[]

for i in range(753):

    if df.iloc[i, 8] == 3 or df.iloc[i, 8] == 5 or df.iloc[i, 8] == 7 or df.iloc[i, 1] == "Vừa":
        lstxoa.append(i)
    
    df2=df.drop(lstxoa)
    print(lstxoa)


    
df2.to_csv('tienxuly/data.csv', encoding='utf-8', index=False)
