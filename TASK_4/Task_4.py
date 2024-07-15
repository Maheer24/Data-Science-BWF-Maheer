# Store a person’s name in a variable, and print a message to that person. Your message should be simple, such as, “Hello Eric,
# would you like to learn some Python today?”

name = 'Eric'
message = f'Hello {name}, would you like to learn some Python today ?'
print(message)
print('\t') 

# Store a person’s name in a variable, and then print that person’s name in lowercase, uppercase, and titlecase.

print("Upper Case: "+name.upper())
print("Lower Case: "+name.lower())
print("Title Case: "+name.title())
print('\t') 

# Find a quote from a famous person you admire. Print the quote and the name of its author. 
# Your output should look something like the following, including the quotation marks:
# Albert Einstein once said, “A person who never made a mistake never tried anything new.”

famous_person = "Angie Weiland"
quote = "Nature is the purest portal to inner-peace."

print(f"{famous_person} once said, '{quote}'")
print('\t') 

# Store a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each
# character combination, "\t" and "\n", at least once. Print the name once, so the whitespace around the name is displayed.
# Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().

person = '\tMaheer Shakil\n'
print(f'Name with whitespaces: {person}')

print("Name after lstrip() (leading whitespace removed):")
print(person.lstrip())

print("Name after rstrip() (trailing whitespace removed):")
print(person.rstrip())

print("Name after strip() (leading and trailing whitespace removed):")
print(person.strip())

# Write a series of conditional tests. Print a statement
# describing each test and your prediction for the results of each test.

weather = 'sunny'
print("\nIs weather == 'sunny'? I predict True.")
print(weather == 'sunny')

print("Is weather == 'foggy'? I predict False.")
print(weather == 'foggy')
print('\t')

# Imagine you have a list of cars and you want to print out the name of each car. Car names are proper names, so the names of
# most cars should be printed in title case. However, the value 'bmw' should be printed in all uppercase.

cars = ['audi','bmw','subaru','toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
print('\t')

# Store a requested pizza topping in a variable and then print a message if the person did not order anchovies

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")
print('\t')

# Checking Multiple Conditions

age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)
print(age_0 >= 21 or age_1 >= 21 )
print('\t')

# Checking Whether a Value Is in a List

requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)

# if-elif Statements

alien_color = 'red'

if alien_color == 'green':
    print('\nYay! You earned 5 points')

elif alien_color == 'yellow':
    print('Yay! You earned 10 points')

elif alien_color == 'red':
    print('Yay! You earned 15 points')
print('\t')

# Make a list of your favorite fruits, and then write a series of independent if statements that check for 
# certain fruits in your list. Make a list of your three favorite fruits and call it favorite_fruits.
# Write five if statements. Each should check whether a certain kind of fruit is in your list. 
# If the fruit is in your list, the if block should print a statement, such as You really like bananas!

favorite_fruits = ['apple','banana','cherry']

if "apple" in favorite_fruits:
    print("You really like apples!")

if "banana" in favorite_fruits:
    print("You really like bananas!")

if "mango" in favorite_fruits:
    print("You really like mangoes!")

if "strawberry" in favorite_fruits:
    print("You really like strawberries!")

if "cherry" in favorite_fruits:
    print("You really like cherries!")
