class Car:
    model=""
    name=""
a1=Car()
a1.model="Alto"
a1.name="Suzuki"
a2=Car()
a2.model="Polo"
a2.name="Volkwagen"
a3=Car()
a3.model="Celerio"
a3.name="Suzuki"
a4=Car()
a4.model="K10"
a4.name="Suzuki"
a5=Car()
a5.model="Ertiga"
a5.name="Suzuki"
lst=[]
lst.append(a1)
lst.append(a2)
lst.append(a3)
lst.append(a4)
lst.append(a5)
i=0
while i<=len(lst)-1:
    a6=lst[i]
    print(lst[i].model,lst[i].name,a6.model,a6.name)
    i+=1


