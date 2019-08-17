"""parent class - Base class"""  
class A:
    rollno=""
""" child Class  -Derived class"""
class B(A):
    name=""

class C(B):
    div=""
    
b=C()

b.rollno="A0001"
b.name="SICSR"
b.div="A"

print(b.rollno,b.name,b.div)

