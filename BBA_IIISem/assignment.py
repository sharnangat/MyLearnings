class student:
	PRN=""
	Div=""
	Name=""
lst=[]
validate="Y"
while validate=="Y":
	stu=student()
	check=input("Do you want to create Student Record[Y/N]")
	if check==validate:
		prn=input("Enter your PRN : ")
		div=input("Enter your Div : ")
		name=input("Enter your Name : ")
		stu.PRN=prn
		stu.Div=div
		stu.Name=name
		lst.append(stu)
	else:
	   validate="N"
	   break

for std in lst:
        print(std.PRN)


   
