USERNAME = "Shetty"
PASSWORD = "1234"
acc_num = "bank123456789"
balance = 1000

###################################

print("Welcome to Bank of BOSS", ("\N{winking face}") * 3)
print()
user_name = input("Enter the User Name : ")
password = input("Enter the Password : ")

if user_name == USERNAME and password == PASSWORD:
    print("Enter your choice :",
          "Press 1 to Check Balance",
          "Press 2 for Withdrawal",
          "Press 3 for Mini-statement",
          "Press 4 to Change Password",
          "Press 5 to Exit", sep='\n')

    choice = int(input("Enter your choice for further process : "))

    if choice == 1:
        print("     ", USERNAME, "Your Current balance is :", balance)

    elif choice == 2:
        amt = int(input("   Enter the amount to withdraw : "))
        if amt < 100:
            print("Please enter amount greater than 100(Shouldn't be in single digit!!).")
        elif amt < balance:
            print("     Withdraw is processing.....")
            print("     Collect your cash and receipt!!")
            print("     Available balance now is : ", (balance-amt))
        else:
            print("Insufficient balance!!!")

    elif choice == 3:
        print("Hi", USERNAME, "here is your bank details : ")
        print("     User name : ", USERNAME)
        print("     Account Number : ", acc_num)
        print("     Your last transactions on 20/07/2022 is credited Rs.500 to", acc_num)
        print("     Balance : ", balance)

    elif choice == 4:
        confirm = input("   Enter your Old Password : ")
        if confirm == password:
            NEW_PASS = input("   Enter new password : ")
            NEW_PASS1 = input("   Re-enter new password : ")
            if NEW_PASS == NEW_PASS1:
                Changed_pass = PASSWORD.replace(PASSWORD, NEW_PASS)
                PASSWORD = Changed_pass
                print("     ", PASSWORD)
                print("   Password changed successfully!!!")
            else:
                print("Confirmation Password is not matching try again!!")

        else:
            print("Unauthorised User!!!")

    elif choice == 5:
        print("     Have a nice TIME!!!")
        print("     Ending your transaction process.....")
    print("End of transaction process.....")

else:
    print("Enter valid USERNAME and PASSWORD")
