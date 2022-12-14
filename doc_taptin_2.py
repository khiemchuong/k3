import os
def doc_noi_dung_tap_tin(thumuc:str,ten_tap_tin:str) ->list:
    try:
        f=open(os.path.join(thumuc,ten_tap_tin),'rt')
        content=f.readline()
        f.close()
        return content
    except Exception as e:
        print(e)
        return None

def main():
    path = 'c:\\Users\\DELL\\PycharmProjects\\pythonProject4'
    filename = 'chuong.txt'
    noidung= doc_noi_dung_tap_tin(path, filename)
    if noidung is None:
        print("xảy ra lỗi ")
    else:
        print(noidung)

if __name__=='__main__':
    main()