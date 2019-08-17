class Mobile:
    model=""
    mobileNo=""
    name=""
list1=[]
m1=Mobile()
m2=Mobile()
m3=Mobile()
m1.model="Samsung S9+"
m1.mobileNo="8169696969"
m1.name="Tim"
m2.model="Iphone 10"
m2.mobileNo="212337714"
m2.name="Bhuban Bam"
m3.model="iphone 12"
m3.mobileNo="70203651445"
m3.name="Hamza"
m4=Mobile()
m4.model="Nokia3310"
m4.name="Hetvi"
m4.mobileNo="6395133291"
list1=[m1,m2,m3,m4]
for mob in list1:
    print(mob.model,mob.name,mob.mobileNo)






