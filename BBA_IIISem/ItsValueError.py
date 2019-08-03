class ItsValueError(Exception):
    def __init__(self, message):
        self.message = message
i=1
try:
    if i==1:
        raise ItsValueError("Error is occured")

except ItsValueError as error1:
    print(error1)
    
