class Vehicle: #parent
    #parent attributes
    def __init__(self, wheels, capacity, make, model):
        self.wheels = wheels
        self.capacity = capacity
        self.make = make
        self.model = model
        self.mileage = 0
        #parent methods
    def drive(self,miles):
        self.mileage += miles
        return self
    def reverse(self,miles):
        self.mileage -= miles
        return self
        #child bike inherited parent vehicle
        # create new attribute vehicle_type and return bike
class Bike(Vehicle):
    def vehicle_type(self):
        return "Bike"
class Car(Vehicle):
    def set_wheels(self):
        self.wheels = 4
        return self
class Airplane(Vehicle):
    def fly(self, miles):
        self.mileage += miles
        return self
# like product assignment, make v as "instance" of class vehicle
# v is instance of class
v = Vehicle(4,8,"dodge","minivan")
print(v.make)
# bike inherited parent class vehicle
# create its own attribute vehicle type
# need to print becuase no display methods existed
# print(subclass b invoke its own function vehicle type, return bike value, which is not exsited in parent class vehicle's attribute
b = Bike(2,1,"Schwinn","Paramount")
print(b.vehicle_type())
# c is subclass of class with 8 wheels
# the function set_wheel modify inherant attribute "wheel" from class
# c invoke its own func set_wheels, which is modified as 4
c = Car(8,5,"Toyota", "Matrix")
c.set_wheels()
print(c.wheels)
# a is sub class of class
# new methods fly(), which added new value on existing mileage
a = Airplane(22,853,"Airbus","A380")
a.fly(580)
print(a.mileage)