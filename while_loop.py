# while loop = execute some code while some condition remains true.

# age = int(input("Enter your age : "))

# while age < 18:
#     print("you can not drive car !")
#     age = int(input("Enter your age : "))
# else : 
#     print("you can drive the car !")



# food =input("Enter a food you like (q to quite): ")

# while not food == "q" :
#     print(f"you like {food}")
#     food =input("Enter a food you like (q to quite): ")
# else: 
#     print("Done")


num = int(input("Enter a number b/w 1-10 : "))

while num<1 or num>10 :
    print(f"your {num} is not valid !")
    num = int(input("Enter a number b/w 1-10 : "))
else:
    print(f"your number {num} is valid !")