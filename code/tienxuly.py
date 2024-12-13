import pandas as pd
import random
df = pd.read_csv('data.csv')


#1:Phi,2:Uc,3:Au,4:A
lstxoa=[]
lsttt=[1,6,7]

for i in range(1999):
    for j in lsttt:

        if j ==1:
            if df.iloc[i, j] == 'thap': df.iloc[i, j] = random.randint(1, 39)
            if df.iloc[i, j] == 'TB': df.iloc[i, j] = random.randint(40, 60)
            if df.iloc[i, j] == 'cao': df.iloc[i, j] = random.randint(61, 100)

        elif j==6:
            if df.iloc[i, j] == 'thap': df.iloc[i, j] = random.randint(5, 7)
            if df.iloc[i, j] == 'TB': df.iloc[i, j] = random.randint(8, 9)
            if df.iloc[i, j] == 'cao': df.iloc[i, j] = 10
        elif j==7:
            if df.iloc[i, j] == 'thap': df.iloc[i, j] = random.randint(8, 13)/2
            if df.iloc[i, j] == 'TB': df.iloc[i, j] = random.randint(14, 17)/2
            if df.iloc[i, j] == 'cao': df.iloc[i, j] = random.randint(18, 20)/2
           
    
 


    
df.to_csv('tienxuly/data.csv', encoding='utf-8', index=False)
