from operationfunctions import *
import operationfunctions

print(operationfunctions.__doc__)
print()
# Using Decorators


def decorators(function):               # using Decorator
    def inner(a, b):
        if a > b:
            return function(a, b)
        else:
            return function(b, a)
    return inner


print("Addition :", add(20, 10))

sub = decorators(sub)
print("Subtraction :", sub(20, 10))
print("Subtraction :", sub(20, 50))

print("Multiplication :", mul(20, 10))
print("Division :", div(20, 10))
print("Floor Division :", floor_div(20, 10))
print("Power :", power(5, 2))
