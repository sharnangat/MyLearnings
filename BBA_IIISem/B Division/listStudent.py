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

a2=Student()
a2.rollno="18030122009"
a2.name="Ankur"
a2.accounts=70
a2.economics=80
a2.dbms=90


a3=Student()
a3.rollno="18030122071"
a3.name="Sejal"
a3.accounts=100
a3.economics=100
a3.dbms=100

lst=[a1,a2,a3]
for std in lst:
    print(std.rollno,std.name,std.accounts,std.economics,std.namedbms)



