from studert import SinhVien
import pickle
import os

path ='c:\\Users\\DELL\\PycharmProjects\\pythonProject4'
filename='chuong.txt'

with open(os.path.join(path,filename),'rb') as f:
    SV= pickle.load(f)
print(type(SV))
print(SV)
print('Kết thúc quá trình lưu dữ liệu')