class SinhVien:
  def __init__(self,fullname:str,yob: int,score:float):
    self.hoten=fullname
    self.namsinh=yob
    self.dtb=score
  def __str__ (self) -> str:
    message='[hoten:'+self.hoten+';namsinh:'\
            +str(self.namsinh)+';dtb:'\
            +str(self.dtb)+']'
    return message
  def __gt__(self,other):
      return(self.dtb>other.dtb)
  def __ge__(self,other):
      return(self.dtb>=other.dtb)
  def __lt__(self,other):
      return(self.dtb<other.dtb)
  def __le__(self,other):
      return(self.dtb<=other.dtb)
  def __eg__(self,other):
      return(self.dtb==other.dtb)
