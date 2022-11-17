# Accepting the electricity units from user and calculate the bill according to the following rates
# First 100 units     : Free
# 101 - 300 units      : Rs.2 per units
# Above 300 units      : Rs.5 per units
# ex: 500 -----> bill = 0 + 400 + 1000 => 1400

'''
units = int(input("Enter the number of units used : "))
bill = 0
count = 0

while count <= units:
    if 0 <= count <= 100:
        bill += 0
    elif 101 <= count <= 300:
        bill += 2
    elif count > 300:
        bill += 5

    count += 1
print(bill)
'''

# Accept the number of days from user and calculate the charge for library according to following
# Till 5 days : Rs.2 / day
# 6 - 10 days : Rs.3 / day
# 11 - 15 days : Rs.4 / day
# After 15 days : Rs.5 / day

'''
days = int(input("Enter the number of days due : "))

charge = 0
count = 0

while count <= days:
    if 1 <= count <= 5:
        charge += 2
    elif 6 <= count <= 10:
        charge += 3
    elif 11 <= count <= 15:
        charge += 4
    elif count > 15:
        charge += 5
    count += 1
print(charge)
'''

# Accept the kilometers covered and calculate the bill according to following criteria
# First 10km : Rs.11 / km
# Next 90km : Rs.10 / km
# After that : Rs.9 / km

'''
km = int(input("Enter the km covered : "))

count = 0
bill = 0

while count <= km:
    if 1 <= count <= 10:
        bill += 11
    elif 11 <= count <= 90:
        bill += 10
    elif count > 90:
        bill += 9
    count += 1

print(bill)
'''




# ip = i am so amazed by the sheer excellence of this boy . I am so so so greatful for this ///// "so"
# op = 4
'''
ip = "i am so amazed by the sheer excellence of So this boy . I am so so so greatful for this"
c = 0
for i in ip.split():
    if i.lower() in "so":
        c += 1
print(c)
'''


# data = [1, 2, 3, 4, 5, 6]
# op = [2, 1, 4, 3, 6, 5]
'''
def even_swap(data):
    n = len(data)
    l1 = []
    i = 0
    j = 2
    while 0 < n:
        var = data[i:j]
        var1 = var[::-1]
        l1.append(var1[0])
        l1.append(var1[1])
        i += 2
        j += 2
        n -= 2
    return l1


def swap(data):
    if len(data) % 2 == 0:
        print(even_swap(data))
    else:
        p = data.pop()
        a = even_swap(data)
        a.append(p)
        print(a)
'''

'''
def swap(data):
    l = []
    for i in range(1, len(data), 2):
        l.append(data[i])
        l.append(data[i-1])
    if len(data) % 2 != 0:
        l.append(data[-1])
    print(l)
'''

'''
swap([1, 2, 3, 4, 5, 6])
swap([1, 2, 3, 4, 5, 6, 7])
'''

# Car

'''
class CarDealer:
    rto =113990
    tcs = 11000

    def _init_(self, car_model):
        self.car_model = car_model

        i = input("Do you want Insurance : ")
        self.insurance = 47300 if i == 'Yes' else 0

        a = input("Do you need any additional accessories : ")
        self.accessories = 15000 if a == 'Yes' else 0

        dis = input("Dealer discount : ")
        self.dis = dis


    def get_price(self):
        d = {'Polo_Trendline': 870000, 'Polo_Highline': 1090000, 'Virtus_Trendline': 1105000 , 'Virtus_Highline': 1308000, 'Tigun_Trendline': 1489000, 'Tigun_Highline': 1542000 , 'Tigun_Topline': 1771000}
        total = 0
        for key, value in d.items():
            if self.car_model == key:
                cost = value


        if self.insurance == 0 and self.accessories == 0:
            print("Any one of the additional features has to be added to get discount")
            self.dis = 0
            total = cost + self.insurance + self.accessories + CarDealer.rto + CarDealer.tcs

        else:
            for j in self.dis:
                if j == "%":
                    self.dis = self.dis.strip("%")
                    self.dis = ((int(self.dis)) / 100) * cost
            if int(self.dis) > 30000:
                self.dis = 30000
                total = cost + self.insurance + self.accessories + CarDealer.rto + CarDealer.tcs - int(self.dis)
            else :
                total = cost + self.insurance + self.accessories + CarDealer.rto + CarDealer.tcs - int(self.dis)
        print(total)



car_name = input("Select car model : ")
car_1 = CarDealer(car_name)
amount = car_1.get_price()

car_name = input("Select car model : ")
car_2 = CarDealer(car_name)
amount = car_2.get_price()

'''

