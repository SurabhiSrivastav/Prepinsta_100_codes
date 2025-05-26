import math
num= int(input('Enter a number: '))

if math.ceil(math.sqrt(num))==math.floor(math.sqrt(num)):
    print(f"{num} is a perfect square number")
else:
    print("It's not a perfect square")

# alternate
from math import sqrt

def isPerfectSquare(x):
    if x>=0:
        sqr=int(sqrt(num))
        return (sqr*sqr)==num
    return False

if isPerfectSquare(num):
    print(True)
    print(f"{num} is a perfect square number")
else:
    print(False)