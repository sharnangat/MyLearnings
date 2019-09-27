class A:
    prnno=""
    name=""
    #below is constructor
    def __init__(self,prnno,name):
        print("called constructor")
        self.prnno=prnno
        self.name=name
    def printData(self):
        print("PRN No",self.prnno," Name ",self.name)
        
# instance of the class
lst=[]
obj=A("A01","Ramesh")
lst.append(obj)
obj1=A("A02","Dinesh")
lst.append(obj1)
obj2=A("A03","Rakesh")
lst.append(obj2)
for k in lst:
    k.printData()
      









