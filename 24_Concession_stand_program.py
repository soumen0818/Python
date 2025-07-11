# Concession stand program 

menu = {
    "pizza": 3.50,
    "nachos":4.58,
    "fries": 2.54,
    "chips": 2.89,
    "soda": 3.00,
    "lemonade":4.55
}

cart = []
total =0

print("----------------MENU--------------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")

print("-----------------------------------")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
        
print("-----------YOUR ORDER-------------")
        
for food in cart :
    total += menu.get(food) 
    print(food, end = " ")  
    
print()
print(f"Total is : ${total:.2f}")
     