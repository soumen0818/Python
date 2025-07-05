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

    