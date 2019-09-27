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
obj.printData()
obj1=A("A02","Dinesh")
obj1.printData()
obj3=A("A03","Rakesh")
obj3.printData()







