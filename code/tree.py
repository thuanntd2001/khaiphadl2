import pandas as pd
import random
df = pd.read_csv('dataSinhv3.csv')

#1:,2:,3:Au,4

for i in range(0, 2999):
#mat
    if df.iloc[i, 0] != 'Đen':
        df.iloc[i, 9] = "Au"
    else:
#toc
        if df.iloc[i, 2] != 'Đen':
            df.iloc[i, 9] = "Au"
        else:
            if df.iloc[i, 3] == "Trắng Sáng":
                df.iloc[i, 9] = "Au"
            elif df.iloc[i, 3] == "Trắng Vàng":
                if df.iloc[i, 7] == 'Rậm' and  df.iloc[i, 4] == 'Cao':
                    df.iloc[i, 9] = "Au"
                else:
                    df.iloc[i, 9] = "A"
            elif df.iloc[i, 3] =="Nâu Vừa":
                if df.iloc[i, 5] == 'Lượn sóng':
                    df.iloc[i, 9] = "Uc"
                elif df.iloc[i, 2] == 'Nhỏ' :
                    df.iloc[i, 9] = "A"
                elif df.iloc[i, 7] == 'Thưa':
                    df.iloc[i, 9] = "A"
                elif df.iloc[i, 4] == 'Thấp':
                    df.iloc[i, 9] = "A"
                else:
                    df.iloc[i, 9] = "Uc"
            else:
            
                if df.iloc[i, 7] == 'Rậm' and df.iloc[i, 5] == 'Lượn sóng':
                    df.iloc[i, 9] = "Uc"
                else:
                    df.iloc[i, 9] = "Phi"
           
df.to_csv('500_dong_tree/data.csv', encoding='utf-8', index=False)
