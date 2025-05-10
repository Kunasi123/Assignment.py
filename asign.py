
account={}
def create_password():
    user_pin =input("Enter a password: ")        
    with open ("login.txt","w") as file:
        file.write(user_pin)
        print("password saved.")


def Saved_password():
    try:
        with open ("login.txt","r") as file:
            return file.read()
    except FileNotFoundError:
        return None


def check_password():

        password=Saved_password()
        if password is None:
            print("password is none")
            create_password()
        else:
            user_pass=input("Enter your password: ")
            if user_pass==password:
                
                print("login successfully")
                
            else:
                print("incorrect password")
                exit()
                
                       
def next_id():
    try:
        with open("users.txt","r")as file:
            lines= file.readlines() 
            if not lines:
                return "1000"
            last_id=int(lines[-1].split(",")[0])
            return str(last_id + 1)
    except FileNotFoundError:
        return "1000"

import random
def account_no():
    while True:
        account_number="22"+ str(random.randint(10000000,99999999))
        if account_number not in account:
            return account_number

def create_account():
    print("=======Create Accounts=======")
    name=input ("enter your name: ")
    Address=input("Enter your address: ")
    user_name=input("Enter user name: ")
    intial_balance=float(input("Enter amount: "))
    user_no=next_id()
    acc=account_no()
    account[acc]={"user_id":user_no,
                  "account_num":acc,
                  "name":name,
                  "address":Address,
                  "user_name":user_name,
                  "balance":intial_balance

    }
    with open("accounts.txt","a")as file:
        file.write(f"{user_no},{acc},{name},{Address},{user_name},{intial_balance}\n")
    with open ("customer.txt","a")as file:
        file.write(f"{acc},{intial_balance}\n")
       
    with open("users.txt","a")as file:
        file.write(f"{user_no},{acc},{user_name}\n")    
    print("Account created successfully!. Thank you.")
    
def user():
    acc_no=input("enter your account number: ")
    if acc_no not in account:
        return acc_no
    
import datetime
def Deposit_money():
    print("=======Deposit money=======")
    Acc=user()
    if not Acc:
        return
    
    while True:
        try:
            amount=float(input("enter the deposit amount: "))
            if amount<=0:
                print("number is negative")
            else:
                break    
        except ValueError:
            print("invalid input!")
            return
    cust=[]
    found=False
    try:
        
        with open("customer.txt","r") as file:
            for line in file:
                account_num,balance= line.strip().split(",")
                
                if Acc==account_num:
                    
                
                    balance=float(balance)+ amount
                    cust.append(f"{account_num},{balance}\n")
                    found=True
                else:
                    cust.append(line)

    except FileNotFoundError:
        print("file not found")
        return

    if not found:
        print("account not found")
        return
    with open("customer.txt","w")as file:
        file.writelines(cust)
    with open("transaction.txt","a")as file:
        file.write(f"{datetime.datetime.now()},{Acc},Deposit amount:{amount},{balance}\n")

    print("deposit successfully. Thank you!!")
    
def Withdrew_money(): 
    print("======Withdrew Money======")
    Acc=user()
    if not Acc:
        return
    while True:
        try:
            amount=float(input("enter the withdrew amount: "))
            if amount<=0:
                print("number is negative")
            else:
                break
                print("")
        except ValueError:
            print("invalid input!")
    bal=[]
    found=False
    
    try:
        with open("customer.txt","r") as file:
            for line in file:
                account_num,balance= line.strip().split(",")
                
                if Acc==account_num:
                    found=True
                    
                    if amount<=float(balance):
                        balance=float(balance)+amount
                        
                        
                        
                        bal.append(f"{account_num},{balance}\n")
                        
                    else:
                        print("the amount is greater thanbalance.please try again.")
                        bal.append(line)
                else:
                    bal.append(line)
    except FileNotFoundError:
        print("the file is not found")
        return
    if not found:
        print("Account number not found.")
        return
        
    with open ("customer.txt","w")as file:
        file.writelines(bal)
    with open("transaction.txt","a")as file:
        file.write(f"{datetime.datetime.now()},{Acc},Withdrewal amount:{amount}\n")
          
    print("Withdrew successfully.Thank you")


def check_balance():
    print("======Check Balance======")
    acc=user()
    if not acc:
        return
    
    try:
        with open("customer.txt","r")as file:
            for line in file:
                account_num,balance=line.strip().split(",")
                
                if acc==account_num:
                    balance=float(balance)
                    print(f"your current balance is:{balance}")
                    break
                else:
                    print('account number not found')
    except FileNotFoundError:
        print("file not found")


def Transaction_history():
    print("======Transaction History======")
    acc=user()
    if not acc:
        return
    found=False
    try:
        with open("transaction.txt","r")as file:
            for line in file:
                data=line.strip().split(",")
                account_n=data[1]
                if acc==account_n:
                    print(f"Transaction:{line.strip()}")
                    found=True
        if not found:
            print("no transaction in this account.")
    except FileNotFoundError:
        print("The file was not found.")
       
def Admin():
    print("======Admin Services======")
    while True:
        check_password()
        print("1.create account")
        print("2.Deposit Money")
        print("3.Withdrew Money")
        print("4.Check Balance")
        print("5.Transaction History")
        print("6.Exit")
        try:
            Check=int(input("Enter a number(1-6): "))
            if Check==1:
                create_account()
                break
            elif Check==2:
                Deposit_money()
                break
            elif Check==3:
                Withdrew_money()
                break
            elif Check==4:
                check_balance()
                break
            elif Check==5:
                Transaction_history()
                break
            elif Check==6:
                print("Exit")
                break
            else:
                print("Number is incorrect.Please try again")
        except ValueError:
            print("Invalid input.Please try again")

def customer():
    print("======Customers Services======")
    while True:     
        print("1.Deposit Money")
        print("2.Withdrew Money")
        print("3.Check Balance")
        print("4.Transaction History")
        print("5.Exit")
        try:
            Check=int(input("Enter a number(1-6): "))
            if Check==1:
                Deposit_money()
                break
            elif Check==2:
                Withdrew_money()
                break
            elif Check==3:
                check_balance()
                break
            elif Check==4:
                Transaction_history()
                break
            elif Check==5:
                print("Exit")
                break
            else:
                print("Number is incorrect.Please try again")
        except ValueError:
            print("Invalid input.Please try again")


def menu():
    while True:
        print("========Welcome to mini bank========")
        print("1.Admin service")
        print("2.Customer service")
        print("3.Exit")
        
        try:
            check=int(input("Enter a number(1-3): "))
            if check==1:
                Admin()
                
            elif check==2:
                customer()
                
            elif  check==3:
                print("Exiting.Thank you!")
                break
            else:
                print("incorrect number!. Please try again")
        except ValueError:
            print("Invalid input. Please try again")
            break
menu()            
