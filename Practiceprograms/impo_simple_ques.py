# -------------------------- If statement ------------------------------------------

# Write a program to check if the number entered by the user is 0
# Write a program to check if a number entered by the user is positive
# Write a program to check if a number entered by the user is negative
# Write a program to check if an iterable is empty


# ------------------------------------- If else statement ----------------------------------------------------

# Write a program to check if a number is even or odd
# Write a program to check if a number is multiple of 5 and 7 or not
# Write a program to check if the character entered by the user is in uppercase
# Write a program to check if the character entered by the user is in lowercase
# Write a program to check if the character entered by the user is a vowel or not
# Write a program to check if entered character is a number or not
# Write a program to check if the entered char is a in
# Check whether a character’s ASCII value of a character is even or odd

# wap to take key from the user an check if the key is present in the
# dict, if present then increment or else initialize the value to 1
# marks = { “social” : 89, “math” : 34, “chemistry” : 90, “physics” : 99 }
'''
marks = {"social": 89, "math": 34, "chemistry": 90, 'physics': 99}

ip = input("Enter the subject : ")
if ip in marks:
    marks[ip] += 1
else:
    marks[ip] = 1

print(marks)
'''

# check if the given string is ending with vowel or not

# wap to convert positive number to negative and vise versa


# ----------------------------------- elif statement ----------------------------------------

# Write a program find the greatest of 3 numbers
# Write a program to find if the entered character is in
# uppercase or lowercase or isn't both
# Write a program to find if the entered number is vowel or
# consonant or isn't both
# Write a program to find if a entered character is a alphabet or
# a number or a special character
# The given number is one digit or two digit or three digits or more
# than three digits.


# -------------------------------- While loop ---------------------------------------------

# - write a program to print numbers from 1 - 10
# - write a program to print numbers from 10 - 1
# - Write a program to print even numbers from 1 - 10
# - Write a program to print even numbers from 20 - 1
# - Write a program to print odd numbers from 1 - 10
# - Write a program to print odd numbers from 10 - 1
# - Write a program to print numbers which are divisible by 5 and 7 in the range of 1 - 200
# - Write a program to print numbers are ending with 6 in the range of 1 - 150
# - Write a program to print numbers which have 8 in them in the range of 1 - 200
# - Write a program to add numbers from 1 - 10 to a list
# - Write a program to add numbers from 1 - 10 to a set
# - Write a program to print ‘hello world’ 10 times
# - Write a program to iterate through a string ‘hello world’
# - Write a program to print all the even indexed values in the string
# - Write a program to iterate through a list
#   l = [1, 2, 3, 40, 50, 60, 70, 34, 33, 69]
# - Write a program to print all the even indexed values in a list
'''
l = [1, 2, 3, 40, 50, 60, 70, 34, 33, 69]
i = 0
while i < len(l):
    if i % 2 == 0:
        print(l[i])
    i += 1
'''

# - Write a program to print all the even numbers from the list
# - Wap to print all the list items with odd indexed values in reverse
'''
l = [1, 2, 3, 40, 50, 60, 70, 34, 33, 69]
i = 0
while i < len(l):
    if i % 2 != 0:
        print(str(l[i])[::-1])
    i += 1
'''
# - Write a program to print to extract all the odd indexed characters and store them inside a list
#   from the following string “Hulk smash”
'''
s = "Hulk Smash"
l = []
i = 0
while i < len(s):
    if i % 2 != 0:
        l.append(s[i])
    i += 1
print(l)
'''

# - write a program to extract all the vowels from the above string and add it to a list
# - Write a program to extract all the characters from the given string and add character and
#   its index pair to a dictionary
# - Write a program to add all the words and their length pair into a dictionary from the following string
#   “Programming is fun with python”
'''
s = "Programming is fun with python"
d = {}
l = s.split()
i = 0
while i < len(l):
    d[l[i]] = len(l[i])
    i += 1

print(d)
'''

