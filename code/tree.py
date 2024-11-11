import pandas as pd
import random
df = pd.read_csv('dataSinhv2.csv')

'''
0So tin chi: tu 1 den 4
1Ty le thuc hanh: thap TB cao
2Ky thuat: ABCD
3Phan tich: ABCD
4Thiet ke: ABCD
5Ky nang nhom: ABCD
6Diem chuyen can: thap TB cao
7Diem tong ket: thap TB cao
8Chuyen nganh: He thong thong tin, Cong nghe phan mem, Khoa hoc may tinh, Mang may tinh va truyen thong
'''
CN_list = ["CNPM", "HTTT"]
for i in range(0, 1999):
#Diem chuyen can thap
    if df.iloc[i, 6] != 'thap':
        if df.iloc[i, 0] == '1':
            df.iloc[i, 8] = CN_list[random.randint(0, 1)]
        else:
            if df.iloc[i, 1] == "cao" or df.iloc[i, 1] == "TB":
                df.iloc[i, 8] = "CNPM"
            else: 
                df.iloc[i, 8] = "HTTT"

#Diem chuyen can cao
    else:
        if df.iloc[i, 7] != 'thap':
            if df.iloc[i, 1] == "cao":
                df.iloc[i, 8] = "CNPM"
            else: 
                df.iloc[i, 8] = "HTTT"            
        else:
            if (df.iloc[i, 2] == "A" or df.iloc[i, 2] == "B"):
                df.iloc[i, 8] = "CNPM"
            elif df.iloc[i, 2] == "D":
                df.iloc[i, 8] = "HTTT"
            else:
                if df.iloc[i, 4] != "D":
                    df.iloc[i, 8] = "HTTT"
                elif df.iloc[i, 3] != "D":
                    df.iloc[i, 8] = "HTTT"
                elif df.iloc[i, 5] == "D":
                    df.iloc[i, 8] = "HTTT"
                else :
                    df.iloc[i, 8] = "CNPM"
           
df.to_csv('500_dong_tree/data.csv', encoding='utf-8', index=False)
