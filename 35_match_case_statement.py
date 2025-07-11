#  Match-case statement (switch) : An  alternative to using many 'elif' statements
#                                  Executive some code if value match a 'case'
#                                  Benifits : cleaner and syntex is more readable

#  Example -1 ......................

def day_of_week(day):
    match day:
        case 1:
            return "it is sunday"
        case 2:
            return "it is Monday"
        case 3:
            return "it is Tuesday"
        case 4:
            return "it is wednesday"
        case 5:
            return "it is Thursday"
        case 6:
            return "it is Friday"
        case 7:
            return "it is Saturday"
        case _:
            return "Not a valid Day"
        
print(day_of_week(10))

# Example -2........................

def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return False
        
print(is_weekend("Monday"))