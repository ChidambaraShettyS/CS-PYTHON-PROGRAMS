
'''
obj = open("student.txt", "w")
n = int(input("Enter the no of students : "))
for i in range(n):
    rno = input("Roll No : ")
    name = input("Name : ")
    marks = input("Marks : ")
    data = rno + "," + name + "," + marks + "\n"
    obj.write(data)
obj.close()
print("Successfully data entered into the file ......")

obj = open("student.txt", "r")
print("Data entered is :")
data = obj.read()
print(data)
'''