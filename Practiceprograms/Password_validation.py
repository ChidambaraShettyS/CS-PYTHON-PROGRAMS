# WAPTC the validity of password input by user
# password must contain of minimum 8 characters length and must contain at least :
# 1 uppercase, 1 lowercase, 1 special char, 1 number

password = input("Enter the Strong Password : ")
c_up = 0
c_low = 0
c_spl = 0
c_num = 0

for char in password:
    if 'A' <= char <= 'Z':
        c_up += 1
    elif 'a' <= char <= 'z':
        c_low += 1
    elif '0' <= char <= '9':
        c_num += 1
    else:
        c_spl += 1

if len(password) < 8:
    print("Password should contain minimum 8 characters")
elif c_up < 1:
    print("Password should contain atleast 1 uppercase character ")
elif c_low < 1:
    print("Password should contain atleast 1 lowercase character ")
elif c_num < 1:
    print("Password should contain atleast 1 Number ")
elif c_spl < 1:
    print("Password should contain atleast 1 Special character ")
else:
    print(" Password Validated it is a Strong Password")















