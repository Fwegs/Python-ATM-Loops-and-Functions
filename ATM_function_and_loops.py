
import random
database = {}

Balance = 0
def init():
    print("------- Welcome to Fwegs bank -----")

    Haveaccount = int(input("Do you have account with us 1 (yes) 2 (no) \n"))
   
    if(Haveaccount == 1):
        Login()
    elif(Haveaccount == 2):
        Registration()
    else:
        print("you have selected an invalid option")
        


def Login():
    print("******** Login  ********")

    accountnNumberFromUser = int(input("what is your account number \n"))
    password = input("what is your password \n")

    for accountnumber,userdetails in database.items():
        if(accountnumber == accountnNumberFromUser):
            if(userdetails[3] == password):
                bankoperation(userdetails)
    else:
        print("invalid account or password")
        Login()  

def Registration():
    print("********  REGISTER  ********")

    email = input("What is your e_mail address \n")
    first_name = input("what is your first name \n")
    last_name = input("what is your last name \n")
    password = input("what is your password \n")
    accountnumber = generationAccountNumber()

    database[accountnumber] = [ first_name, last_name, email, password]
    
    print("Your account Has been successfully created")
    print("== ==== ====== ==== ==")
    print(f"Your account number is:  {accountnumber} ")
    print("make sure you keep it safe")

    Login()

def bankoperation(user):
    print("Welcome %s %s " % ( user[0], user[1] ) )  
    
   

    selectedOption = int(input("What do you like to do (1) Withdrawal (2) deposit (3) logout (4) exit \n"))

    if(selectedOption == 1):
           
        withdrawal_operation()
    elif(selectedOption == 2):
            
        deposit_operation()
    elif(selectedOption == 3):
        Login()
    elif(selectedOption == 4):
        exit()
    else:
        print("invalid option selected")    
        bankoperation(user)

def withdrawal_operation():
    print(f"your balance is : #{Balance}")
    print("==================")
    withdraw = int(input("How much do you want to withdraw? \n"))

    if(Balance > withdraw):
        print("Take your cash")
        print("=================")
        print (f"Your current balance is #{Balance - withdraw}")

    else:
        print("Insufficient Balance")


    another_action()

def deposit_operation():
    print(f"your balance is : #{Balance}")
    deposit = int(input("How much do you want to deposit \n"))
    
    current_balance = (Balance + deposit)
    print(f"your current balance is #{current_balance}")

    another_action()

def another_action():
    more_actions = int(input("do you want to perform another operation (1) yes (2) no \n"))   

    if(more_actions == 1):
        Login()
    elif(more_actions == 2):
        exit()
    else:
        print("invalid option selected, try again")
        another_action()
    
def logout():
    Login()

def generationAccountNumber():
    
    return random.randrange(1111111111, 9999999999)



init()
print(generationAccountNumber())
