# name = input("Enter you name : ")
# phone_number = input("Enter youe phone number : ")

# result = len(name)
# result = name.find (" ")
# result = name.rfind ("n")
# result = name.capitalize()  => Return a capitalized version of the string.
#                               More specifically, make the first character have upper case and the rest lower case.

# result = name.upper()   
# result = name.lower () 
# result = name.isdigit()  =>  Return True if the string is a digit string, False otherwise.
# result = name.isalpha ()    => Return True if the string is an alphabetic string, False otherwise.

# result = phone_number.count("-")
# result = phone_number.replace("-", "")


# print(result)


# Exercise..............................
#valid user input exercise 
#1. username is no more than 12 charecters
#2. username must not contain any spaces
#3. usernamemust not contain digits

username = input ("Enter you Username : ")

if len(username) > 12 :
    print("You username can not be more than 12 cherecters")
elif not username.find(" ") == -1:
    print("Your username can not contain any spaces")
elif not username.isalpha() :
    print("Your username can not contain any numbers")
else :
    print(f"welcome {username}")