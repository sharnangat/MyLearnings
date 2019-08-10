class student:
	PRN=""
	Div=""
	Name=""
	python=0
	hrm=0
	php=0
	mysql=0
	ittb=0
	total=0
	per=0.0
	
lst=[]
validate="Y"
j=1
while j<=5:
    stu=student()
    print("Enter new student details",j)
    prn=input("Enter your PRN : ")
    div=input("Enter your Div : ")
    name=input("Enter your Name : ")
    print("Enter subject marks")
    python=input("Python:")
    hrm=input("hrm:")
    php=input("php:")
    mysql=input("mysql:")
    ittb=input("ittb:")
    stu.PRN=prn
    stu.Div=div
    stu.Name=name
    stu.python=python
    stu.hrm=hrm
    stu.php=php
    stu.mysql=mysql
    stu.ittb=ittb
    stu.total =stu.python+stu.hrm+stu.php+stu.mysql+stu.ittb
    stu.per=stu.total/5
    lst.append(stu)
    j+=1

print("Details of students entered from you are")
print("PRN  Div Name")
for std in lst:
        print(std.PRN,std.Div,std.Name)


   
