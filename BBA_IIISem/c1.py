class A:
    prnno=""
    name=""
    def __init__(self,prnno,name):
        print("called constructor and passing values")
        self.prnno=prnno
        self.name=name
    def printA(self):
        print("Values of the student")
        print(self.prnno, self.name)

        

obj1=A("A00001","Sejal")
obj1.printA()

obj2=A("B0001","Atmica")
obj2.printA()
    
    
    
