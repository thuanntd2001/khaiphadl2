import numpy as np
from gen import *

def read_lines_to_list(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    # Remove any trailing newline characters
    return [line.strip() for line in lines]

# Example usage:
tenmh = './cautruc-d-kodau.csv'  
fieldnames = read_lines_to_list(tenmh)
print(fieldnames)



lstDiem=["A","B","C","D","A+","B+","C+","D+"]





def phanPhoiChuan(a,b,c,e=10):
    d=-1
    while d<1 or d>e:
        d=(int(np.random.normal(a,b,c)))
    return d





fieldnames = fieldnames
'''So tin chi,Tong tiet,Ly thuyet,Thuc hanh,Ky thuat,Phan tich,
Thiet ke,Ky nang nhom,Diem,Chuyen nganh'''
records = []
for i in range(300):
    record = {}
    for j in range(len(fieldnames)):
        record['So tin chi']=(phanPhoiChuan(4,2,1))

    records.append(record)


with open('dataSinhv2.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(records)
