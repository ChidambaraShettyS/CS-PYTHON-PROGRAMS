
# WAP to get the following o/ps using fun

# 1
'''
i/p : [2, 4, 'hello', 4+3j, 1, 3]
o/p : [12, 6, 24, 24, 24, 8]
'''

'''
l = [2, 4, 'hello', 4+3j, 1, 3]
l1 = []

for ele in l:
    mul = 1
    for ele1 in l:
        if type(ele1) == int and ele != ele1:
                mul *= ele1
    l1.append(mul)
print(l1)
'''

# 2
'''
i/p : ('python', 'programming', 'language', 'is', 'easy', 'python', 'easy')
o/p : {'python' : [1,1], 'programming' : [2,3], 'language' : [3,3], 'is' : [4,1], 'easy' : [5,2]}
'''

'''
t = ('python', 'programming', 'language', 'is', 'easy', 'python', 'easy')
d = {}

for ele in t:
    count = 0
    for i in ele:
        if i in "aeiou":
            count += 1
        d[ele] = [(t.index(ele)+1), count]

print(d)
'''

# OR

'''
t = ('python', 'programming', 'language', 'is', 'easy', 'python', 'easy')
d = {}
pos = 1
for ele in t:
    if ele not in d:
        count = 0
        for char in ele:
            if char in "aeiouAEIOU":
                count += 1
        d[ele] = [pos, count]
    pos += 1
print(d)
'''

# ----------------------------- IF --------------------------------

# The given i/p is +ve r -ve
'''
num = int(input("Enter the number:"))
if num >= 0:
    print("Number is Positive!!!!")
else:
    print("Number is Negative!!!!")
'''


# Consider 2 i/ps i.e a n b which accepts string as the i/p. Reverse i/p 2 and compare i/p 1 and i/p 2
# if i/p 1 matches with i/p 2 print Python students are the best if condition dosen't match
# print Python student are worst

'''
a = input("Enter 1st i/p : ")
b = input("Enter 2nd i/p : ")

if a == b[::-1]:
    print("Python Students are BEST!!!")
else:
    print("Python Students are SUPER!!!")
'''


# A parameter side is true if the monkey is sitting on the floor.
# Parameter side is flase if the monkey is sitting on a tree
# If the monkey is sitting on a floor it has 1 tail if the same monkey is sitting on a tree it has 2 tails.
# check wathere the monkey is having 1 r 2 tails

'''
ip1 = input("Enter floor or tree :")

if ip1 == "floor":
    side = True
else:
    side = False

if side == True:
    print("Monkey has 1 Tail")
else:
    print("Monkey has 2 Tail")
'''

# A parameter smile is true if the girl is smiling
# A parameter smile is false if the girl is crying
# A boy wants to prapose the girl on valaintise day if she smiles then it means the praposal is accepted
# if she cries then the praposal is rejected print happy if she accepts the praposal
# print sad if she rejects the praposal

'''
para = input("Girl is Smile r Cry : ")

if para == "Smile":
    girl = "Smiling"
else:
    girl = "Crying"

if girl == "Smiling":
    print("Happy")
else:
    print("Sad")
'''

'''
smile = bool(input("Enter True if girl is smiling : "))
if smile == True:
    print("Happy")
else:
    print("Sad")
'''


# WAP to check wethere the given char is eithere upper, lower, num without using inbuild fun
'''
char = input("Enter the Character : ")

if 'A' <= char <= 'Z':
    print("Upper")
elif 'a' <= char <= 'z':
    print("Lower")
elif -9 <= int(char) <= 9:    # Or '0' <= char <= '9': only for +ve num and else block won't work
    print("Number")
else:
    print("Special char")
'''

# WAP to check wethere the given integer num is divisible by 3 n 5 or not if it is div by 3 print cube of that num
# if it is div by 5 print num ^ 5, if the num is div by both 3 n 5 add 3 n 5 to that num n print o/p
'''
num = int(input("Enter the number : "))

if num % 3 == 0 and num % 5 == 0:
    print(num + 3 + 5)
elif num % 3 == 0:
    print(num ** 3)
elif num % 5 == 0:
    print(num ** 5)
else:
    print("Not divisible by both number!!!!")
'''

