""" This module is of Decorators examples """

# ------------------- Decorators ---------------------

# Create a decorator which can delay fun exe by 3sec

'''
from time import sleep


def delayer(function):
    def inner():
        sleep(3)
        function()
    return inner


@delayer
def spam():
    print("Spam fun executed !!!")


@delayer
def display():
    print("Display fun executed !!!")


spam()
display()
'''

# wapt create a decoration which decorates the function with the pattern
'''
---------><-----------
----------------------

        function

---------><------------
-----------------------
'''

'''
def decoration(function):
    def inner(*args, **kwargs):
        print("----------><-----------")
        print("-----------------------")
        function(*args, **kwargs)
        print("-----------------------")
        print("----------><-----------")
    return inner


@decoration
def fun1(*args, **kwargs):
    print(f"Function One is executing....., with {args} and {kwargs}")


@decoration
def fun2(*args, **kwargs):
    print(f"Function Two is executing......, with args of {len(args)} and kwargs of {len(kwargs)}")


# fun1 = decoration(fun1) => if u r not writing @decoration before function definition
fun1(1, 2, 3, a=1, b=2, c=3)
print()
fun2(10, 20, 30, a=10, b=20, c=30)

'''







