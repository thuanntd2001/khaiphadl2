import pandas as pd
import random
df = pd.read_csv('data.csv')
f=open("data.csv")

#1:Phi,2:Uc,3:Au,4:A
lstxoa=[]

for i in range(381):

    if df.iloc[i, 8] == 1:
        df.iloc[i, 8] = "Phi"
    if df.iloc[i, 8] == 2:
        df.iloc[i, 8] = "Uc"
    if df.iloc[i, 8] == 4:
        df.iloc[i, 8] = "Au"
    if df.iloc[i, 8] == 6:
        df.iloc[i, 8] = "A"



    
df.to_csv('data1247.csv', encoding='utf-8', index=False)
