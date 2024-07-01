# Exercise 9-6

from classes import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)

        self.flavours = ['Mango','Vanilla','Chocolate','Strawberry']
    
    def displayFlavours(self):
        for flavour in self.flavours:
            print(flavour,'',end="")

MyIceCream = IceCreamStand('Lal Qila','Chinese')
MyIceCream.displayFlavours()

# Example 9-7 and 9-8

from classes import User

class Admin(User):
    def __init__(self, first_name, last_name, age, profession):
        super().__init__(first_name, last_name, age, profession)

        self.privileges = Privileges()
    
class Privileges():
    def __init__(self,privileges = ["can add post", "can delete post", "can ban user"]):
        self.privileges = privileges

    def showPrivileges(self):
        print("\nAdministrator's Privileges: ")
        for privilege in self.privileges:
            print(privilege,'',end="")

admin1 = Admin('Sara','Ahmed',28,'Engineer')
admin1.privileges.showPrivileges()