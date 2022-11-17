# ---------- WHILE LOOP --------------

# WAP to print Hello world 5 times using while loop

'''
count = 1

while count <= 5:
    print("Hello world")
    count = count + 1
'''

# WAPT print even numbers from 50 to 75

'''
a = 50

while a <= 75:
    print(a)
    a += 2'''

#   OR
'''
a = 50

while a <= 75:
    if a % 2 == 0:
        print(a)
    a += 1'''

# WAPT print all the multiples of 5 and 7 from 1 to 250

'''
a = 1

while a <= 250:
    if a % 5 == 0 and a % 7 == 0:
        print(a)
    a += 1
'''

# WAPT traverse the string and traversing in reverse
'''
s = "Hello World"
index = 0

while index < len(s):
    print(s[index], end='')
    index += 1
'''

# And
'''
s = "Hello World"
index = len(s) - 1   # -1

while index >= 0:         # instead of 0 -len(s)
    print(s[index], end='')
    index -= 1'''

# Extracting Alphabets, Numbers and Special characters from the string seperate
'''
s = "Hello@World$1234#5678!"
index = 0

alpha = ""
num = ""
special =""

while index < len(s):
    char = s[index]
    if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
        alpha += char
    elif '0' <= char <= '9':
        num += char
    else:
        special += char
    index += 1
print(s)
print(alpha)
print(num)
print(special)
'''

# Printing Index and Character of string one by one
'''
s = "Hello"

index = 0

while index < len(s):
    print(s[index], index)
    index += 1
    '''

# Program to count the number of capital and small letters in the string "HelLo WORld"
'''
s = "HelLo WORld"

index = 0
s_count = 0
c_count = 0
while index < len(s):
    char = s[index]
    if 'a' <= char <= 'z':
        s_count += 1
    elif 'A' <= char <= 'Z':
        c_count += 1

    index += 1
print("Small letter count in string :", s_count)
print("Capital letter count in string :", c_count)
'''

# Count the number of Special Characters in the string "john@123gmail.com"
'''
s = "John@123gmail.com"

index = 0
s_count = 0
c_count = 0
spe_count = 0
num_count = 0

while index < len(s):
    char = s[index]
    if 'a' <= char <= 'z':
        s_count += 1
    elif 'A' <= char <= 'Z':
        c_count += 1
    elif '0' <= char <= '9':
        num_count += 1
    else:
        spe_count += 1

    index += 1

print("Small letter count in string :", s_count)
print("Capital letter count in string :", c_count)
print("Numbers count in string :", num_count)
print("Special character count in string :", spe_count)
'''

# Write a number to reverse a number

'''
num = int(input("Enter the number to reverse : "))
s_num = str(num)
rev_str = s_num[::-1]
rev_num = int(rev_str)
print("Reversed number is : ", rev_num)
'''

# OR
'''
num = int(input("Enter the number to reverse : "))
s_num = str(num)

index = len(s_num) - 1
print("Reversed number is : ", end='')

while index >= 0:
    print(s_num[index], end='')
    index -= 1

'''

# WAPT find if a number is palindrome or not
'''
num = int(input("Enter the number to reverse : "))
s_num = str(num)
rev_str = s_num[::-1]
rev_num = int(rev_str)

if num == rev_num:
    print("The given number is Palindrome!!")
else:
    print("The given number is NOT Palindrome!!")
'''

# Accept two numbers from the user and display sum of even numbers between them (including both)
'''
num1 = int(input("Enter the First range : "))
num2 = int(input("Enter the Second range : "))
sum = 0

while num1 <= num2:
    if num1 % 2 == 0:
        sum += num1
    num1 += 1

print("Sum of even numbers is : ", sum)
'''

# Print alternative numbers and print items with corresponding index from the list
'''
l = [1997, 1998, 1999, 2000, 2001, 2002, 2003]

print("Printing Alternative items from the list :", l[::2])

index = 0
print("Printing item and its index : ")

while index < len(l):
    print(l[index], ",", index)
    index += 1
'''

# ------------- LOOP CONTROL STATEMENTS -----------------

# --- BREAK --- CONTINUE --- PASS --- ELSE

# ---- BREAK -----
'''
while True:
    print('Line 1 !!!')
    print('Line 2 !!!')
    break
    print('Line 3 !!!')
    print('Line 4 !!!')
'''
'''
count = 0

while count < 10:
    print(count)
    if count == 5:
        break
    count += 1
else:
    print("Executed without Break")
'''

# ---- CONTINUE ------
'''
count = 0

while count <= 10:
    if count == 5:
        count += 1
        continue
    print(count)
    count += 1
'''
# ------------- FOR LOOP --------------------

# ---------- range() -----------
'''
var = range(10)
var_2 = range(0, 10, 2)
var_1 = range(0, -10, -1)
print(tuple(var))
print(tuple(var_1))
print(tuple(var_2))
'''

# index with Value
'''
l = [1, 2, 3, 4, 5, 6]
for i, val in enumerate(l):
    print(i, " ", val)
'''
# Generate nos from 1 to 10
'''
for num in range(1, 11):
    print(num)
'''

# Generate nos from -10 to -20
'''
for num in range(-10, -21, -1):
    print(num)
'''

# Print even nos from 1 to 20
'''
for num in range(2, 21, 2):
    print(num)
'''

# Printing nos ending with 3 from 1 to 100
'''
for num in range(3, 101, 10):
    print(num)
'''
# OR
'''
for num in range(1, 101):
    n = str(num)
    if n[-1] == '3':
        print(num)
'''

# Printing nos having 6 in them from 1 to 100
'''
for num in range(1, 101):
    n = str(num)
    if '6' in n:
        print(num)
'''


# Create an infinite for loop
'''
l = ['hi']

for ele in l:
    l.append(1)
'''