#   S = “jacob.smith12345@gmail.com”
# ● WAP to count the number of alphabets in the above string using while loop
# ● WAP to count the number of digits in the above string
# ● WAP to count the number special characters in the string
# ● Wap to count and print all number of special characters, alphabets,digits from the above string
# ● Wap to extract from all the digits in a string and print the sum of digits

# ● Create a dictionary for the below list
#   cities = [('India', 'Bangalore'), ('Italy',’Rome '), ('Russia', 'Moskov'),
#             (‘Germany', 'Berlin'), ('France', ‘Paris'), ('USA', 'New York'),
#             ('Australia', 'Sydney'), ('Egypt', ‘cairo'), ('China', 'Shanghai')]
'''
cities = [('India', 'Bangalore'), ('Italy', 'Rome'), ('Russia', 'Moskov'),
          ('Germany', 'Berlin'), ('France', 'Paris'), ('USA', 'New York'),
          ('Australia', 'Sydney'), ('Egypt', 'cairo'), ('China', 'Shanghai')]
'''
'''
d = dict(cities)
print(d)'''


# ● Print all countries which as the city names ending with consonants


# ● Print all the asian countries along with their cities in from the above dictionary
'''
d = dict(cities)
i = 0
k = list(d.keys())
v = list(d.values())
a = ["India", "China", "Afghanistan", "Bangladesh", "Indonesia", "Pakistan" "Sri Lanka"]
while i < len(k):
    if k[i] in a:
        print(k[i], v[i])
    i += 1
'''

# --------------------------------------- For loop ---------------------------------------------


# - write a program to print numbers from 1 - 10
'''
for i in range(1, 11):
    print(i)
'''
# - write a program to print numbers from 10 - 1
'''
for i in range(10, 0, -1):
    print(i)
'''
# - Write a program to print even numbers from 1 - 10
'''
for i in range(1, 11):
    if i % 2 == 0:
        print(i)
'''
# - Write a program to print even numbers from 20 - 1
'''
for i in range(20, 0, -1):
    if i % 2 == 0:
        print(i)
'''
# - Write a program to print odd numbers from 1 - 10
'''
for i in range(1, 11):
    if i % 2 != 0:
        print(i)
'''
# - Write a program to print odd numbers from 10 - 1
'''
for i in range(10, 0, -1):
    if i % 2 != 0:
        print(i)
'''
# - Write a program to print numbers which are divisible by 5 and 7 in the range of 1 - 200
'''
for i in range(1, 201):
    if i % 5 == 0 and i % 7 == 0:
        print(i)
'''

# - Write a program to print numbers are ending with 6 in the range of 1 - 150
'''
for i in range(1, 151):
    if str(i)[-1] == '6':
        print(i)
'''
# - Write a program to print numbers which have 8 in them in the range of 1 - 200
'''
for i in range(1, 201):
    if '8' in str(i):
        print(i)
'''
# - Write a program to add numbers from 1 - 10 to a list
# - Write a program to add numbers from 1 - 10 to a set
# - Write a program to print ‘hello world’ 10 times
# - Write a program to iterate through a string ‘hello world’
# - Write a program to print all the even indexed values in the string
# - Write a program to iterate through a list
#   l = [1, 2, 3, 40, 50, 60, 70, 34, 33, 69]
# - Write a program to print all the even indexed values in a list
# - Write a program to print all the even numbers from the list
# - Wap to print all the list items with odd indexed values in reverse
# - Write a program to print to extract all the odd indexed characters
# and store them inside a list from the following string - “Hulk smash”
# - write a program to extract all the vowels from the above string and add it to a list
# - Write a program to extract all the characters from the given string and add character
#   and its index pair to a dictionary
# - Write a program to add all the words and their length pair into a dictionary from the following string
#   “Programming is fun with python”
#   S = “jacob.smith12345@gmail.com”
# ● WAP to count the number of alphabets in the above string using while loop
# ● WAP to count the number of digits in the above string
# ● WAP to count the number special characters in the string
# ● Wap to count and print all number of special characters, alphabets,digits from the above string
# ● Wap to extract from all the digits in a string and print the sum of digits
#   Marks = {“math”: 34, “phy”: 89, “comp”: 88, “chem” : 99}
# ● Wap to iterate through a dictionary
# ● Wap to print all the keys and values in a dictionary
'''
Marks = {"math": 34, "phy": 89, "comp": 88, "chem": 99}
# print(Marks.items())
for i, j in Marks.items():
    print(i, j)
'''
# ● Wap to print all the keys if the values are of numeric type
'''
Marks = {"math": 34, "phy": 89, "comp": 88, "chem": 99}

for i, j in Marks.items():
    if isinstance(j, (int, float)):
        print(j)
'''

