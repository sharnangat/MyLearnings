class A:
    name=""
    address=""
    def __init__(self,n,a):
        print("Constructor is called")
        self.name=n
        self.address=a
    def printA(self):
        print("Name",self.name,"Address",self.address)
        

a=A("Vij","Pune")
a.printA()
        
    
