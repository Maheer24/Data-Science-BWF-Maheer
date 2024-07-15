from classes import Car

# Example 
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super(ElectricCar, self).__init__(make, model, year)

        super().__init__(make,model,year)
        self.battery = Battery()
        

    def fill_gas_tank():
        print("This car doesn't need a gas tank!")

class Battery():
    def __init__(self,battery_size = 70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def upgrade_battery(self):
        if self.battery_size < 85:
            self.battery_size = 85
    
my_tesla = ElectricCar('tesla','model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()

# Example

class Person():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printName(self):
        print(self.fname, self.lname)

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

        self.graduationYear = 2026

    def welcome(self):
        print("Welcome", self.fname, self.lname, "to the class of", self.graduationYear)

x = Person('Maheer','Shakil')
s = Student('Naveera','Shakil')
x.printName()
s.printName()
s.welcome()





