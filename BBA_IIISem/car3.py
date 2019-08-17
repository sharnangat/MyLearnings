class Car:
    model=""
    name=""
car_1=Car()
print("Car object values are as follows")
print("Model=",car_1.model)
print("Name =",car_1.name)
car_2=Car()
car_2.model="Celerio"
car_2.name="MarutiSuzuki"

print(car_2.model,car_2.name)

car_1.model="Alto"
car_1.name= car_2.name

print("Model=",car_1.model)
print("Name =",car_1.name)
car_3=car_1

print(car_3.model,car_3.name)
car_3=Car()
print("Car 3 model",car_3.model,"Car 3 name",car_3.name)








