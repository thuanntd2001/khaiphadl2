import numpy as np
from gen import *



def read_lines_to_list(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    # Remove any trailing newline characters
    return [line.strip() for line in lines]

# Example usage:
cautruc = './cautruc-d-kodau.csv'  
fieldnames = read_lines_to_list(cautruc)
print(fieldnames)


def phanPhoiChuan(a,b,c):
    d=-1
    while d<1 or d>35:
        d=(int(np.random.normal(a,b,c)))
    return d

def Thuchanh(a):
    if a=='TB':
        return a
    if a=='cao':
        return 'thap'
    if a=='thap':
        return 'cao'    
'''
So tin chi: tu 1 den 4
Ty le ly thuyet: thap TB cao
Ty le thuc hanh: thap TB cao
Ky thuat: ABCD
Phan tich: ABCD
Thiet ke: ABCD
Ky nang nhom: ABCD
Diem chuyen can: thap TB cao
Diem tong ket: thap TB cao
Chuyen nganh: He thong thong tin, Cong nghe phan mem, Khoa hoc may tinh, Mang may tinh va truyen thong
'''
lstSoTinChi= ['1','2','3','4']
lstTyLeLyThuyet= ['thap','TB','cao']
lstTyLeThucHanh= ['thap','TB','cao']
lstKyThuat= ['A','B','C','D']
lstPhanTich= ['A','B','C','D']
lstThietKe= ['A','B','C','D']
lstKyNangNhom= ['A','B','C','D']
lstDiemChuyenCan= ['thap','TB','cao']
lstDiemTongKet= ['thap','TB','cao']
lstChuyenNganh= ['He thong thong tin',' Cong nghe phan mem',' Khoa hoc may tinh',' Mang may tinh va truyen thong']


records = []
for i in range(2000):
    record = { 'So tin chi':'', 'Ty le thuc hanh':'', 'Ky thuat':'', 'Phan tich':''
            , 'Thiet ke':'','Ky nang nhom':'','Diem chuyen can':'','Diem tong ket':'',  'Chuyen nganh':''}
   
    record['So tin chi']=(choose2(lstSoTinChi, 5, 35,35,25))
    record['Ty le thuc hanh']=(choose2(lstTyLeThucHanh, 20,60,20))
 
    record['Ky thuat']=(choose2(lstKyThuat,40,40,10,10))

    record['Phan tich']=(choose2(lstPhanTich,25, 25,25,25))
    record['Thiet ke']=(choose2(lstThietKe, 5, 15,45,35))
    record['Ky nang nhom']=(choose2(lstKyNangNhom, 25, 25,25,25))
    record['Diem chuyen can']=(choose2(lstDiemChuyenCan, 30,30,40))
    record['Diem tong ket']=(choose2(lstDiemTongKet, 30,40,30))

    record['Chuyen nganh']=''
    records.append(record)


with open('dataSinhv2.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(records)
