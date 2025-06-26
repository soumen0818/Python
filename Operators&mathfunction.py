# Operators => Operators in general are used to perform operations on values and variables.

Book = 10

# Addition ...........
# Book = Book + 5
# Book += 5

# Subtraction..........
# Book = Book - 4
# Book -= 5

# Multipication.........
# Book = Book * 2
# Book *= 2

# Division..............
# Book = Book/2
# Book /= 2 

# Squar ..............(Exponentiation)
# Book = Book ** 2
# Book **= 2

# Reminder ...........(Modulus)
# Book = Book % 4
# Book %= 4

# print(Book)

# Math function .................................................


x = 2.54
y = -5
z = 6

# result = round(x)      => The round() function in Python is a built-in function used to round a number to
# a specified number of decimal places or to the nearest integer.    // output = 3

# result = abs(y)      => it is use for convert negative to positive   // output = 5

# result = pow (6, 2)   => power function  // Output = 36

# result = max (x, y, z)   => Find maximum value among the diffrent variable    //output = 6
# result = min (x, y, z)   => Find maximum value among the diffrent variable    // output = -5

# print(result) 


#...........................................................................

# import math

# x = 9.2

# print(math.pi)    => output = 3.141592653589793
# print(math.e)     => output = 2.718281828459045

# result = math.sqrt(x)   => output = 3.0 , when x=9

# result = math.ceil(x)     => Return the ceiling of x as an Integral. This is the smallest integer >= x.
# result = math.floor(x)       => Return the floor of x as an Integral. This is the largest integer <= x.




# print(result)




# Exercise.................................................

# 1. Circumference of circle .  // c = 2*pi*r

import math

radius = float (input("Enter the redius of a circle : "))

Circumference = 2 * math.pi * radius

print(f"Circumference of the circle is : { round(Circumference, 2)} cm")


