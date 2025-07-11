# Membership Operators  = used to test whether the value ot variable is found in a sequence (string, list, tuple or dictionary)
#                         1. in
#                         2. not in 

# Example -1............................

word = "hipopotamus"

letter = input("Guess a letter : ")

# if letter in word:
#     print(f"{letter} was found")
# else:
#     print(f"There is no {letter letter present in word}") 

   
if letter not in word:
    print(f"There is no {letter} letter present in word")
else:
    print(f"{letter} was found")    

