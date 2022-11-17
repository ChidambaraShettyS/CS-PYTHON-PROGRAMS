# ------------ Class Creation ----------------
''''''

# Example Program
'''
class Laptop:               # class creation with class_name Laptop
    ram = '8GB'             # class variables or states
    rom = '1TB SSD'


laptop_1 = Laptop()         # obj 1
laptop_2 = Laptop()         # obj 2


print(laptop_1)
print(laptop_2)
print(laptop_1.ram)
print(laptop_1.rom)
print(laptop_2.ram)
print(laptop_2.rom)
'''


# Example for class and methods (magic methods and alternate methods)
'''
class Bike:                                     # Class creation
    color = "Black"                             # class variables
    wheels = 2
    milaze = "30km"

    def __init__(self, engine, brakes):         # constructor magic method r dunder method
        self.engine = engine                    # Object variables
        self.brakes = brakes
        # self.milaze = milaze

    def mechanic(self, engine, brakes, color, wheels):         # Alternate constructor method
        self.engine = engine
        self.brakes = brakes
        self.color = color
        self.wheels = wheels


ninja = Bike("500cc", "ABS")                    # Objects creation
honda = Bike("250cc", "ABS")

print("Ninja :")
print(ninja.engine)
print(ninja.brakes)
print(ninja.milaze)
print("Honda :")
print(honda.engine)
print(honda.brakes)
print(honda.color)
print(honda.wheels)
print(honda.milaze)
print("---------------")

honda.mechanic("750cc", "Disc", "Blue", 4)         # Modifying the obj with alternate method

print("Honda :")
print(honda.engine)
print(honda.brakes)
print(honda.color)
print(honda.wheels)
'''


# BankAccount
'''
class BankAccount:

    def __init__(self, owner: str, balance: int = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: int):
        self.balance += amount

    def withdrawal(self, amount: int):
        if self.balance > amount:
            self.balance -= amount
            print("Transaction completed successfully...")
        else:
            print("Insufficient Balance...... ")


acc_1 = BankAccount("Ram", 2000)
acc_2 = BankAccount("Sham", 2000)

print(acc_1.owner)
print(acc_1.balance)
acc_1.deposit(500)
print(acc_1.balance)
acc_1.withdrawal(200)
print(acc_1.balance)
'''


# Circle
'''
class Circle:

    def __init__(self, x_co: float, y_co: float, radius: float):
        self.x_co = x_co
        self.y_co = y_co
        self.radius = radius

    def find_area(self):
        print(((self.x_co - self.radius) ** 2) + ((self.y_co - self.radius) ** 2))

    def find_circumference(self):
        pass


obg1 = Circle(2.3, 3.2, 2.0)
obg1.find_area()
obg1.find_circumference()
'''


# Books
'''
class Books:

    def __init__(self, book_data: dict, book_id: int, book_name: str, book_author: str, year_of_publish: str, price: float):
        self.book_data = book_data
        self.book_id = book_id
        self.book_name = book_name
        self.book_author = book_author
        self.year_of_publish = year_of_publish
        self.price = price

    def add_new_book(self, book: str):
        self.book_data["Book_name"] = book

    def delete_book(self, book: str):
        for ele in self.book_data:
            if self.book_data[ele] == book:
                del ele

    def display_book(self, book: str):
        pass

    def inquire_book(self, book: str):
        pass


obj1 = Books({}, 1, "java", "Abc", "12/04/1992", 200)
obj1.add_new_book("Python")
print(obj1.book_data)
obj1.add_new_book("Java")
print(obj1.book_data)

'''


# ListData
'''
class ListData:

    def __init__(self, list_: list):
        self.list_ = list_
    
    def add_data(self, ele):
        self.list_ += [ele]

    def find_length(self):
        count = 0
        for i in self.list_:
            count += 1
        return count

    def delete_data(self, ele):
        for index in range(0, self.find_length()):
            item = self.list_[index]
            if item == ele:
                del self.list_[index]
                break

    def find_data(self, ele):
        for index in range(0, self.find_length()):
            item = self.list_[index]
            if item == ele:
                print(index)


obj1 = ListData([1, 2, 3, 4])
print(obj1.list_)

obj1.add_data("Hello")
print(obj1.list_)

print(obj1.find_length())

obj1.delete_data(2)
print(obj1.list_)

obj1.find_data("Hello")
'''


# DateClass
'''
class DateClass:
    
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year
    
    def set_date(self):
        pass
    
    def get_day(self):
        pass
    
    def get_month(self):
        pass
    
    def get_year(self):
        pass
    
    def print_date(self):
        pass
    
'''

# Student
'''
class Student:

    def __init__(self, sname: str, sid: int, location: str):
        self.sname = sname
        self.sid = sid
        self.location = location

    def display(self):
        print(f"Student details : {self.sname} {self.sid} {self.location}")

    def add(self, l:list):
        std = []
        std.append(l)
        print(std)
    
    def edit(self):
        pass
    
    def delete(self):
        pass
    
    
ram = Student("Ram", 101, "Ban")
ram.display()
ram.add(["cs", 102, "Ban"])
ram.add(["cs", 103, "Ban"])
'''











































































