'''
class Car:
    cars = {"Polo Trendline" : 870000, "Polo Highline" : 1009000, "Virtus Trendline" : 1105000, "Virtus Highline" : 1308000, "Taigun Trendline" : 1489000, "Taigun Highline" : 1542000, "Taigun Topline" : 1771000}
    RTO = 113990
    insurance = 47300
    TCS = 11000
    additional = 15000

    def __init__(self, car_name):
        print(self.cars)
        self.car_name = car_name
        if self.car_name in self.cars:
            self.insu = input("Do you need Insurance : ")
            self.add_acc = input("Do you need Additional Accessories : ")
            if self.insu == "yes" or self.add_acc == "yes":
                print("You can get discount upto 30,000 !!!")
                self.dis = int(input("Dealer discount : "))
                self.bill(self.dis, self.insu, self.add_acc)
            else:
                print("You Cant Claim Discount!!!")
                self.dis = int(input("Dealer discount : "))
                self.bill(self.dis, self.insu, self.add_acc)

        else:
            print("Out of Stock!!!")

    def bill(self, diss, insu, add_acc):
        self.diss = diss
        self.insu = insu
        self.add_acc = add_acc
        if self.insu and self.add_acc == "yes":
            total = self.cars[self.car_name] + self.RTO + self.TCS + self.insurance + self.additional - self.diss
            print(f"Your total bill is {total} ")
        elif self.insu or self.add_acc == "yes":
            if self.insu == "yes":
                total = self.cars[self.car_name] + self.RTO + self.TCS + self.insurance - self.diss
                print(f"Your total bill is {total} ")
            elif self.add_acc == "yes":
                total = self.cars[self.car_name] + self.RTO + self.TCS + self.additional - self.diss
                print(f"Your total bill is {total} ")
        else:
            total = self.cars[self.car_name] + self.RTO + self.TCS
            print(f"Your total bill is {total} ")


print({"Polo Trendline" : 870000, "Polo Highline" : 1009000, "Virtus Trendline" : 1105000, "Virtus Highline" : 1308000, "Taigun Trendline" : 1489000, "Taigun Highline" : 1542000, "Taigun Topline" : 1771000})
c = input(f"Select car : ")
car1 = Car(c)
'''


# Employee Table
'''
emp_sal = {"A": 1000, "C": 3000, "B": 2000, "D": 4000, "E": 2000, "F": 1500, "G": 7000}
emp_dep = {"A": "IT", "C": "IT", "B": "IT", "D": "HR", "E": "HR", "F": "IT", "G": "HR"}
it = []
hr = []

for i, j in emp_dep.items():
    if j == "IT":
        it.append(emp_sal[i])
    elif j == "HR":
        hr.append(emp_sal[i])
it.sort()
hr.sort()

for i, j in emp_sal.items():
    try:
        if emp_dep[i] == "IT":
            print([i, j, emp_dep[i], it[it.index(j)+1]])
        elif emp_dep[i] == "HR":
            print([i, j, emp_dep[i], hr[hr.index(j)+1]])

    except Exception:
        print([i, j, emp_dep[i]])

'''

'''
n1 = input("N1 : ")
n2 = input("N2 : ")

a = input("No :")
b = input("No :")

if int(n1) == len(a) and int(n2) == len(b):
    c = int(a[::-1]) + int(b[::-1])
    print(str(c)[::-1])
'''


# Geek has N food items. Every sec Geek will eat:
# N/2 foods items if N is divisible by 2
# N+1/2 foods items if N is not divisible by 2
# i/p : 4, o/p : 3
# i/p : 0, o/p : 0