# ● Wap to extract all the even values from the set and add them in to a new set
#   S = {10, 11, 12, 13, 14, 15, 16, 17}
'''
S = {10, 11, 12, 13, 14, 15, 16, 17}
s = set()
for i in S:
    if i % 2 == 0:
        s.add(i)
print(s)
'''

# ● Wap to index the above set and print all the even indexed values in the above set
'''
S = {10, 11, 12, 13, 14, 15, 16, 17}
l = []
for i in S:
    l.append(i)
for j in range(len(l)):
    if j % 2 == 0:
        print(l[j])
'''


# ● Create a dictionary for the below list
#   cities = [('India', 'Bangalore'), ('Italy',’Rome '), ('Russia', 'Moskov'),
#             (‘Germany', 'Berlin'), ('France', ‘Paris'), ('USA', 'New York'),
#             ('Australia', 'Sydney'), ('Egypt', ‘cairo'), ('China', 'Shanghai')]

cities = [('India', 'Bangalore'), ('Italy','Rome'), ('Russia', 'Moskov'),
          ('Germany', 'Berlin'), ('France', 'Paris'), ('USA', 'New York'),
          ('Australia', 'Sydney'), ('Egypt', 'cairo'), ('China', 'Shanghai')]
'''
d = dict(cities)
print(d)'''


# ● Print all countries which as the city names ending with consonants
'''
d = dict(cities)
for i, j in d.items():
    if j[-1] in "aeiouAEIOU":
        print(i)
'''

# ● Print all the asian countries along with their cities in from the above dictionary
'''
d = dict(cities)
a = ["India", "China"]
for i, j in d.items():
    if i in a:
        print(i, j)
'''
# ● fuels = “petrol diesel methanol ethanol gas kerosene hydrogen”
#   Prices = “120.23,100.34,150,160,190,60,200”
#   Store both fuels and prices in lists and iterate through them at a time

# fuels = "petrol diesel methanol ethanol gas kerosene hydrogen"
# prices = "120.23,100.34,150,160,190,60,200"
'''
fl = []
pl = []
for i in fuels.split():
    fl.append(i)
    print(i)

for j in prices.split(sep=","):
    pl.append(j)
    print(j)
'''
# ● Print all the fuel names along with prices which are priced above 100 LOL :)

'''
d = dict(zip(fuels.split(), prices.split(sep=",")))
for i, j in d.items():
    if float(j) > 100:
        print(i, ":", j)
'''

'''
fuels = "petrol diesel methanol ethanol gas kerosene hydrogen"
prices = "120.23,100.34,150,160,190,60,200"
f = fuels.split()
p = prices.split(sep=",")
obj = dict(zip(f, p))


for key in obj:
    if float(obj[key]) > 100:
        print(key)
'''

# ● Find the sum of all the numbers from n1 to n2 ( n1 and n2 are inputs)
# ● Find the factorial of a given number
'''
n = int(input("Enter the number : "))
f = 1
for i in range(1, n+1):
    f *= i
print(f)
'''

# Fibonancci
'''
n = 0
n1 = 1
# i = 1
c = int(input("Enter the no of febo series : "))
print(n, n1, end=" " )
# while i <= c - 2:             # Using While Loop
#     n2 = n + n1
#     print(n2, end=" ")
#     n, n1 = n1, n2
#     i += 1
for i in range(1, c-1):         # Using For Loop
    n2 = n + n1
    print(n2, end=" ")
    n, n1 = n1, n2
'''

























































































































































































































