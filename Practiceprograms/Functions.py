# Define a function to search for char in a given string and return the corresponding index
'''
def index(string, val, start=0, end=-1):
    if end == -1:
        end = len(string)
    i = start
    while i < end:
        char = string[i]
        if char == val:
            return i
        i += 1
    else:
        raise ValueError


print(index("hello", 'l', 4, 6))
'''

# ------------------------ FUNCTIONS ASSIGNMENT --------------------------

# ● Define a function returns the data type of the given argument

'''
def display(value):
    if isinstance(value, (str, tuple, list, dict, int, float, bool, complex, set)):
        return type(value)


print(display([100, 'hi']))
print(display(100))
print(display((100, 'hi')))
print(display({100, 'hi'}))
'''

# ● Define a function which takes any number and returns if the number is a PALINDROME not

'''
def palindrome(num):
    s = str(num)
    s1 = s[::-1]
    if num == int(s1):
        print(f" {num} Number is palindrome")
    else:
        print(f" {num} Number is not palindrome")


palindrome(121)
palindrome(1251)
palindrome(1552551)
'''


# ● Define a function which takes any iterable and returns the length of the iterable
# ( without using len function )

'''
def length(iterable):
    count = 0
    for i in iterable:
        count += 1

    print(count)


length("Hello")
length(["Hello", 1, 2, 3])
length({"Hello", 1, 2, 3, 4, "hi"})
'''


# ● Define a function which takes 4 inputs from the user and returns the average of the inputs
'''
def avg(n1, n2, n3, n4):
    print("The average of given four numbers is :", (n1+n2+n3+n4)/4)


avg(2, 2, 4, 4)
'''

'''
def avg(*args):
    n = len(args)
    print(sum(args)/n)


avg(2, 2, 2, 2)
'''

# ● Define a function which takes 2 arguments start, stop and prints all the numbers from
# Start to stop (take only positive arguments)

'''
def print_num(start, end):
    while start <= end:
        print(start)
        start += 1


print_num(1, 20)
'''

# ● Define a function which will take string "After all, tomorrow is another day!”
# as argument and calculates the sum of all the consonants indices

'''
def sum_of_con(string):
    sum1 = 0
    for i in string:
        if i not in "aeiouAEIOU":
            sum1 += string.index(i)
    print(f"{string} :: Consonants indices summation is :", sum1)


sum_of_con("After all, tomorrow is another day!")
sum_of_con("hqwr")
'''

'''
o/p:
After all, tomorrow is another day! :: Consonants indices summation is : 272
hqwr :: Consonants indices summation is : 6
'''


# ● Define a function which takes the following lists as arguments
# Movies = [“spiderman”, “batman”, “hulk”, “lion king”, “captain america”]
# Parts = [3, 1, 0, 3, 3]
# And returns a dict with movie names as keys and number of parts as values

'''
def merge(movies, parts):
    print(dict(zip(movies, parts)))


merge(["spiderman", "batman", "hulk", "lion king", "captain america"], [3, 1, 0, 3, 3])
'''

'''
o/p:
{'spiderman': 3, 'batman': 1, 'hulk': 0, 'lion king': 3, 'captain america': 3}
'''


# ● Define a which takes variable number of positional arguments and returns the MEAN value
# of the arguments given

'''
def avg(*args):
    n = len(args)
    print(sum(args)/n)


avg(2, 2, 2, 2, 4)
'''

'''
o/p: 2.4
'''
# ● Define a function which takes multiple keyword arguments and return all the keywords
# Which has numbers as values

'''
def key_args(**kwargs):
    for values in kwargs.values():
        if type(values) == int or type(values) == float:
            print(values)


key_args(a=1, b=2.202, c="hi", d=100, e=[1, 2, 3])
'''

'''
o/p:
1
2.202
100
'''

# ● Define a function which takes multiple keyword arguments and return all the keywords
# Which has numbers as values

'''
def key_args(**kwargs):
    for key in kwargs.keys():
        if isinstance(kwargs[key], (int, float, complex)):
            print(key, end=" ")


key_args(a=1, b=2.202, c="hi", d=100, e=[1, 2, 3], A=1000, B=2000, C="HELLO BRO")
'''

'''
o/p : a b d A B
'''


# ● Define a function which can take multiple numbers as positional arguments and returns
# the MEDIAN of the numbers

'''
def avg(*args):
    l = list(args)
    l.sort()
    print(l)
    if len(l) % 2 == 0:
        a = len(l) // 2
        b = (l[a] + l[a-1]) / 2
        print("Median :", b)
    else:
        n = len(l) // 2
        print("Median :", l[n])


avg(4, 2, 5, 1, 3)
avg(3, 2, 1, 4, 6, 5)
avg(2, 5, 1, 8, 3, 4, 6, 7)
'''

'''
l = [2, 5, 1, 8, 3, 4, 6, 7]
l.sort()
print(l)'''


'''
o/p: 3
'''


# ● Define a function which returns if a number is ARMSTRONG number or not
# 153 = 1^3 + 5^3 + 3^3 = 153
'''
def armstrong(num):
    s = str(num)
    sum1 = 0
    length = len(s)
    for i in s:
        n = int(i)**length
        sum1 += n
    if num == sum1:
        print(f"The given number {num} is Armstrong number.")
    else:
        print(f"The given number {num} is Not Armstrong number.")


armstrong(153)
armstrong(15)
armstrong(1634)
armstrong(54748)
armstrong(5478)
'''


# ● Define a function which returns the reverse of a string if given or returns “give a string
# dude!” if any other data type is passed

