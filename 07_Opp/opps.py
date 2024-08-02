# How to define a class
class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    
    def fullName(self):
        return f"{self.brand} {self.model}"

# inheritance
class ElectricCar(Car):
    def __init__(self, brand, model,batterySize):
        super().__init__(brand, model)
        self.batterySize=batterySize

myCar=Car("Mahindra","3XO")

ElecCar=ElectricCar("Tesla","Tesla S","800kWh")

print(ElecCar.fullName())