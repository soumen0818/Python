# Module  ==> A file containing code you want to include in your program.
#             use 'import' to include a module (build in or your own)
#             useful to break up a large program reuseable separate files.

import math
# import math as  m
# from math import e

a, b, c, d, e = 1, 2, 3, 4, 5

# print(math.e ** a)
# print(math.e ** b)
# print(math.e ** c)
# print(math.e ** d)
# print(math.e ** e)


# Example .........

import ownmodule

result = ownmodule.pi
result = ownmodule.square(3)
result = ownmodule.cube(3)
result = ownmodule.circumference(3)
result = ownmodule.area(3)

print(result)