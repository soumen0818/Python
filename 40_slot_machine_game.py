# python slod machine game 
import random

def spin_row():
    pass

def print_row():
    pass

def get_payout():
    pass

def main():
    balance = 100
    
    print("*****************")
    print("Welcome to python slot game!")
    print("Symbol: 🍒 🍉 🌶 🥟 🎇")
    print("*****************")
    
    while balance > 0:
        print(f"Your current Balance is ${balance}")
        
        bet = int(input("Enter your Bet amount: "))
        
        if not bet.isdigit():
            print("Please enter a valid number")
            continue
        if bet > balance:
            print("Insufficient Balanace!")
            continue
        if bet <=0 :
            print("Bet must be greater than 0")
            continue
        
        balance -= bet
        


if __name__ == '__main__':
    main()