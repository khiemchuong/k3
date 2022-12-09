#1
import os

def bai_tap1():
    a="khiêm chương"

    b=open("thu.txt",mode="w",encoding="utf-8")
    b.write(a)
#2
def bai_tap2():
    b = open("thu.txt", mode="w", encoding="utf-8")
    print(os.getcwd())
#3
def bai_tap3():
    c = [" đẹp trai"]
    b = open("thu.txt", mode="w", encoding="utf-8")
    b.writelines(c)
    b.close()

#4
def bai_tap4():
    b = open("thu.txt", mode="r", encoding="utf-8")
    print(b.read())
#5
def bai_tap5():
    import numpy as np
    v1=np.random.randint(start=-1000,stop=1000,size=1000)
    b = open("thu.txt", mode="w", encoding="utf-8")
    t=0
    for i in range(100):
        for J in range(0,10):
            b.write(f"{v1[t]}, ")
            t=t+1
        b.write('\n')
    b=open('thu.txt',mode="r")
    for sua in b.readline():
        print(sua.replace(',',"\t"))
def main:
    bai_tap1()
    bai_tap2()
    bai_tap3()
    bai_tap4()
    bai_tap5()
if __name__=='__main__':
    main()