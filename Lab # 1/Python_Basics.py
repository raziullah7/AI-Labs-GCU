# print("Hello World!")
# print(1)
# print(3.0)
# print('hello!')

a = 5
b = 5.7
c = 'hello'

e = a + b
# print(e)

# power (3 raised to the power 2)
f = 3 ** 2
# print(f)

# ----------------------------------------------------------
# # # TASK1 # # #
# # print age
# age = 22
# print(f"My Age is {age}")

# # print area of circle of radius of 5 units
# area = 3.14 * (5 ** 2)
# print(f"Area of Circle is {area}")

# # print no. of months and weeks in 27 years
# years = 27
# months = years * 12
# weeks = months * 4
# print(f"\nNumber of Years = {years}\nNumber of Months = {months}\nNumber of Weeks = {weeks}")

# ----------------------------------------------------------
# getting input from user
# print("Enter Your Name: ", input())
# name = input()

# name = input("Enter Your Name: ")
# print(name)

# ----------------------------------------------------------
# # # TASK2 # # #
# name = input("Enter Your Name: ")
# age = input("Enter Your Age: ")
# print("Name: ", name)
# print("Age: ", age)

# print('\n')

# name = "Mon prenom est Razi"
# age = "J'ai 22 ans"
# print("Name: ", name)
# print("Age: ", age)

# ----------------------------------------------------------
# type casting
# a = int(3.3)
# b = 'hello'
# c = a + b     # error
# c = str(a) + b
# # c = (a) + str(b)  # error
# # c = (a) + int(b)  # error
# print(c)

# ----------------------------------------------------------
# string manipulation
# what = 'HAAAhhahaha'
# idk = str.format(f"Tis eh lol {what}")    # error
# idk = "Tis eh lol {what}".format(what)    # error

# nom = input("Quel est votre nom: ")

        # # # variables are not working with str.format() # # #
# print("Je m'appelle {}".format("Razi"))

# f-string
# nom = input("Quel est votre nom: ")
# print(f"Je m'appelle {nom}")

# ----------------------------------------------------------
# function calls for string manipulation
idk = '  hello    world '

# # capitalize initial letter of all words
# idk.capitalize()
# print(idk)

# # all letters uppercase
# idk.upper()
# print(idk)

# # all letters lowercase
# idk.lower()
# print(idk)

# # only makes the first letter of the entire string capital
# idk.title()
# print(idk)

# # removing starting and ending spaces (not the spaces between words)
# idk.strip()
# print(idk)

# function chaining
# idk.capitalize().upper().lower().title().strip()
# print(idk)

# ----------------------------------------------------------
# # # TASK2 # # #
greeting = "Hello, world"
print(greeting + '!')

name = input("What is your name? ").title().strip()
print(f"Greetings to the Earthling named {name}!")
print(name)

print("\nI am " + str(29))

title = "Joker"
diector = "Todd Philips"
release_year = 2019

print(f"{title} ({release_year}), directed by {diector}")

# ----------------------------------------------------------