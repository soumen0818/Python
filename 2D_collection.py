groceries = [["apple", "banana", "orange", "coconut"],
             ["carrots", "potatoes", "onion"],
             ["chicken","fish"]]


# print(groceries[1])    ==> output = ['carrots', 'potatoes', 'onion']
# print(groceries[0][2])   ==> print a particular iteam at index, output = orange

for collection in groceries :
    for iteam in collection:
        print(iteam, end = ",")
    print()
       
       
       

# Exercise ===> Num_pad..............................................................

num_pad = ((7,8,9),
           (4,5,6),
           (1,2,3),
           ("+", 0, "*"))


for row in num_pad:
    for num in row :
        print(num, end = " ")
    print()