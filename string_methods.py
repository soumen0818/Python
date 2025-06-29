# name = input("Enter you name : ")
phone_number = input("Enter youe phone number : ")

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
result = phone_number.replace("-", "")



print(result)