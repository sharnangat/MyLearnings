class A:  
    name=""
    address=""
    def __init__(self,n,a):
        print("Base Constructor is called")
        self.name=n
        self.address=a
    def printA(self):
        print("Name",self.name,"Address",self.address)

class B(A):
    
    city=""
    def __init__(self,n,a):
        print("Derived class constructor is called")
        A.__init__(self,n,a)
    
a=B("Vij","Pune")
a.printA()
        
    
