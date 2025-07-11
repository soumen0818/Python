# Membership Operators  = used to test whether the value ot variable is found in a sequence (string, list, tuple, set, or dictionary)
#                         1. in
#                         2. not in 

# Example -1............................

word = "hipopotamus"

# letter = input("Guess a letter : ")

# if letter in word:
#     print(f"{letter} was found")
# else:
#     print(f"There is no {letter letter present in word}") 

   
# if letter not in word:
#     print(f"There is no {letter} letter present in word")
# else:
#     print(f"{letter} was found")    

# Example -2............................

grades = {"soumen": "A",
            "suman":"B",
            "souvik":"C"}

student = input("Enter the student name : ")

if student in grades:
    print(f"{student}'s grade is {grades[student]}")
else:
    print(f"{student} is not found")