class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand +" !"

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "petrol or diesel"
    

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):

        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "electric charge"


my_tesla = ElectricCar("Tesla", "Model S", "85kwh")

# solutin 5
# print(my_tesla.fuel_type())

# audi = Car("Audi", "Q2")
# print(audi.fuel_type())

# solution 4
# print(my_tesla.brand)
# print(my_tesla.get_brand())

# solution 3
# print(my_tesla.full_name())
# print(my_tesla.battery_size)
# print(my_tesla.brand)
# print(my_tesla.model)

# solution 2 
# my_car = Car("Audi", "Q2")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# solution 1 example 
# my_new_car = Car("Volkswogen","Tigun")
# print(my_new_car.brand)
# print(my_new_car.model)