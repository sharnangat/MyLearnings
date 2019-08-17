class Student:
    rollno=""
    name=""
    accounts=0
    economics=0
    dbms=0
    python=0
    cswt=0
    statistics=0
    total=0
    perc=0
    
a1=Student()
a1.rollno="01"
a1.name="Harsha Malika"
a1.accounts=90
a1.economics=40
a1.dbms=50
a1.python=70
a1.cswt=89
a1.statistics=50
a1.total=a1.accounts+a1.economics+a1.dbms+a1.python+a1.cswt+a1.statistics
a1.perc=a1.total/6


a2=Student()
a2.rollno="02"
a2.name="Harika"
a2.accounts=70
a2.economics=40
a2.dbms=70
a2.python=65
a2.cswt=88
a2.statistics=90
a2.total=a2.accounts+a2.economics+a2.dbms+a2.python+a2.cswt+a2.statistics
a2.perc=a2.total/6


a3=Student()
a3.rollno="03"
a3.name="Hasini"
a3.accounts=67
a3.economics=89
a3.dbms=40
a3.python=77
a3.cswt=99
a3.statistics=100
a3.total=a3.accounts+a3.economics+a3.dbms+a3.python+a3.cswt+a3.statistics
a3.perc=a3.total/6


a4=Student()
a4.rollno="04"
a4.name="Vaisnavi"
a4.accounts=89
a4.economics=90
a4.dbms=56
a4.python=100
a4.cswt=88
a4.statistics=50
a4.total=a4.accounts+a4.economics+a4.dbms+a4.python+a4.cswt+a4.statistics
a4.perc=a4.total/6


a5=Student()
a5.rollno="05"
a5.name="Riya"
a5.accounts=66
a5.economics=50
a5.dbms=69
a5.python=77
a5.cswt=60
a5.statistics=100
a5.total=a5.accounts+a5.economics+a5.dbms+a5.python+a5.cswt+a5.statistics
a5.perc=a5.total/6

a6=Student()
a6.rollno="06"
a6.name="Rahul"
a6.accounts=65
a6.economics=78
a6.dbms=60
a6.python=88
a6.cswt=100
a6.statistics=90
a6.total=a4.accounts+a4.economics+a4.dbms+a4.python+a4.cswt+a4.statistics
a6.perc=a6.total/6

a7=Student()
a7.rollno="07"
a7.name="Kriti"
a7.accounts=56
a7.economics=78
a7.dbms=89
a7.python=80
a7.cswt=90
a7.statistics=100
a7.total=a7.accounts+a7.economics+a7.dbms+a7.python+a7.cswt+a7.statistics
a7.perc=a7.total/6


a8=Student()
a8.rollno="08"
a8.name="Vidhi"
a8.accounts=67
a8.economics=78
a8.dbms=89
a8.python=98
a8.cswt=90
a8.statistics=70
a8.total=a8.accounts+a8.economics+a8.dbms+a8.python+a8.cswt+a8.statistics
a8.perc=a8.total/6

a9=Student()
a9.rollno="09"
a9.name="Rohan"
a9.accounts=56
a9.economics=87
a9.dbms=90
a9.python=78
a9.cswt=70
a9.statistics=69
a9.total=a9.accounts+a9.economics+a9.dbms+a9.python+a9.cswt+a9.statistics
a9.perc=a9.total/6

a10=Student()
a10.rollno="10"
a10.name="Priya"
a10.accounts=50
a10.economics=89
a10.dbms=98
a10.python=78
a10.cswt=89
a10.statistics=90
a10.total=a10.accounts+a10.economics+a10.dbms+a10.python+a10.cswt+a10.statistics
a10.perc=a10.total/6


lst=[a1,a2,a3,a4,a5,a6,a7,a8,a9,a10]
for std in lst:
	print(std.rollno,std.name,std.accounts,std.economics,std.dbms,std.python,std.cswt,std.statistics,std.total,std.perc)                                                             
	if std.perc>=80:
		print("A++ grade")
	elif std.perc>=70:
		print("A grade")
	elif std.perc>=60:
		print("B grade")
	elif std.perc>=50:
		print("C grade")
	elif std.perc>=35:
		print("D grade")
	else:
		print("Fail")
		
