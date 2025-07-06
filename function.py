# Function = A block of reusable code 
#            place () after the function name to invoke it.

# Example 1......................

# def happy_birthday(name, age):
#     print(f"Happy Birthday to {name}")
#     print(f"you are {age} years old !")
#     print("Happy Birthday to you 🎈!")
#     print()
    
    
# happy_birthday("Soumen", 20)
# happy_birthday("suman", 30)
# happy_birthday("Arka", 40)

# Example 2..........................

# def display_invoice(username, amount, due_date):
#     print(f"Hello {username}!")
#     print(f"Your bill of ${amount:.2f} is due : {due_date}")
    
# display_invoice("soumen", 45.254, "01/05/2025")


# Return ==> statement used to end a function and send a result back to the caller.

def create_name (first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("soumen", "das")

print(full_name)


