# Temprature conversion in python

temp = float(input("Enter the temperature : "))
unit = input("is the temperature in celsius or fahrenheit (c/f): ")

if unit == "c":
    temp = round ((9 * temp) /5 + 32 , 2)
    print (f"The Temperature in fahrenheit is : {temp}°F")
elif unit == "f":
    temp = round ((temp - 32) *5 / 9 , 2)
    print (f"The Temperature in fahrenheit is : {temp}°C")
else: 
    print(f"{unit} is not valid !")
