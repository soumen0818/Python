# shoping card program 

foods = []
prices = []
total = 0

while True:
    food =input("Enetr a food , you want to buy(q to quite) : ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)
        
print("-------YOUR CART------")

for food in foods :
    print(food, end = ",")
        
for price in prices:
    total += price
    
print()    
    
print(f"You total bill is :${total}")
        