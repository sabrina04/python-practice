#!/usr/bin/python

#example 1
class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00
        
    def full_time_wage(self, hours):
        return super(PartTimeEmployee, self).calculate_wage(hours)
        

milton = PartTimeEmployee("Milton")
print milton.full_time_wage(10)

#example 2
class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
        
    def display_car(self):
        return "This is a %s %s with %s MPG." % (self.color,self.model, str(self.mpg))
        
    def drive_car(self):
        self.condition = "used"

class ElectricCar(Car):
    def __init__(self, battery_type, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
        self.battery_type = battery_type
        
    def drive_car(self):
        self.condition = "like new"
        
my_car = ElectricCar("molten salt","DeLorean", "silver", 88)
print my_car.condition
my_car.drive_car()
print my_car.condition

#example 3
class Point3D(object):
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        
    def __repr__(self):
        return "(%d, %d, %d)"% (self.x, self.y, self.z)
        
my_point = Point3D(1,2,3)
print my_point