import csv
import random
from functools import reduce
from operator import add

# tỷ lệ xuất hiện(c) trong khoảng cách [a,b] của list
# ví dụ màu mắt (đen, nâu, lam) có tỷ lệ xuất hiện là 80% thì hàm sẽ là choose(lstMauMatTuNhien, 0, 2, 80)
def choose(lst, a, b, c):
    
    ran = random.randint(1,100)
    if ran <= c:
        ran = random.randint(a, b)
    else:
        ran = random.randint(b + 1, len(lst)-1)
    return lst[ran]

def choose2(lstThuocTinh, *lstTiLe):
    if reduce(add, lstTiLe) !=100:
        print("Ti le khong khop 100")
        return -1
    else:
        ran = random.uniform(0,100)
        sumTiLe=0
        sumTiLeMoi=0
        for i in range(0,len(lstTiLe)):
            sumTiLeMoi+=lstTiLe[i]
            if sumTiLe<ran < sumTiLeMoi:
                 return lstThuocTinh[i]
            
            sumTiLe=sumTiLeMoi
       
