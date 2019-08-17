lst=[1,2,3,4,5,6,7,8,9,10]
oddList=[]
evenList=[]

for i in lst:
    if i%2==0:
        evenList.append(i)
    if i%2!=0:
        oddList.append(i)
   

j=0
print("Odd List",oddList)
print("Even List",evenList)
oddList=[]
evenList=[]

while j<=len(lst)-1:
    if lst[j]%2==0:
        evenList.append(lst[j])
    if lst[j]%2!=0:
        oddList.append(lst[j])
    j+=1


print("Odd List",oddList)
print("Even List",evenList)



