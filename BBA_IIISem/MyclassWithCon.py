class MyClass:
    """A simple example class"""
    code=""
    name=""
    def __init__(self,name,code):
        print("User Init called.")
        self.name=name
        self.code=code
lst=[]
x=MyClass("1","Vij")
lst.append(x)
x1=MyClass("2","Avi")
lst.append(x1)

i=0
a=MyClass
while i<=len(lst)-1:
    a=lst[i]
    print(a.code, a.name)
    i+=1
