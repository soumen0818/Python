# input() = A function that prompts the user to enter data 
#           Returns the entered data as a string

name = input ("What is you name ? : ")
age = int (input ("how old are you ? : ")) # This mathod is more easy and write less line code.

# age = int (age)  => This is also a method to convert datatype , using this method require extra line of code .
age = age + 2

print(f"your name is {name}")
print("Happy BirthDay !")
print(f"You are {age} year old")

#......................................................


# Exercise 1 => Rectangle area cal.
#               Area = length * width


length = float (input("Enter the length : "))
width = float (input("Enter the width : "))

Area = length *width

print(f"Area of the rectangle is: {Area}cm²")


#........................................................


# Exercise 2 => shoping cart program

item = input("What item would you like to buy? : ")
price = float(input("What is the price of the iteam?: "))
Quantity = int(input("how many would you like to buy: "))

total_price = price * Quantity

print(f"Your total bill is : ${total_price}")
