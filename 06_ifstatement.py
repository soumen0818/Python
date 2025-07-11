# if statement = Do some code only , if some condition is true , 
#                Else do something else


age = int (input ("Enter you age : "))

if age >= 18 :
    print("you are eligibil for vote")
elif age < 0:
    print("you are not born it !")
else :
    print("you are not eligible for vote")
    
    
# Boolean .........................

online = False

if online :
    print("User is online !")
else :
    print("user is ofline !")