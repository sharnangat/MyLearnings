class Student:
    prn=""
    name=""
    
lst=[]

validate="Y"
while validate=="Y":
    check=input("Do you want to add student[Y/N]")
    if check==validate:
        std=Student()
        print("Enter student information")
        prn=input("enter prn")
        name=input("enter name")
        std.prn=prn
        std.name=name
        lst.append(std)
     else:
        validate=="N"
    

    


    
