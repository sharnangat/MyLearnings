class A:
    def printA():
        print("called first")
    def printA(self,fname):
        print("called second")
    def printA(self,fname,sname):
        print("called third")
    
   
a=A()
a.printA("SICSR","College")
        
