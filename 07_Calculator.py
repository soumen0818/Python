# Python calculator

# operators = input ("Enter the operator(+ * - /) : ")

# num1 = float (input ("Enter the 1st number :"))
# num2 = float (input ("Enter the 2nd number : "))

# if operators == "+" :
#     result = num1 + num2
#     print (round (result , 3))
# elif operators == "-" :
#     result = num1 - num2
#     print (round (result , 3))
# elif operators == "*" :
#     result = num1 * num2
#     print (round (result , 3))
# elif operators == "/" :
#     result = num1 / num2
#     print (round (result , 3))
# else :
#     print(f"{operators} is not valid !")   


# python weight converter ........................

weight = float(input("Enter you weight : "))

unit = input("Enter the unit (K or L) : ")


if unit == "K" :
    weight = weight * 2.205
    unit = "Lbs"
    print (f"Your weight is : {round (weight , 2)} {unit}") 
elif unit == "L" :
    weight = weight / 2.205
    unit = "Kg"
    print (f"Your weight is : {round (weight , 2)} {unit}") 
else :
    print(f"{unit} was not valid")