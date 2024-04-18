from math import sin, cos, pi
import time

# list of values using List Comprehension
# we use the long-hand method of reducing the PI to 3 decimal places
# this is because range only allows integer values
xList = [i for i in range(int(-pi*1000), int(pi*1000) + 1)]

# function to return "d/dx sin(x) = sin(x + h) / h"
def derivativeOfSin(x, h):
    return (sin(x+h)) / h


for x in xList:
    h = 0.001
    sinDerivative = derivativeOfSin(x, h)
    cosOfX = cos(x)
    print(f"x = {x}")
    print(f"Value of Derivative of sin(x): {sinDerivative}")
    print(f"Cos of x: {cosOfX}")
    
    # to actually be able to see the starting values and results
    # they get erased due to the terminal's limit
    time.sleep(0.5)   # comment this statement out see fast execution