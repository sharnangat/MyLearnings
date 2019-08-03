test_list = [[3, 5], [7, 3, 9], [1, 12]]

print("The original list : " + str(test_list)) 
  
# using sorted + list comprehension 
# sort flatten list of list 
res = [k  for i in test_list for k in i]

print(res)
