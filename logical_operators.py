# Logical operators = Evaluate multiple conditions (or, and, not)
#                     or => at least one condition must be True. 
#                     and => both condition must be True .
#                     not => inverts the condition (not false, not true)

# or operators .......................

# temp = 50
# is_raining = True

# if temp > 45 or temp < 0 or is_raining :
#     print("Today show is cancelled !")
# else :
#     print("Today show is scheduled")

# and & not operators.........................

is_sunny = False
temp = 30

if temp >= 28 and is_sunny :
    print("The weather is hot !🤔")
elif 28 > temp >0 and is_sunny:
    print ("The weather is warm !🤕")
elif temp >= 28 and not is_sunny :
    print("The weather is not hot !🤔")
elif 28 > temp >0 and not is_sunny:
    print ("The weather is not warm !🤕")
