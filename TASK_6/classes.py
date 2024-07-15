# Creating a class Dog

class Dog():

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title()+ " is now sitting.")

    def roll_over(self):
        print(self.name.title()+" rolled over!")

myDog = Dog('Willie',6)
print("My dog's name is "+str(myDog.name))
print(str(myDog.name) + " is "+ str(myDog.age) + " years old.")
myDog.sit()
myDog.roll_over()

# Excercise 9-1 and 9-4

class Restaurant():

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} is serving {self.cuisine_type.title()}")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()} is now open!")

    def set_number_served(self, served):
        self.number_served = served
    
    def increment_number_served(self, served):
        self.number_served += served

    def get_number_served(self):
        print(f"{self.restaurant_name.title()} served {str(self.number_served)} people.")

restaurant = Restaurant('Lal Qila', 'Chinese')

print(f"\nRestaurant's name is {restaurant.restaurant_name.title()}.")
print(f"{restaurant.restaurant_name.title()} serves {restaurant.cuisine_type.title()}.")

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.get_number_served()

restaurant.set_number_served(50)
restaurant.get_number_served()

restaurant.increment_number_served(20)
restaurant.get_number_served()

# Excercise 9-3

class User():
    def __init__(self,first_name,last_name,age,profession):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.profession = profession

    def describe_user(self):
        print(f"\n{self.first_name.title()} {self.last_name.title()} is a/an {self.profession.title()} by profession and is {self.age} years old")

    def greet_user(self):
        print(f"Greetings! {self.first_name} {self.last_name}.")

user1 = User('Sara','Khan',25,'Artist')
user1.describe_user()
user1.greet_user()

# Example (Creating a class Car)

class Car():

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {str(self.odometer_reading)} miles on it.")

    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
        self.odometer_reading += miles
    
myCar = Car('audi','a4',2016)
print(myCar.get_descriptive_name())

myCar.update_odometer(23)
myCar.read_odometer()

myCar.increment_odometer(100)
myCar.read_odometer()


