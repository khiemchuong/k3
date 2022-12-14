import os
path ='c:\\Users\\DELL\\PycharmProjects\\pythonProject4'
filename='chuong.txt'
#1
#f=open("c:\\Users\\DELL\\PycharmProjects\\pythonProject4\\chuong.txt",'rt')
#content=f.readlines()
#f.close()
#print(content)
#2
with open(os.path.join(path,filename),'rt') as f:
    content=f.readlines()
print(content)
#3
#try:
#    f=open(os.path.join(path,filename),'rt')
 #   content=f.readlines()
  #  f.close()
  #  print(content)
#except Exception as e:
 #   print('Error:',e)

#print('Kết thúc chương trình')