# Consider a restorant which sells 3 diff pizza ( cheese loaded, Veg loaded, Non veg loaded) at the price of
# 120, 180, 240 w.r.t. Customer can order one varity of pizza at a time n can order n no of piza in the same flavour.
# if any add ons is required customer can opt one rwq add on along with a order.
# Avialable add ons are (extra cheese, extra ketchap) at the price of 20 each.
# Based on the customer order calculate the total bill using nested if stmts
'''
pizza = input("Selct the Pizza : (cheese loaded, veg loaded, nonveg loaded): ")
count = int(input("Count of pizza : "))

if pizza == "cheese loaded":
    addon = input("Any Add ons = (extra cheese, extra ketchap) rs.20")
    if addon == "extra cheese" or addon == "extra ketchap":
        print("Bill is :", (120 * count) + 20)
    else:
        print("Bill is :", (120 * count))
elif pizza == "veg loaded":
    addon =input("Any Add ons = (extra cheese, extra ketchap) rs.20")
    if addon == "extra cheese" or addon == "extra ketchap":
        print("Bill is :", (180 * count) + 20)
    else:
        print("Bill is :", (180 * count))
elif pizza == "nonveg loaded":
    addon = input("Any Add ons = (extra cheese, extra ketchap) rs.20")
    if addon == "extra cheese" or addon == "extra ketchap":
        print("Bill is :", (240 * count) + 20)
    else:
        print("Bill is :", (240 * count))
else:
    print("Outof Stock!!!")
'''

# OR
'''
menu = {"cheese loaded": 120, "veg loaded": 180, "non veg loaded": 240}
addon = {"extra cheese": 20, "extra ketchen": 20}

a = input("Enter pizza name :")
b = int(input("Enter quantity :"))
c = input("Enter 1 if addon is neede else enter 0 :")

if a in menu:
    bill = menu[a]*b
    if c == '1':
        d = input("Enter Addon :")
        if d in addon:
            bill += addon[d]
            print(bill)
        else:
            print("Addon not available")
    else:
        print(bill)
else:
    print("Item not available")
'''

# Using Class
'''
class Pizza:
    menu = {"cheese loaded": 120, "veg loaded": 180, "non veg loaded": 240}
    addon = {"extra cheese": 20, "extra ketchen": 20}

    def __init__(self, p, q, a):
        self.p = p
        self.q = q
        self.a = a

    def bill(self):
        if self.p in self.menu:
            tbill = self.menu[p] * self.q
            if self.a == 1:
                ad = input("Enter the AddOn : ")
                if ad in self.addon:
                    tbill += self.addon[ad]
                    print(tbill)
                else:
                    print("Addon is not available")
                    print(tbill)
            else:
                print(tbill)
        else:
            print("Pizza Out of stock")


p = input("Enter the Pizza name :")
q = int(input("Enter the Pizza quantity :"))
a = int(input("Enter 1 if you need addon : "))
obj = Pizza(p, q, a)
obj.bill()
'''


# -------------------------------- WHILE LOOP ----------------------------------

# wap to get the following o/p
# 1 * 5 = 5
# 2 * 5 = 5
#
# 10 * 5 = 50
'''
i = 1
n = int(input("Enter the num to multiply : "))
while i <= 10:
    print(f"{i} * {n} = {i*n}")
    i += 1
'''


# wap to check wethere the given collection is homogenious r heterogenious


'''
n = ['python', 10, 20, 30, 'program']
m = [1, 2, 3, 4, 5]

flag = 0
i = 1
while i < len(m):
    if type(m[0]) != type(m[i]):
        flag = 1
    i += 1
if flag == 1:
    print("Heterogenious !!!")
else:
    print("Homogenious !!!")
'''


# wap to reverse the given num without typecasting r slicing n pri the divisors of rev num
'''
n = int(input("enter the num : "))
rev = 0
while n != 0:                        # n > 0
    rev = rev * 10 + n % 10
    n //= 10
    
print(rev)

i = 1
while i <= rev:
    if rev % i == 0:
        print(i)
    i += 1
'''

# wap to desing the login page which accepts username n password initially the entered by the user has to be
# stored in the form of a collection n later that data has to be used to validate the login if the credentials
# entered by the user is mathing with the data stored previously print the msg login successful else print the msg
# enter valid credentials n re enter the credentials (re enter the credentials shd be done until u get login get successful)

