
list1=['a','b','c']

if "a" in list1:
    print("Element is found")


lst1=[1,2,3]
lst2=[1,2,3]

if lst1==lst2:
    print("Both are equal")

lst3=[1,2,3,4]
lst4=[1,2,3]    

if lst3 > lst4:
    print("list 3 is greater")

list1=[[1,2,3],[4,5,6],[8,9,10]]
list2 =[j for i in list1 for j in i]
list2.reverse()
list2.sort()
print(list2)









