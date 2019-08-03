class Student:
    rollno=""
    name=""
    accounts=0
    economics=0
    dbms=0
    total=0
    per=0.0
a1=Student()
a1.rollno="18030122003"
a1.name="Aatmica"
a1.accounts=80
a1.economics=90
a1.dbms=100

a1.total= a1.accounts+a1.economics+a1.dbms
a1.per= a1.total/3

a2=Student()
a2.rollno="18030122009"
a2.name="Ankur"
a2.accounts=70
a2.economics=80
a2.dbms=90

a2.total= a2.accounts+a2.economics+a2.dbms
a2.per= a2.total/3

a3=Student()
a3.rollno="18030122071"
a3.name="Sejal"
a3.accounts=100
a3.economics=100
a3.dbms=100

a3.total= a3.accounts+a3.economics+a3.dbms
a3.per= a3.total/3

print("Student 1 details are below")
print(a1.rollno, a1.name, a1.total, a1.per)

print("Student 2 details are below")
print(a2.rollno, a2.name, a2.total, a2.per)

print("Student 3 details are below")
print(a3.rollno, a3.name, a3.total, a3.per)







