# python slod machine game 
import random

def spin_row():
    symbols = ['🍒', '🍉', '🌶', '🥟', '🎇']
    
    return[random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("************")
    print(" | ".join(row))
    print("************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] =='🍒':
            return bet * 3
        if row[0] == '🍉':
            return bet * 4
        if row[0] == '🌶':
            return bet * 5
        if row[0] == '🥟':
            return bet * 10
        if row[0] == '🎇':
            return bet * 20
    return 0

def main():
    balance = 100
    
    print("*****************")
    print("Welcome to python slot game!")
    print("Symbol: 🍒 🍉 🌶 🥟 🎇")
    print("*****************")
    
    while balance > 0:
        print(f"Your current Balance is ${balance}")
        
        bet = input("Enter your Bet amount: ")
        
        if not bet.isdigit():
            print("Please enter a valid number")
            continue
        
        bet = int(bet)
        
        if bet > balance:
            print("Insufficient Balanace!")
            continue
        if bet <=0 :
            print("Bet must be greater than 0")
            continue
        
        
        balance -= bet
        
        row = spin_row()
        print("spinning..\n")
        print_row(row)
        payout = get_payout(row,bet)
        
        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("Sorry! you lost the game..")
            
        balance += payout
        
        play_again = input("Do you want to play again? (Y/N): ").upper()
        
        if play_again != 'Y':
            break
        
    print(f"Game over! Your final balance is ${balance}")
        

if __name__ == '__main__':
    main()