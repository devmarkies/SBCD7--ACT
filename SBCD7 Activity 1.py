import random

accounts = {}

def create_account():
    user_id = random.randint(1000, 9999)
    balance = 1000  
    accounts[user_id] = balance
    print(f"Account created successfully! Your user ID is {user_id}")
    print(accounts)
    return user_id

def balance_enquiry():
    user_id = int(input("Enter your user ID: "))
    if user_id in accounts.keys():
        print(f"Total balance: {accounts[user_id]}")
    else:
        print("Wrong id")
    print('')

def withdraw_cash():
    user_id = int(input("Enter your user ID: "))
    if user_id in accounts.keys():
            amount = int(input("Enter amount you want to withdraw: "))
            if amount >int (accounts.get(user_id)):
                print("Enough balance.")
            else:
                accounts[user_id] = int (accounts.get(user_id))- amount
                print(f"{amount}Your remaining balance is {accounts[user_id]}")
                print(accounts)
    else:
        print("Wrong id")

def deposit():
    user_id = int(input("Enter your user ID: "))
    if user_id in accounts.keys():
            amount = int(input("Enter amount you want to withdraw: "))
            if amount >int (accounts.get(user_id)):
                print("Enough balance to wihdraw.")
            else:
                accounts[user_id] = int (accounts.get(user_id))+ amount
                print(f"{amount} successfully withdraw. Your remaining balance is {accounts[user_id]}")
                print(accounts)

    else:
        print("Wrong id")

def delete_account():
    user_id = int(input("Enter your user ID: "))
    if user_id in accounts.keys():
        accounts.pop(user_id)
        print("Account deleted successfully")
    else:
        print("Wrong id")

is_quit = False


while not is_quit:
    print("Please select an option:")
    print("1. Create Account")
    print("2. Withdraw Cash")
    print("3. Balance Enquiry")
    print("4. Deposit")
    print("5. Delete Account")

    num = int(input("Enter the number: "))
    if num ==1:
         create_account()     
    elif num == 2:
        withdraw_cash()
    elif num == 3:
        balance_enquiry()
    elif num == 4:
        deposit()
    elif num == 5:
        delete_account()
    elif num ==7:
        break
    elif num == 6:
        print(accounts)
        user_id = int(input("Enter your user ID: "))
        print(accounts.get(user_id))
        
    else:
        print("Please select the exact value")
