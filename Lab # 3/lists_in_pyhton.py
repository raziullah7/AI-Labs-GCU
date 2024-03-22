colors = ['red', 'pink', 'green']
# print(colors)

myList = ['hello', 2, 'world', False]
# print(myList)

# -------------------------------------------------------------------------
# accessing indices
# print(myList[0])
# print(myList[-1])

# -------------------------------------------------------------------------
# functions on lists
colors.append('white')
# print(colors)

colors.remove('red')
# print(colors)

# print(len(colors))

# removes last element or provide index
colors.pop(0)
# colors.pop()
# print(colors)

# -------------------------------------------------------------------------
# sorting lists
num = [1, 3, 5, 4, 9, 2]
# ascending
num.sort()
# descending
num.reverse()
# empties the list
num.clear()
# print(num)

# -------------------------------------------------------------------------
# looping through lists
vals = []

# printing int in ascending order
# for i in range(5):
#     vals.append(int(input(f"Enter Num {i + 1}: ")))
# vals.sort()
# print("Ascending Order: ", vals)

# printing sum of list
sum = 0
for val in vals:
    sum += val
# print("Sum: ", sum)

# joint of 2 lists
anotherVals = [12, 1, 6, 4, 7]

allVals = vals + anotherVals
# print("Joint Vals: ", allVals)

# -------------------------------------------------------------------------
# finding a value from list
# theVal = int(input("Enter The Value to be Searched: "))
# flag = False

# for val in anotherVals:
#     if (val == theVal):
#         flag = True
#         break

# if flag:
#     print(f"${theVal} exists in array")
# else:
#     print(f"${theVal} does not exists in array")
   
# -------------------------------------------------------------------------
# tuples
theColors = ('red', 'pink', 'green',)
# another tuple
anotherColor = 'white',

# -------------------------------------------------------------------------
# list of tuples
# movieList = []

# # getting values
# while (True):
#     title = input("Enter Movie Title: ")
#     movieBudget = input("Enter Movie Movie Budget: ")
#     dirName = input("Enter Movie Director Name: ")
#     releaseYear = input("Enter Movie Release Year: ")
    
#     flag = input("Do you want to add another movie (yes/no): ")
#     if flag.lower == 'no':
#         break

# movieList.append((title, movieBudget, dirName, releaseYear))

# for movie in movieList:
#     print(f"Movie Name: {movie[0]}\nRelease Year: {movie[3]}\n\n")

# -------------------------------------------------------------------------
# function
def Sum(num1, num2):
    return num1 + num2

# def Factorial(n):
#     return Factorial(n * (n - 1))

# print(Factorial(5))

def say_hello(name):
    print("Hello", name)

def palindrome(name):
    return name == name[::-1]
#     if (name == reversed(name)):
#         return True
#     else:
#         return False

print("Is the Name a Palindrome: ", palindrome("madam"))