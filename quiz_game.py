# Python Quiz Game

Questions = (("How many elements are present in the periodic table? "),
             ("Which animal lays the largest eggs? "),
             ("How many bons are presents in human body? "),
             ("which planet solar system is the hottest? "))

options = (("A.116","B.117","C.118","D.119"),
           ("A.whale","B.crocodile","C.Elephant","D.ostrich"),
           ("A.206","B.207","C.208","D.209"),
           ("A.Mercury","B.Venus","C.Earth","D.Mers"))

answers = (("C", "D", "A", "B"))
guesses = []
score = 0
question_num = 0

for question in Questions:
    print("------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
        
    guess = input("Enter the answer (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer.")
    question_num += 1
    
    
print("------------------------------------")
print("            Result              ")
print("------------------------------------")

print ("Answer: ", end = "")
for answer in answers :
    print(answer, end = " ")
print()

print ("Guesses: ", end = "")
for guess in guesses :
    print(guess, end = " ")
print()

score  = int(score / len(Questions) * 100)
print(f"Your score is : {score}%")