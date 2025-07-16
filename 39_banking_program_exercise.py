# Banking program in python

def show_balance():
    print(f"Your balance is ${balance: .2f}")

def deposite():
    amount = float(input("Enter an amount to be deposited: "))
    
    if amount < 0:
        print("That is not a valid amount !")
        return 0
    else:
        return amount

def withdraw():
    amount = float(input("Enter your withdraw amount: "))
    
    if amount > balance:
        print("Insufficiant Balance")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount

balance = 0
is_runing = True

while is_runing:
    print("---------Banking Program------------")
    print ("1.Show Balance")
    print ("2.Deposite")
    print ("3.Withdraw")
    print ("Exit")
    
    choice = input ("Enter your choice(1 to 4): ")
    
    if choice == '1':
        show_balance()
    elif choice == '2':
        balance += deposite()
    elif choice == '3':
       balance -= withdraw()
    elif choice == '4':
        is_runing = False
    else:
        print(f"{choice} is not valid")
    
print("Thank you!")