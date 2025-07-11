# Iterables  ==> An object/collection that can return its elements one at a time,allowing it to be iterated over in a loop.

# .............................
numbers = (1,2,3,6)

for number in reversed(numbers):
    print(number)

# .............................
fruits = ("Apple", "Banana", "Orange", "Coconut")

for fruit in reversed(fruits):       
    print(fruit)

# ..............................
name = "soumen Das"

for cherecter in name :
    print(cherecter, end=" ")

# .............................
my_dictionary ={"A":1, "B":2, "C":5}

for key, value in my_dictionary.items():
    print(f"{key} = {value}")