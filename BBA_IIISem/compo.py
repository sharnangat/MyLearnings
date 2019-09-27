class A:
    name=""
    city=""
    def __init__(self,name,city):
        self.name=name
        self.city=city

class compo:
    def __init__(self,name,city):
        a=A(name,city)
    def printData(self):
        print(self.name)


c=compo("V","Pune")
c.printData();
        
