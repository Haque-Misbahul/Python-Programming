class Car:

    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1

    def get_brand(self):
        return self.__brand +" !"

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "petrol or diesel"
    
    @staticmethod
    def genaral_description():
        return "Cars are useful"
    
    @property
    def model(self):
        return self.__model
    

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):

        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "electric charge"


my_tesla = ElectricCar("Tesla", "Model S", "85kwh")




# solutin 9 test/answer
# print(isinstance(my_tesla, Car))
# print(isinstance(my_tesla, ElectricCar))

# solution 10 answer
class Battery:
    def battery_info(self):
        return "this is battery"

class Engine:
    def engine_info(self):
        return "This is engine"

class ElectricCarTwo(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla", "Model S")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())


# solutin 8 test
# my_car = Car("Audi", "Q2")
# # my_car.model = "Q3"
# print(my_car.model())

# solutin 7 test
# print(Car.genaral_description())

# solutin 6 test
# audi = Car("Audi", "Q2")
# print(audi.fuel_type())
# print(Car.total_car)


# solutin 5 test
# print(my_tesla.fuel_type())

# audi = Car("Audi", "Q2")
# print(audi.fuel_type())

# solution 4 test
# print(my_tesla.brand)
# print(my_tesla.get_brand())

# solution 3 test
# print(my_tesla.full_name())
# print(my_tesla.battery_size)
# print(my_tesla.brand)
# print(my_tesla.model)

# solution 2 test
# my_car = Car("Audi", "Q2")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

# solution 1 test 
# my_new_car = Car("Volkswogen","Tigun")
# print(my_new_car.brand)
# print(my_new_car.model)