'''
def reverse(string):
    if type(string) == str:
        print(string[::-1])
    else:
        print("Give a string Dude!!!!")


reverse("hello")
reverse("Boss")
reverse(1)
reverse([1, "hi", 2, 3])
'''

'''
o/p:
olleh
ssoB
Give a string Dude!!!!
Give a string Dude!!!!
'''

# ● Define a function which can take multiple keyword arguments and combine all the
# keywords in the form of a string and returns it

'''
def display(**kwargs):
    str1 = ""
    for values in kwargs.values():
        str1 += values
    print(str1)


display(a="Hey", b="Hi", c="Bro")
'''

'''
o/p:
HeyHiBro
'''

# ● Define a function to calculate and return the number of times its being called
'''
count = 0


def myfun():
    global count
    count += 1


myfun()
myfun()
myfun()

print(f"Function called {count} times!!!")
'''

# ---------------------- RECURSION ---------------------------

# ● Define a function which prints all the ODD numbers using RECURSION

'''
def odd_fun(num=1):
    if num <= 50:
        if not num % 2 == 0:
            print(num)
        odd_fun(num + 1)


odd_fun()
'''


# ● Define a function to traverse through a string using recursion

'''
def traverse(string="HELLO", i=0):
    if i < len(string):
        print(string[i], end="")
        traverse(string, i+1)


traverse()
'''
# ● Define a function which can print all the EVEN indexed values from a list
# [1, 2, 3, 4, 5, 6] using recursion

'''
def even_index(l, i=0):
    if i < len(l):
        if i % 2 == 0:
            print(l[i], end=" ")

        even_index(l, i+1)


even_index(l=[1, 2, 3, 4, 5, 6])
'''

# -------------------------------- END OF ASSIGNMENT ------------------------------------

# Prime Number

'''
num = int(input("Enter any number : "))
for n in range(2, num):
    if num % n == 0:
        print("Not Prime")
        break
else:
    print("Prime Number")
'''

# prime numbers in range

'''
start = int(input("Enter the First number : "))
end = int(input("Enter the End number : "))
if start == 1:
    start += 1

for num in range(start, end+1):
    for n in range(2, num):
        if num % n == 0:
            break
    else:
        print(num, end=" ")
'''

# n number of prime numbers
'''
start = int(input("Enter the First number : "))
end = int(input("Enter the End number : "))
stop = int(input("Enter how much first prime numbers to be print : "))
count = 0
if start == 1:
    start += 1

for num in range(start, end+1):
    for n in range(2, num):
        if num % n == 0:
            break
    else:
        count += 1
        if count <= stop:
            print(num, end=" ")
'''

# ----------------------------- RECURSION PRACTICE PROGRAMS -------------------------------

# 1. Write a Python program of recursion list sum.
#    Test Data: [1, 2, [3,4], 5]
#    Expected Result: 15

# sum = 0
'''def list_sum(l, i=0, sum = 0):
    # global sum
    if i < len(l):
        if type(l[i]) == int:
            # print(l[i])
            sum += l[i]
            list_sum(l, i+1, sum)
        elif type(l[i] == list):
            for j in l[i]:
                # print(j)
                sum += j
            list_sum(l, i+1, sum)
    else:
        print(f"Sum of list is {sum}")


list_sum(l=[1, 2, [3, 4], 5])
list_sum(l=[1, 2, [3, 4], 5, [5, 5, 10]])
'''


# 1. Write a Python program of recursion list sum.
#    Test Data: [1, 2, [3,4], [5,6]]
#    Expected Result: 21
'''
sum = 0


def list_sum(l, i=0):
    if i < len(l):
        global sum
        sum = sum + l[i]
        list_sum(l, i+1)
    else:
        print(f"Sum of list is {sum}")


list_sum(l=[1, 2, 3, 4, 5])

'''
# Write a Python program to get the sum of a non-negative integer.
# Test Data:
# sumDigits(345) -> 12
# sumDigits(45) -> 9

'''
def sum_digits(num=123, sum = 0, i=0):

    s = str(num)
    if i < len(s):
        sum += int(s[i])
        sum_digits(num, sum, i+1)
    else:
        print(f"Sum of digits is {sum}")


sum_digits()
'''


# -------------------- COMPREHENSION --------------------------

# ------------------ LIST COMPREHENSION -----------------------

# WAPT print nos from 1 to 5 in a list
'''
l = [ n for n in range(1, 6)]
print(l)
'''

# WAPT print nos from -10 to -1 in a list
'''
l = [ n for n in range(-1, -11, -1)]
print(l)
'''

# ------------------- INLINE IF ---------------------------

# Example
'''
num = 5
if num < 10: print(num); num += 5; print(num); num += 5; print(num)
'''

# WAPT add the even nos from 1 to 10 into a list
'''
l = [ n for n in range(1, 11) if n % 2 == 0 ]
print(l)
'''

# Add all the odd numbers from 150 to 180 into a list
'''
l = [ n for n in range(150, 181) if n % 2 != 0 ]
print(l)
'''

# ------------------ INLINE IF-ELSE ------------------

# Check given number is even r odd
'''
num = 10
print("even") if num % 2 == 0 else print("odd")
'''

# o/p : [1001, 2, 1003, 4, 1005, 6, 1007, 8, 1009, 10]
'''
l = [ num if num % 2 == 0 else num + 1000 for num in range(1, 11)]
print(l)
'''

# ArithmaticProgression
'''
def arithmatic_progression(array):
    for i in array:
        for j in array:
            if j-i == (j+1)-(i+1):
                print("AP")
            else:
                print("NAP")


arithmatic_progression([2, 4, 6, 8, 10])
arithmatic_progression([1, 3, 5, 7, 9, 12, 13])
'''














