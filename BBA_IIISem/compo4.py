class A:
     #A class constructor
    def __init__(self,basicpay):""" line 1"""
        print("Stataement 4")
        self.basicpay=basicpay

    def getBasicPay(self):
        print("Stataement 5")
        return self.basicpay*2000

class B:
    #B class constrcutor
    def __init__(self,total,bonus,basicpay):
        print("Stataement 1")
        self.a=A(basicpay)   """ this state calling line1"""
        print("Stataement 2")
        print("fetched value from class A",
              self.a.getBasicPay()+bonus)
        print("Value of total",total)
b=B(0,2,2000)