'''
d = {}
user_name = input("Enter the User Name to store : ")
password = input("Enter the Password for above user name to store : ")

d[user_name] = password

i = True

while i:
    print("Enter the credentials : ")
    user = input("Enter the user name : ")
    if user in d:
        p_word = input("Enter the password : ")
        if d[user_name] == p_word:
            print("Log in Successful !!!")
            i = False
        else:
            print("Enter Valid Credentials !!!")
    else:
        print("Enter Valid Credentials !!!")
'''


# wap to find the sum of ASCII values of all upper case char n lower case char separately
# in a given str.
# if the sum of ASCII values of all upper case char is greater than sum of ascii of lower case char then print
# all upper case char present at odd index in the same given str else print all lower case char present at even index
# str = "pYSpiDeRsBTm@123"

'''
s = "pYSpiDeRsBTm@123"

u_sum, l_sum, i = 0, 0, 0
while i < len(s):
    if 'A' <= s[i] <= 'Z':
        u_sum += ord(s[i])
    elif 'a' <= s[i] <= 'z':
        l_sum += ord(s[i])
    i += 1
print(f"UPPER SUM : {u_sum}, LOWER SUM : {l_sum}")
i = 0
if u_sum > l_sum:
    while i < len(s):
        if 'A' <= s[i] <= 'Z' and i % 2 != 0:
            print(f"Odd Index Of UPPER case : {s[i]}, {i}")
        i += 1
else:
    while i < len(s):
        if 'a' <= s[i] <= 'z' and i % 2 == 0:
            print(f"Even Index of LOWER case : {s[i]}, {i}")
        i += 1
'''

# Without i two times

'''
s = "pYSpiDeRsBTm@123"

u_sum, l_sum, i = 0, 0, 0
while i < len(s):
    if 'A' <= s[i] <= 'Z':
        u_sum += ord(s[i])
    elif 'a' <= s[i] <= 'z':
        l_sum += ord(s[i])
    i += 1

# i = 0
if u_sum > l_sum:
    while i >= 0:
        i -= 1
        if 'A' <= s[i] <= 'Z' and i % 2 != 0:
            print(f"Odd Index Of UPPER case : {s[i]}, {i}")

else:
    while i >= 0:
        i -= 1
        if 'a' <= s[i] <= 'z' and i % 2 == 0:
            print(f"Even Index of LOWER case : {s[i]}, {i}")
'''

# wap to find the > among 4 integer nos
'''
l = [1, 4, 6, 2]
i, g = 0, 0
while i < len(l):
    if l[i] > g:
        g = l[i]
    i += 1
print(g)
'''

# wap to check wethere the given no is armstrong no

# wap to print all the PERFECT nos b/w the range 1 to 1000 using while loop
# 6 -> 1 2 3 4 5 -> 1 + 2 + 3 = 6

'''
i = 1
while i <= 1000:
    j = 1
    sum = 0
    while j < i:
        if i % j == 0:
            sum += j
        j += 1
    if sum == i:
        print(i)
    i += 1
'''
'''
for i in range(1, 1000+1):
    s = 0
    for j in (1, i):
        if i % j == 0:
            s += j
            if s == i:
                print(i)
'''




# -------------------------- FOR LOOP ------------------------------------

# 1. wap to check wethere the given num is ARMSTRONG num r not
# 153 -> 1^3 + 5^3 + 3^3 -> 153
# power is length of the no

# with typecasting
'''
ip = int(input("Enter the no : "))
s = str(ip)
sum = 0
for i in s:
    sum += int(i) ** len(s)
if sum == ip:
    print("Armstrong No")
else:
    print("Not Armstrong No")
'''

# without using typecasting
'''
a = int(input("No : "))
n = a
i = 0
out = []
while n > 0:
    out = [n % 10] + out
    i += 1
    n //= 10
s = 0
for j in out:
    s += j ** i
if s == a:
    print("Armstrong no", s)
else:
    print("Not Armstrong no", s)
'''

# 2.  wap to get following o/p
# i/p : [10, 2.3, 'hello', 'python', 2437]
# o/p : ((10, 2), (2437, 4))
'''
ip = [10, 2.3, 'hello', 'python', 2437]
op = tuple()
for i in ip:
    if type(i) == int:
        op += ((i, len(str(i))),)

print(op)
'''

# 3. An organization plans to conduct a art competation where 4 teams will be participating n
# the team names r east, west, north n south now the organization has to prepare a schedule to conduct the contest
# b/w 2 teams at a time prepare the schedule list for all possible contest b/w the teams where no teams shd be
# competing more tha 1 time with same opponent n no team can compete on itself.

