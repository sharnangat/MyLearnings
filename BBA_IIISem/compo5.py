


class  baseA:
    def __init__(self,name):
        print("2 Called the baseA Constructor")
        self.name=name
    def printName(self):
        print("3 Printed value of Name")
        print("4 Name is",self.name)
     
class derivedB:
    def __init__(self,name):
        print("1 Received Name",name)
        self.b=baseA(name)
        self.b.printName() 

c=derivedB("SICSR")








    
        
