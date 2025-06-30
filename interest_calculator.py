principle = 0
rate = 0
time = 0

# while principle <= 0:
#     principle = float(input("Enter the primciple amount : "))
#     if principle <=0 :
#         print("principle can not be less than or equal to zero !")
# while rate <= 0:
#     rate = float(input("Enter the rate of interest: "))
#     if rate <=0 :
#         print("rate can not be less than or equal to zero !")
# while time <= 0:
#     time = float(input("Enter the time in year : "))
#     if time <=0 :
#         print("time can not be less than or equal to zero !")
        

# print(principle)
# print(rate)
# print(time)

# total= principle * pow((1+rate/100),time)
# print(f"Balance after interest is : ${total :.2f}")



# 2nd method................


while True:
    principle = float(input("Enter the primciple amount : "))
    if principle <0 :
        print("principle can not be less than or equal to zero !")
    else:
        break
while True:
    rate = float(input("Enter the rate of interest: "))
    if rate <0 :
        print("rate can not be less than or equal to zero !")
    else:
        break
while True:
    time = float(input("Enter the time in year : "))
    if time <0 :
        print("time can not be less than or equal to zero !")
    else:
        break

print(principle)
print(rate)
print(time)

total= principle * pow((1+rate/100),time)
print(f"Balance after interest is : ${total :.2f}")