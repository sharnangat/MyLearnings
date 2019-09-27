class A:
    num1=0
    def __init__(self,n):
        print("Called in A")
        self.num1= n
class B(A):
    num2=0
    def __init__(self,n):
        print("Called in B")
        self.num2= 400
        A.__init__(self,n)
    def printA(self):
        print(self.num1,self.num2)    
class C:
    num3=0
    def __init__(self,n):
        self.num3= n
  

b1=B(200)
b1.printA()
c1=C(300)

    
