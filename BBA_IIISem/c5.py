class A:
    number1=0
    number2=0
    def __init__(self,n1,n2):
        print("Constructor in Base class called")
        self.number1=n1
        self.number2=n2
class B(A):
    number3=0
    number4=0
    def __init__(self,n3,n4):
        print("Constructor in Derived class called")
        self.number3=n3
        self.number4=n4
        A.__init__(self,n3,n4)
    def printData(self):
        print(self.number1,self.number2,self.number3,self.number4)

derivedObject=B(1,2)
derivedObject.printData()
    
    
    
