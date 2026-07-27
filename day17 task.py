class vehicles:
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed
    def show_method(self):
        print(f"{self.brand} is moving")
        print(f"{self.speed} is high")
class car(vehicles):
    def drift(self):
        print(f"{self.brand} is drifting")
class bike(vehicles):
    def wheeling(self):
        print(f"{self.speed} is wheeling")
car=car("BMW",200)
bike=bike("royal enfeild",150)
print(car.show_method)
car.show_method()
print(bike.show_method)
bike.show_method()
car.drift()
bike.wheeling()