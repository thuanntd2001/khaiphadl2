import numpy as np
from gen import *

def read_lines_to_list(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    # Remove any trailing newline characters
    return [line.strip() for line in lines]

# Example usage:
tenmh = '../tenmh-doc.csv'  
lstTenmh = read_lines_to_list(tenmh)
print(lstTenmh)



lstDiem=["A","B","C","D","A+","B+","C+","D+"]





def phanPhoiChuan(a,b,c):
    d=-1
    while d<1 or d>10:
        d=(int(np.random.normal(a,b,c)))
    return d





fieldnames = lstTenmh

records = []
for i in range(300):
    record = {}
    for j in range(len(fieldnames)):
        record[fieldnames[j]]=(phanPhoiChuan(10,6,1))

    records.append(record)


with open('dataSinhv2.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(records)
