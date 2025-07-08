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

print(add(1,2,3))

# Example -2.............................
def display_name(*args):
    for arg in args:
        print(arg, end =" ")
        
display_name("Dr.", "Soumen", "Das")