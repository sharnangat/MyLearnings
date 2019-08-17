class Person:
    fname=""
    sname=""
    def __init__(self,f,s):
        self.fname=f
        self.sname=s
    def printData(self):
        print(self.fname,self.sname)
class Student(Person):
    tname=""
    def __init__(self,f,s):
        self.tname=f
        Person.__init__(self,f,s)
    def printStd(self):
        print(self.tname)
    

p1=Person("Sanjay","Vijay")
p1.printData()

p2=Student("A")

p2.printStd()