'''
def solve(N, s=0):
    if N % 2 == 0:
        N = N // 2
    else:
        N = (N+1)//2
    s += N
    if N >= 2:
        solve(N, s)
    else:
        print(s)


solve(4)
solve(0)
solve(6)
'''

# Using Class

'''
class Solution:
    def solve(self, N, s=0):
        if N % 2 == 0:
            N = N // 2
        else:
            N = (N+1)//2
        s += N
        if N >= 2:
            obj.solve(N, s)
        else:
            print(s)


obj = Solution()
obj.solve(4)
obj.solve(0)
'''

'''
a = "abcdefabcdabefgabeabc"
b = "ab"

c = a.split(b)
d = 0

for i in range(len(c)-1):
    d += 1

print(d)
'''

# String : abcd
# {'bcd', 'b', 'cd', 'ab', 'bc', 'c', 'abcd', 'abc', 'd', 'a'}
# 4 substring with vowel alphabets
'''
s = input("String : ")
ss = set()
for i in range(0, len(s)):
    for j in range(i, len(s)):
        ss.add(s[i:(j+1)])
print(ss)

c = 0
for i in ss:
    for j in i:
        if j in "AEIOUaeiou":
            c += 1
print(c)
'''

# Strange nos count
'''
L = int(input("Low range :"))
R = int(input("High range :"))

c = 0
for i in range(L, R+1):
    for j in str(i):
        for k in range(2, int(j)+1):
            if int(j) % k == 0:
                break
        else:
            c += 1

print(c)
'''
'''
for i in range(1, 101):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
'''

# 5
# 1
# 0
# 1
# 0
# 0
# 0 0 0 1 1
'''
a = int(input())
l = []
for i in range(1, a+1):
    b = int(input())
    l.append(b)

l.sort()
for i in l: 
    print(i, end=" ")
'''

# String :commission
# 4
# 1
'''
s = input("String :")
for i in range(0, len(s)):
    if s[i] == s[i+1]:
        print(i+2)
        break
    # else:
    #     print(0)
    #     break

for i in s:
    if s.count(i) == 1:
        print(s.index(i)+1)
        break
    # else:
    #     print(0)
    #     break
'''

# All elements shd be unique shd not be sorted elements shd be > 0 and <= length of list
# --> Good else BAD
'''
A = []
N  = int(input())
for i in range(1, N+1):
    n = int(input())
    A.append(n)

f1 = 0
f2 = 0
f3 = 0

for i in A:
    if A.count(i) > 1:
        f1 = 1

if A == sorted(A):
    f2 = 1

for i in A:
    if i < 0 or i > N:
        f3 = 1

if f1 == 1 or f2 == 1 or f3 == 1:
    print("BAD")
else:
    print("GOOD")
'''

# Maximum Array Difference

'''
def maxDiff(arr):
    max_diff = arr[1] - arr[0]

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if (arr[j] - arr[i]) > max_diff:
                max_diff = arr[j] - arr[i]

    print(max_diff)


# Driver program to test above function
maxDiff([2, 3, 10, 6, 4, 8, 1])
maxDiff([1, 2, 90, 10, 110])
maxDiff([7, 9, 5, 6, 3, 2])
'''

# Sum Pair in an Array

'''
def sum_pair(arr, sum):
    l1 = []
    for i in arr:
        for j in arr:
            if (i + j) == sum:
                if (i, j) not in l1 and (j, i) not in l1:
                    l1.append((i, j))
    print(l1)


sum_pair([0, 1, 2, 3, 4, 5, -1], 4)
'''


# Palindrome Counter

'''
def pali_count(s):
    s1 = set()

    for i in range(len(s)):
        for j in range(i, len(s)):
            s1.add(s[i : (j+1)])

    c = 0
    for i in s1:
        if i == i[::-1]:
            c += 1
    print(c)


pali_count("level")
pali_count("mam")
'''

# Factorial Logic

'''
def factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    print(f)


factorial(3)
factorial(5)
'''


n = int(input("No : "))
sum = 0
for i in range(2, n+1):
    ind = 0
    for j in range(2, i):
        if i % j == 0:
            ind = 1
    if ind == 0:
        sum += i

print(sum)












































