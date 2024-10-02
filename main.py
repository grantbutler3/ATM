Greeting = "Welcome to Butler Banking"
print(Greeting)
Trails = 3
UserPin = 1234

while Trails != 0:
    Pin = int(input("please Enter Your 4 Digit Pin Number"))
    if Pin != UserPin:
        Trails -= 1
        print("Wrong Pin Number. You have", Trails, "Trails Left")
    else:
        UserChoice = input("d: Depost or w: Withdraw: ")
        if UserChoice == "d":
            UserDeposit = input("Enter The Amount You Would Like To Deposit: ")
            print(UserDeposit, "$ Have Been Deposited Into Your Account")
        if UserChoice == "w":
            UserWithdraw = input("Enter The Amount You Would Like To Withdraw: ")
            print(UserWithdraw, "$ Have Been Withdrawed Into Your Account")
    UserExit = input("Would You Like To Continue? Y/N: ")
    if UserExit == "N":
        print("Thank You For Using Butler Banking")
        break
    else:
        continue