'''
l = ["East", "West", "North", "South"]
l1 = []
for i in l:
    for j in l:
        if i != j:
            l1.append([i, j])
            if [i, j] and [j, i] in l1:
                l1.remove([i, j])

for i in range(0, len(l1)):
    j, k = 0, 1
    print(f"{l1[i][j]} Vs {l1[i][k]}")
'''
'''
zone = ["East", "West", "North", "South"]
out = []
for i in zone:
    for j in zone:
        if i != j and (i+"vs"+j) not in out and (j+'vs'+i) not in out:
            out += [i+'vs'+j]
            # print(out)
            print(f"{i} vs {j}")
'''

# wap to get the following o/p wuthout using any in built method n slicing
# a = "Python Programming Language"
# op = {6 : 'nohtyP', 11 : "gnimmargorP", 8 : "egaugnaL"}

'''
a = "Python Programming Language"
op = {}
s = ""
c = 0
for i in a:
    if i != ' ':
        s = i + s
        c += 1
    else:
        op[c] = s
        s = ""
        c = 0
op[c] = s
print(op)
'''

# wap to print the series of PRIME nos b/n the range 1 to 50
'''
n = int(input("Enter No:"))
for i in range(1, n+1):
    ind = 0
    for j in range(2, i):
        if i % j == 0:
            ind = 1
    if ind == 0:
        print(i)
'''

# Check no

'''
n = int(input("No : "))
f = 0
for i in range(2, n):
    if n % i == 0:
        f = 1

if f == 0:
    print("Prime no")
else:
    print("Not Prime no")
'''


# wap to print the series of ARMSTRONG nos b/n the range 100 to 500
'''
num = int(input("Enter no : "))
for n in range(100, num+1):
    sum = 0
    for i in str(n):
        sum += int(i) ** len(str(n))
    if sum == n:
        print(n)
'''

# wap to print febonancie series from 0 till 50
'''
a = 0
b = 1
i = 0
while i <= 50:
    if a <= 50:
        print(a)
        c = a + b
        a = b
        b = c
    i += 1
'''

# wap to check the wethere no is febonancie no r not


# wap to generate otp using random module
# enter your mobile no as the ip n check whether mobile no is having 10 digits or not
# if it is having 10 dig no, wheather the first dig is in range b/n (6-9)
# if both the condition are true print 4 dig otp. otp shd be generated randomly using random module

'''
import random as rd
phno = int(input("Enter the Ph No : "))
i = 0
while phno != 0:
    d = phno % 10           # first num
    phno = phno // 10
    print(phno)
    i += 1                  # length of num
    

print(i, d)
if 6 <= d <= 9 and i == 10:
    a = rd.randint(1000, 9999)
    print(f"Your otp is : {a}")
else:
    print("Number is invalid!!!!")
'''


# important
# wa generic program to below series for any user entered num 10 upto 5 decimal places
# print the value of series for x = 2 correct to 4 decimal places w/o any in-built method
# note use of formula is not allowed in the prgm
# the prgm shd print accurate values upto 4 decimal places
# the addition of further element shd not change the value upto 4 decimal places, don't round off the value
# F(x) = 1/x + 1/x^2 + 1/x^3 + ............+ 1/x^(n)

'''
x = int(input("Enter the value for x : "))
n = int(input("Enter the value for n : "))
out = 0
c = 1
while c <= n:
    out += (1/(x ** c))
    c += 1

print(round(out, 4))            # built-in
print(float(str(out) [:6:]))    # w/o built-in
'''


# The first line of the ip consists of an integer - stock_size, representing yhe no of selected stocks(N),
# The second line consists of N space-separated integers - stock0, stock1, ......, stockn-1,
# representing the relative stock prices of the selected stocks.
# The third line consists of an integer - value K, representing the value K for which he to find the stock price

'''
def smalleststockprice(stock, vk):
    stock.sort()
    return stock[vk-1]


def main_stock():
    stock = []
    s_size = int(input("Stock Size : "))
    stock = list(map(int, input("Enter the list : ").split()))
    vk = int(input("K value : "))

    result = smalleststockprice(stock, vk)
    print(result)


main_stock()
'''


# ip = H1e2L3140&5%W$6o7r8l9D
# op = "HELLOWORLD123456789&%$"

