from MyPyPackage.operationfunctions import *
from MyPyPackage import operationfunctions

print(operationfunctions.__doc__)

print()
print("Addition :", add(20, 10))
print("Subtraction :", sub(20, 10))
print("Subtraction :", sub(20, 50))
print("Multiplication :", mul(20, 10))
print("Division :", div(20, 10))
print("Floor Division :", floor_div(20, 10))
print("Power :", power(5, 2))

