# Today topic of discussion is about composition
# Composition is concept of using one class into another class
# without using the inheritance

class baseA:
    name=""
    def __init__(self,name):
        print("baseA constructor is called")
        self.name=name
    def printBaseA(self):
        print("Name of college",self.name)

class deriveB:
    city=""
    def __init__(self,city,name):
        self.baseAObject=baseA(name)
        print("DerviceB constructor is called")
        self.city=city
        self.baseAObject.printBaseA()
#instanace of deriveB
baseBobject=deriveB("pune","sicsr")
