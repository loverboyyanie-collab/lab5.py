
# Activity 5: Vehicle and Car
# Demonstrating the Four Pillars of OOP

# Parent Class
class Vehicle:
    # Encapsulation
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    # Abstraction
    def start(self):
        print("Vehicle is starting.")


# Child Class
class Car(Vehicle):
    # Polymorphism
    def start(self):
        print("Car engine is starting.")


# Main Program
vehicle = Vehicle("Toyota", 100)
car = Car("Honda", 120)

vehicle.start()
car.start()
