import numpy as np
from gen import *


lstMauMatTuNhien=["Đen","Lam","Vàng"]
lstKieuMat=["To","Nhỏ"]
lstMauTocTuNhien=["Đen","Vàng","Đỏ"]
lstRauTocLong=["Rậm", "Thưa"]
lstKieuMuiTuNhien=["Cao","Thấp"]
lstKieuTocTuNhien=["Xoăn","Thẳng","Lượn sóng"]
lstKieuMoi=["Dày","Mỏng"]
lstMauDa=["Trắng Sáng","Trắng Vàng","Nâu Vừa", "Nâu Sậm"]
lstKieuKhuonMat=["Dài","Dô","Ngắn","Bẹt"]



def phanPhoiChuan(a,b,c):
    d=-1
    while d<1 or d>35:
        d=(int(np.random.normal(a,b,c)))
    return d


#lstChungToc=[1:"Đại chủng Xích đạo Phi",2:"Đại chủng Xích đạo Úc",3:"Hợp nhóm chuyên tiếp giữa các đại chủng Xích đạo đại chủng Âu",4:"Đại chủng Âu",5:"Hợp nhóm chuyển tiếp giữa Âu và Á",6:"Đại chủng Á",7:"Hợp nhóm chuyển tiếp giữa đại chủng Á và Xích đạo"]
#https://vi.wikipedia.org/wiki/M%C3%A0u_da


fieldnames = [ 'Màu Mắt','Kiểu Mắt', 'Màu Tóc Tự Nhiên', 'Màu Da', 'Kiểu Mũi'
            , 'Kiểu Tóc', 'Kiểu Môi','Râu Tóc Lông','Kiểu Khuôn Mặt', 'Chủng Tộc']

records = []
for i in range(3000):
    record = { 'Màu Mắt':'','Kiểu Mắt':'', 'Màu Tóc Tự Nhiên':'', 'Màu Da':'', 'Kiểu Mũi':''
            , 'Kiểu Tóc':'','Kiểu Môi':'','Râu Tóc Lông':'','Kiểu Khuôn Mặt':'',  'Chủng Tộc':''}
   
    record['Màu Mắt']=(choose2(lstMauMatTuNhien, 90, 8,2))
    record['Kiểu Mắt']=(choose2(lstKieuMat, 40,60))
    record['Màu Tóc Tự Nhiên']=(choose2(lstMauTocTuNhien, 90,8,2))
    #record['Màu Da']=(int(np.random.normal(24,5, 1)))
    #record['Màu Da']=(choose2(lstMauDa, 5,20,35,40))
    record['Màu Da']=(phanPhoiChuan(24,6,1))

    record['Kiểu Mũi']=(choose2(lstKieuMuiTuNhien,20, 80))
    record['Kiểu Tóc']=(choose2(lstKieuTocTuNhien, 40,30,30))
    record['Kiểu Môi']=(choose2(lstKieuMoi, 60,40))
    record['Râu Tóc Lông']=(choose2(lstRauTocLong, 70,30))
    record['Kiểu Khuôn Mặt']=(choose2(lstKieuKhuonMat, 25,20,15,40))

    record['Chủng Tộc']=''
    records.append(record)


with open('dataSinhv2.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(records)
