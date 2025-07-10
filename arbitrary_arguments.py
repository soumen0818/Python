# *args ==> Allows you to pass multiple non-key arguments
# **Kwargs ==> Allows you to pass multiple keyword-arguments
#              * Unpackig operator
#              1. position, 2. default, 3. keyword 4. ARBITRARY

# Example -1 ...........................
def add (*args):
    total = 0 
    for arg in args:
        total += arg
    return total

# print(add(1,2,3))

# Example -2.............................
def display_name(*args):
    for arg in args:
        print(arg, end =" ")
        
display_name("Dr.", "Soumen", "Das")



# Example of  kwargs ......................

def print_address (**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")
        
print_address(street = "123 Fake st.",
              apt = "200",
              city="Kolkata",
              state = "West Bengal",
              Zip = "721444")


# Exercise .............................

def shipping_lable(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    # for value in kwargs.values():
    #     print(value, end=" ")
    
    print(f"{kwargs.get('street')}, {kwargs.get('apt')}")
    print(f"{kwargs.get('city')}, {kwargs.get('state')}, {kwargs.get('Zip')}")
        
shipping_lable("Dr.", "Soumen", "Das",
               street = "123 Fake st.",
               apt = "@200",
               city="Kolkata",
               state = "West Bengal",
               Zip = "721444"
               )

