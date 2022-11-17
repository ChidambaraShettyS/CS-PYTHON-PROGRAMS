# ------------------------------- GENERATORS --------------------------------------

# 1. Generate all the numbers in the range of 1 - 10

'''
def numbers():
    for n in range(1,11):
        yield n


obj = numbers()
print(next(obj))
print(next(obj))
print(next(obj))
for i in obj:
    print(i)
'''

# 2. Generate the following  sequence " 1 12 123 1234 12345 123456"

'''
def pattern():
    for num in range(1, 7):
        s = ''
        for n in range(1, num+1):
            s += str(n)
        yield s


obj = pattern()
for i in obj:
    print(i, end=' ')
'''

# 3. Generate the following sequence " a ab abc abcd abcde abcdef"
'''
def pattern():
    for num in range(97, 103):
        s = ''
        for n in range(97, num+1):
            s += chr(n)
        yield s


obj = pattern()
for i in obj:
    print(i, end=' ')
'''

# 4. Generate all the numbers which are ending with 3 in the range of 1 - 100
# ex : 3, 13, 23, 33, 43, 53, 63,..........,93

'''
def numbers():
    for num in range(1, 101):
        s = str(num)
        if s[-1] == '3':
            yield num


obj = numbers()
for i in obj:
    print(i, end=" ")
'''
'''
o/p:
3 13 23 33 43 53 63 73 83 93 
'''

# 5. Generate all the numbers which have 7 in them in the range 1 - 100
# ex : 7, 17, 27, 37, 47, 57, ..........97

'''
def numbers():
    for num in range(1, 101):
        s = str(num)
        if '7' in s:
            yield num


obj = numbers()
for i in obj:
    print(i, end=" ")
'''
'''
o/p:
7 17 27 37 47 57 67 70 71 72 73 74 75 76 77 78 79 87 97 
'''

# 6. Generate all the armstrong numbers in the range 0f 1 - 1000

'''
def armstrong():
    for n in range(1, 1001):
        s = str(n)
        sum = 0
        for n1 in s:
            sum += int(n1) ** len(s)
        if sum == n:
            yield n

obj = armstrong()
for i in obj:
    print(i, end=" ")
'''
'''
o/p:
1 2 3 4 5 6 7 8 9 153 370 371 407  
'''

# 7. Generate all the strong numbers in the range of 1 - 1000

'''
def strongnum():
    for n in range(1, 1001):
        s = str(n)
        sum = 0
        i = 1
        fact = 1
        for n1 in s:
            while i <= int(n1):
                fact = fact * i
                i += 1

            sum += fact
        if sum == n:
            yield n


obj = strongnum()
for item in obj:
    print(item)
'''
'''
o/p:
1
2
145
'''
'''
# Factorial 

num = 4
i = 1
f = 1
while i <= num:
    f = f * i
    i += 1

print(f)

'''



