'''
ip = "H1e2L3l4o&5%W$6o7r8l9D"
s = ""
n = ""
spe = ""
for i in ip:
    if "A" <= i <= "Z" or "a" <= i <= "z":
        s += i.upper()
    elif "0" <= i <= "9":
        n += i
    else:
        spe += i

print(s+n+spe)
'''
'''
s = "Roses are Red"
s1 = ""
for i in s.split():
    s1 += i[::-1]
    s1 += " "
print(s1)
'''

'''
s = "Roses are Red"
s1 = ""
for i in s.split():
    s1 = " " + i[::-1] + s1

print(s1)
'''

# Prime r not

'''

n = int(input("No : "))
for n1 in range(2, n):
    if n % n1 == 0:
        print("Not Prime")
        break
else:
    print("Prime")

'''

# Prime in range
'''
for i in range(100, 201):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
'''





# ----------------------------- NESTED FOR LOOP ---------------------------------

# -------------- Pattern Programs -------( pattern_prog.py ) --------------------


# ------------------------------ Functions -----------------------------------------


# Define a fun to extract all the integer values from the given collection

'''
def fun_ex(a, t = ()):
    for i in a:
        if type(i) == int:
            t += (i,)
    return t


print(fun_ex((1, 2.2, 2, 5+5j)))
'''

# define a fun to get the following o/p
# a = "xxxyxzzzyyyzxy"
# o/p = "x5y5z4"

'''
def fun(a, o=""):
    for i in a:
        c = 0
        for j in a:
            if i == j:
                c += 1
        if i not in o:
            o += i + str(c)
    return o
'''
'''
def fun(a, o=""):
    for i in a:
        c = 0
        if i in o:
            continue
        else:
            for j in a:
                if i == j:
                    c += 1
            o += i + str(c)
    return o

print(fun("xxxyxzzzyyyzxy"))
'''

# Define a fun to print n FIBONACCI no

'''
def fibo(n):
    n1 = 0
    n2 = 1
    print(n1, n2,end=" ")
    for i in range(2, n):
        n3 = n1 + n2
        print(n3, end=" ")
        n1, n2 = n2, n3
'''

'''
def fibo(n):            # Upto n
    n1 = 0
    n2 = 1
    print(n1, n2,end=" ")
    while n2 < n:
        c = n1 + n2
        n1, n2 = n2, c
        print(c, end=" ")
        '''
'''
0 1 1 2 3 5 
0 1 1 2 3 5 8 13 
0 1 1 2 3 5 8 13 21 
'''
'''
fibo(5)
print()
fibo(10)
print()
fibo(15)
'''

# define fun to CHECK the given no is FIBONACCI no r not

'''
def fibo(n):            
    n1 = 0
    n2 = 1
    l = []
    l.append(n1)
    l.append(n2)
    while n2 < n:
        c = n1 + n2
        n1, n2 = n2, c
        l.append(c)
    if n in l:
        print("Fibo")
    else:
        print("Not Fibo")

fibo(5)
fibo(4)
'''


# define fun to print all the STRONG nos b/w the range 1 to 200

'''
def strong_fun(m, n):
    for i in range(m, n+1):
        sum = 0
        for j in str(i):
            f = 1
            for k in range(1, int(j) + 1):
                f *= k
            sum += f
        if sum == i:
            print(i, end=" ")
    print()

strong_fun(1, 200)
strong_fun(1, 100000)
'''

'''
1 2 145 
1 2 145 40585 
'''


# define a fun to print the series of ARMSTRONG nos b/w the range 1 - 200

'''
def armstrong_fun(m, n):
    for i in range(m, n + 1):
        sum = 0
        for j in str(i):
            sum += int(j) ** len(str(i))
        if i == sum:
            print(i, end=" ")
    print()


armstrong_fun(1, 200)
armstrong_fun(100, 1000)
'''

'''
1 2 3 4 5 6 7 8 9 153 
153 370 371 407 
'''

# define a fun to check wethere the given no is HAPPY no r not

'''
def happy_fun(n):                  # Using List (No Recursion)
    l = []
    l.append(n)
    for i in l:
        j = str(i)
        for k in j:
            n = (int(k) ** 2)
        if n == 1:
            print("Happy No")
        elif n > 0:
            l.append(n)
        else:
            print("Not a Happy No")
'''

