# List comprehensions  = A concise way to create lists in python.
#                        --> compact and easier to read then traditional loops
#                        --> **[expression for value in iterable if condition] ==> formula

doubles = [x*2 for x in range(1,11)]
triples = [y*3 for y in range(1,11)]
squares = [z*z for z in range(1,11)]

# print(squares)

fruits = ["apple", "orange", "mango", "coconut"]
fruit = [fruit.upper() for fruit in fruits]

# print(fruit)

numbers = [1,5,-7,-4,-6,9,8,12]
positive_num = [num for num in numbers if num >= 0]
even_num = [num for num in numbers if num % 2 == 0]


print(even_num)