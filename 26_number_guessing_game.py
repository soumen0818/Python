# Number Guessing Game in Python
import random

lowest_num = 10
highest_num = 100

answer = random.randint(lowest_num, highest_num)
guesses = 0
is_runing = True

print("---------Welcome to Python Number Guessing Game --------")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_runing:
    guess = input("Enter your Guesses : ")
    
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        
        if guess < lowest_num or guess > highest_num:
            print("The Number is out of range")
        elif guess < answer:
            print("Too low! Try Again")
        elif guess > answer:
            print("Too High! Try again")
        else:
            print(f"CORRECT! The answer is : {answer}")
            print(f"Number of guesses: {guesses}")
            is_runing = False
         
    else:
      print("Invalid Guess")
      print(f"Please select a number between {lowest_num} and {highest_num}")