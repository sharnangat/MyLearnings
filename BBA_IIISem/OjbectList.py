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
lst=[a1,a2,a3,a4,a5]
for i in lst:
    print(i.model,i.name)


