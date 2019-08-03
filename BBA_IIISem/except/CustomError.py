class MyError(Exception): 
    # Constructor or Initializer 
    def __init__(self, value):
        self.value = value
        print("value in function",self.value)             

    # __str__ is to print() the value 
    def __str__(self): 
        return(repr(self.value)) 
i=1 
try:
    
    
    if i==1:
        raise(MyError(1)) 
  
# Value of Exception is stored in error 
except MyError as error: 
    print('A New Exception occured: ',error.value)
