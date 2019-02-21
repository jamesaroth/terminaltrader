
def welcome():
    print("Welcome to KnightRider Trader\nPlease select from the following options\n\n")

def enter_info():
    print("Please Enter the following information\n")

def main_menu():
    answer = input("1. Create an Account\n2. Login\n3. Quit\nYou select: ")
    return answer

def username_inpt():
    inpt = input("Enter your username: ")
    return inpt

def password_inpt():
    inpt = input("Enter your password: ")
    return inpt

def set_password_inpt():
    inpt = input("Create your secure password: ")
    return inpt

def invalid_info():
    print("Invalid account number or Password. Try again\n")

def choose_valid():
    print("Please choose valid options. Try again\n")

def enter_digit():
    print("Enter a single numerical digit only\n")
 
def program_end():
    print("Thank You for trading with us! Come back soon!\n")

def saving_change():
    print("Changes have been saved\n\n")

def acc_created(username):
    print("A new account for the username: {} has been created\n".format(username))

def trading_menu(username, accnumber):
    print('Hello '+ username + "Please choose from the following options:\n")
    inpt = input("1. Check Balance\n2. Deposit Funds\n3. Buy a stock\n4. Sell a stock\n5. View detailed stock position holdings\n6. View detailed trade history\n7. Reset password\n8. Logout and return to main menu\n\nYou select: ")
    return inpt

def deposit_inpt():
    inpt = input("How much would you like to deposit into your account? ")
    return inpt

def deposit_outp(amount):
    print("You deposited ${} to your account. Changes have been saved\n".format(amount))
    
def balance_statement(amount):
    print("Your account cash balance is: {} dollars\n".format(amount))

def newbalance_statement(amount):
    print("Your new account cash balance is: {} dollars\n".format(amount))

def not_funds(amount):
    print("You don't have enough funds to withdraw ${}".format(amount))
