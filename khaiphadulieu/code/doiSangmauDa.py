import pandas as pd
import random
df = pd.read_csv('dataTuLam.csv')


#1:Phi,2:Uc,3:Au,4:A
lstxoa=[]

for i in range(381):

    if df.iloc[i, 3] <10:
        df.iloc[i, 3] = "Trắng Sáng"
    elif df.iloc[i, 3] <15:
        df.iloc[i, 3] = "Trắng Vàng"
    elif df.iloc[i, 3] <27:
        df.iloc[i, 3] = "Nâu Vừa"
    else:
        df.iloc[i, 3] = "Nâu Sậm"


    
df.to_csv('dataSinhv3.csv', encoding='utf-8', index=False)
