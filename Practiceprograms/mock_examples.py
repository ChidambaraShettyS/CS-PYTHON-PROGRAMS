# 1. Write program to convert the alphabets in the string "I'm BATMAN" from uppercase to lowercase and vice-versa
# without using inbuilt methods
'''
s = "I'm BATMAN"
s1 = ""
for i in s:
    if "A" <= i <= "Z":
        s1 += chr(ord(i) + 32)
    elif "a" <= i <= "z":
        s1 += chr(ord(i) - 32)
    else:
        s1 += i
print(s1)
'''

# 2. Create a function to check a given strings palindrome or not without using slicing
'''
s = input("Enter the string : ")
s1 = ""

for i in s:
    s1 = i + s1

if s == s1:
    print("Palindrome")
else:
    print("Not Palindrome")
'''

# 3. Write a program to find the longest word in the sentence
#    "You either die a hero or live long enough to become the villain"

'''
s = "You either die a hero or live long enough to become the villain"
s1 = s.split()
l = []
for i in s1:
    l.append(len(i))

g = l[0]
for j in l:
    if j > g:
        g = j

n = l.index(g)
print(s1[n])
'''

'''
s = "You either die a hero or live long enough to become the villain"
s1 = s.split()
d = {}
l = []
for i in s1:
    d[i] = len(i)

for j in d.values():
    l.append(j)
    
g = l[0]
for item in l:
    if item > g:
        g = item

print(g)
'''


# 4. Write a program to print the following patter


# 5. Create a class called TestYantra and create a class variables called
#    CEO and assign the value Mr.Girish
#    Create methods called testing, product development
#    Create classes called Qspiders, Jspiders, Pyspiders and inherit
#    all the properties to them from TestYantra

'''
class TestYantra:
    CEO = "Mr.Girish"

    # print(CEO)

    @staticmethod
    def testing():
        print("Testing Method from TestYantra class")
        print(f"TestYantra class CEO : {CEO}")

    @staticmethod
    def product_development():
        print("Product Development Method from TestYantra class")


class Qspiders(TestYantra):
    pass


class Jspiders(TestYantra):
    pass


class Pyspiders(TestYantra):
    pass


obj = Qspiders
# obj.ceo()
obj.testing()
obj.product_development()


obj1 = TestYantra()
print(obj1.CEO)
'''
# 6. Wap to count the number of occurrences of character in the string 'I am vengeance'
'''
s = 'I am vengeance'
d = {}
for i in s:
    c = 0
    for j in s:
        if i == j:
            c += 1
        d[i] = c
print(d)
'''
# OR
'''
s = 'I am vengeance'
d = {}
for i in s:
    d[i] = s.count(i)

print(d)
'''
# 1. wap to get the following output.
# i. a = 'python programming languagee
#    out = {1:'nohtyp', 3:'gnimmargorp', 4:'eegangnal"}

'''
a = 'python programming language'
d = {}

for i in a.split():
    c = 0
    for j in i:
        if j in "aeiouAEIOU":
            c += 1
    d[c] = i[::-1]

print(d)
'''

# ii. p = 'bruhat bengaluru maha nagara palike'
#    out={"BRUHAT":0,"Bengaluru':1, MAHA':2, 'Nagara':3, 'PALIKE":4}
'''
p = 'bruhat bengaluru maha nagara palike'
c = 0
d = {}
for i in p.split():
    if c % 2 == 0:
        d[i.upper()] = c
    else:
        d[i.capitalize()] = c       #d[i.replace(i[0], i[0].upper())] = c
    c += 1
print(d)
'''
# 2. define a function to count the number of uncommon elements present in the given two collection
#       list1 = [11,2,3,5,4,5,67,8]
#       list2-[1,2,1,1,2,3,4,9,10,11,12,1,2,13]
#       output=12

'''
def func(l1, l2):
    out = 0
    for i in l2:
        if i not in l1:
            out += 1
    for j in l1:
        if j not in l2:
            out += 1
    return out


list1 = [11, 2, 3, 5, 4, 5, 67, 8]
list2 = [1, 2, 1, 1, 2, 3, 4, 9, 10, 11, 12, 1, 2, 13]
print(func(list1, list2))
'''

# 3. define a function to check whether the given number is STRONG number or not.
#       ex: 145---1!+4!+5!-145

'''
def strong_num(num):
    s = str(num)
    sum = 0
    for i in s:
        f = 1
        for n in range(1, int(i)+1):
            f *= n
        sum += f

    if num == sum:
        print(f"{num} is Strong Number")
    else:
        print(f"{num} is Not a Strong Number")


strong_num(1)
strong_num(2)
strong_num(145)
strong_num(146)
strong_num(40585)
strong_num(40)
strong_num(100)
'''

# 4. create a class named Resume using inheritance and class should contain atleast 3 obj and 2 class methods in each.
'''
class Resume:

    def __init__(self, name, mail_id):
        self.name = name
        self.mail_id = mail_id

    def display_name(self):
        print(f"Name of candidate is {self.name}")

    def display_mail(self):
        print(f"Mail Id of candidate is {self.mail_id}")

class Candidates(Resume):
    pass


anu = Candidates("Anu", "Anu@gmail.com")
lav = Candidates("Lav", "Lav@gmail.com")
kar = Candidates("Kar", "Kar@gmail.com")
anu.display_name()
anu.display_mail()
lav.display_name()
lav.display_mail()
kar.display_name()
kar.display_mail()
'''



# 5. Create a class similar like an inbuilt class to perform arithematic operations using magic methods.

'''
class Arithematic_Operations:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        print(f"Addition : {self.a + self.b}")

    def sub(self):
        print(f"Subtraction : {self.a - self.b}")

    def mul(self):
        print(f"Multiplication : {self.a * self.b}")

    def div(self):
        print(f"Division : {self.a / self.b}")

    def floor_div(self):
        print(f"Floor Division : {self.a // self.b}")

    def power(self):
        print(f"Power : {self.a ** self.b}")



obj = Arithematic_Operations(5, 2)
obj.add()
obj.sub()
obj.mul()
obj.div()
obj.floor_div()
obj.power()
'''


'''
class UserMainCode(object):
    @classmethod
    def totalTurns(cls, input1,input2, input3):
        input1 : "string"
        input2 :int
        input3 : int

        cls.input1 = input1
        cls.input2 = input2
        cls.input3 = input3

        sum = input3
        s = ""
        c = 0
        for i in range(len(cls.input1)):
            if i != cls.input1[-1]:
                s += cls.input1[i]
                c +=1
            else:
                 s += cls.input1[-1]
                 c +=1

        print(s)
        print(c)


o = UserMainCode
o.totalTurns("abcabc", 1, 2)
'''

















