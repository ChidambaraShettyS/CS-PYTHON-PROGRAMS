# Conditional examples

# if statement

# wapt check no is positive

'''num = int(input("enter the number : "))

if num > 0 :
    print("Number is positive")

print("end of execution!!")'''


# wapt check is given number is even

'''num = int(input("enter the number : "))

if num % 2 == 0 :
    print("Given number is even")

print("end of execution")'''


# wapt check the given number is even or odd

'''num = int(input("enter the number : "))

if num % 2 == 0 :
    print("Given number is even")
else:
    print("Given number is odd")'''

# wapt check the given alphabet is vowel or not

'''alpha = input("enter alphabet :")[0]

if alpha in 'aeiou' :
    print("The given alphabet is vowel")
else:
    print("The given alphabet is not vowel")

print("End of program")'''

# wapt check if the string is of even length or not

'''s = input("enter the string : ")

if len(s) % 2 == 0 :
    print("String length is even")
else:
    print("String length is odd")

print("End of program")'''

# wapt accept percentage from user and display the grade according to the following criteria :
'''>90 grade A
>80 and <=90 grade B
>=60 and <=80 grade C
below 60 grade D
below 35 Fail'''

'''marks = int(input("Please enter the marks : "))

if 0 <= marks < 35:
    print("You Failed exam !! ")
elif 35 <= marks <= 100:
    print("You Passed exam !!")
    if marks > 90:
        print("Grade A !! ")
    elif 80 < marks <= 90:
        print("Grade B !! ")
    elif 60 <= marks <= 80:
        print("Grade C !! ")
    else:
        print("Grade D !! ")
else:
    print("Please enter the correct marks !! ")
'''

# Check if the entered character is vowel or not, if it is vowel create a dictionary with char and its ascii value pair

'''char = input("enter the character : ")
vowel = 'aeiouAEIOU'
d = {}

if char in vowel:
 print("Entered Character is vowel!!!")
 asc = ord(char)
 d.update({char: asc})
 print(d)

else:
 print("Entered Character is not vowel!!!")'''

# The given number is divisible by 5 or not

'''num = int(input("Enter the number : "))

if num % 5 == 0:
 print("Entered number is divisible by 5.")
else:
 print("Entered number is not divisible by 5.")'''

# In a number check if the second last number is even or not

'''num = 1234
n = str(num)
n1 = n[-2]
num1 = int(n1)

if num1 % 2 == 0:
 print("The last second number is EVEN!!")
else:
 print("The last second number is ODD!!")'''




























































































































































































































































