'''
def happy_fun(n):                   # Using Recursion
    for i in str(n):
        n = (int(i) ** 2)
    if n == 1:
        print("Happy No")
    elif n > 0:
        happy_fun(n)
    else:
        print("Not a Happy No")
'''
'''
happy_fun(7)            # Happy
happy_fun(10)           # Not Happy
# happy_fun(12)
happy_fun(49)           # Happy
happy_fun(100)          # Not Happy
'''

# SAD no r not

'''
def sad_fun(n):     # Using Recursion
    a = n
    for i in str(a):
        a = (int(i) ** 2)
    if a == n:
        print("Sad No")
    elif a > 0:
        sad_fun(a)
    else:
        print("Not a Sad No")


sad_fun(7)
sad_fun(10)
# sad_fun(14)
sad_fun(100)
sad_fun(49)           
'''

# PERFECT NO

'''
def perfect_fun(m, n):
    for i in range(m, n+1):
        sum = 0
        for j in (1, i):
            if i % j == 0:
                sum += j
        if sum == i:
            print(i)


perfect_fun(1, 1000)
'''


# wap to get the following o/p
# i/p : a = "xxxyyzzbbcczx"
# op1 : "x4y2z3b2c2"
# op2 : "twwde"

'''
def fun1(a):
    o = ""
    o1 = ""
    for i in a:
            c = 0
            if i in o:
                continue
            else:
                for j in a:
                    if i == j:
                        c += 1
                o += i + str(c)
                if "a" <= chr(ord(i) + c) <= "z":
                    o1 += chr(ord(i)+int(c))
                else:
                    o1 += chr(ord(i)-int(c))
    print(o)
    print(o1)

fun1("xxxyyzzbbcczx")
'''

# define a fun to get the following o/p
# a = "bruhat bengaluru maha nagara palike"
# o = {"'Ekilap' : 2, 'Aragan' : 2, 'Aham' : 2, 'Urulagneb' :3,'Tahurb' : 2"}

'''
def fun(a):
    d = {}
    for i in a[::-1].split():
        l = []
        for j in range(2, len(i)):
            if len(i) % j == 0:
                l.append(j)
        d[i.capitalize()] = l[0]
    print(d)


fun("bruhat bengaluru maha nagara palike")
'''


# ip = 4 5 6
#      7 8 9
#      10 11 -15

# op = |3 - 24| = 21
'''
def mat(ip):
    for i in range(0, len(ip)):
        sum = 0
        sum1 = 0
        for j in range(0, len(ip)):
            if i == j:
                sum += int(ip[i][j])
        print(sum)
'''

'''
def mat(ip):
    i = 0
    o1 = 0
    o2 = 0
    while i < len(ip):
        o1 += ip[i][i]
        i += 1
    j = 0
    while j < len(ip):
        i -= 1
        o2 += ip[j][i]
        j += 1
    print(abs(abs(o1)-abs(o2)))

'''
# mat([[4, 5, 6], [7, 8, 9], [10, 11, -15]])

# DATE AND TIME PROGRAM

# wap to check wethere the entered food item is avialable at current time r not idli- sambar is avialable in resto only at 7am till 10am and
# evening from 6pm till 8pm cosider the system time and check wethere the current sys time is present in the given time range
'''
from datetime import datetime

now = datetime.now()
ct = now.strftime("%H:%M:%S")

ip = input("Enter Food Item : ")

if ip == "idli":
    if "07:00:00" <= ct <= "10:00:00" or "06:00:00" <= ct <= "08:00:00":
        print("Idli")
    else:
        print("No Idli")
else:
    print("ONLY IDLI BRO !!!!!")
'''

# wap to print Good morning, ga, ge or gn based on the ip time entered the range of
# gm is "05:00AM-12:00pm"
# ga is "12:00pm-04:00pm"
# ge is "04:00pm-06:00pm"
# gn is > "06:00pm"
'''
from datetime import datetime

now = datetime.now()
ct = now.strftime("%H:%M:%S")
'''
'''
ip = input("Enter the time : ")

if "05:00am" <= ip <= "12:00pm":
    print("GOOD MORNING")
elif "12:00pm" <= ip <= "04:00pm":
    print("GOOD AFTERNOON")
elif "04:00pm" <= ip <= "06:00pm":
    print("GOOD EVENING")
else:
    print("GOOD NIGHT")
'''

























