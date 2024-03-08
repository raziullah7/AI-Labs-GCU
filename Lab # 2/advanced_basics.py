# if else
# age = input("Enter Age: ")

# if int(age) > 20:
#     print("Eligible")
# elif int(age) < 20:
#     print("Not Eligible")
# else:
#     print("Apply Again")
    
# ---------------------------------------
# direct casting from input
# num = int(input("Enter Number: "))

# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# elif num == 0:
#     print("Zero")
# else:
#     print("NANII!!!")

# ---------------------------------------
# even or odd?
# num = int(input("Enter Number: "))

# if (num % 2):
#     print("Number is Odd!")
# else:
#     print("Number is Even")

# ---------------------------------------
# employee wage?
# weekHours = float(input("Enter no. of hours worked in the week: "))
# hourWage = float(input("Enter the hourly wage: "))

# finalWage = hourWage * weekHours

# if (weekHours > 40):
#     print("Overtime is Due")
#     finalWage = finalWage + ((weekHours - 40) * (hourWage * 1.1))

# print(f"Final Wage: {finalWage}")

# ---------------------------------------
# grade student?
# marks = int(input("Enter Marks Between 1 - 100: "))
# while marks < 0 or marks > 100:
#     marks = int(input("Error! Enter Marks Between 1 - 100: "))

# if marks > 90:
#     print("Grade is A+")
# elif marks > 80:
#     print("Grade is A")
# elif marks > 70:
#     print("Grade is B")
# elif marks > 60:
#     print("Grade is C")
# elif marks > 60:
#     print("Grade is D")
# else:
#     print("Grade is F")

# ---------------------------------------
# tables?
# for i in range(1, 11):
#     print(f"2 * {i} = {2 * i}" )

# ---------------------------------------
# infinite loop
# i = 0
# while i < 10:
#     print("Hello World!")
# i = i + 1

# ---------------------------------------
# conditions in loop
# i = 0
# sum = 0
# while i < 10:
#     if i == 5:
#         sum = sum + i
#     i = i + 1
# print("Sum: ", sum)

# ---------------------------------------
# prime numbers
# i = 2
# isPrime = True
# n = int(input("Enter Number to Check Prime: "))

# while i < n:
#     r = n % i
#     if r == 0:
#         isPrime = False
#         break
#     else:
#         i = i + 1

# if isPrime:
#     print(f"{n} is a Prime Number")
# else:
#     print(f"{n} is not a Prime Number")

# ---------------------------------------
# Finonaucci Series
n = int(input("Enter number for Fibnaucchi Series Sum: "))

while n <= 0:
    n = int(input("Enter a Positive Number for Fibnaucchi Series Sum: "))

if n == 1:
    print("Sum = 1")
else:
    fib_sum = 1  # Sum starts with 1 because the first Fibonacci number is 1
    fib_prev = 0
    fib_current = 1
    for _ in range(2, n + 1):
        fib_next = fib_prev + fib_current
        fib_prev = fib_current
        fib_current = fib_next
        fib_sum += fib_current
    
    print(f"Sum = {fib_sum}")