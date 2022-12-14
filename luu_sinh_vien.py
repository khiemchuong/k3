from studert import SinhVien
import pickle
import os

SV=SinhVien('văn Khiêm Chương',2004,10.0)
path ='c:\\Users\\DELL\\PycharmProjects\\pythonProject4'
filename='chuong.txt'
with open(os.path.join(path, filename),"wb") as f:
    pickle.dump(SV,f)
print('Kết thúc quá trình lưu dữ liệu')