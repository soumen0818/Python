groceries = [["apple", "banana", "orange", "coconut"],
             ["carrots", "potatoes", "onion"],
             ["chicken","fish"]]


# print(groceries[1])    ==> output = ['carrots', 'potatoes', 'onion']
# print(groceries[0][2])   ==> print a particular iteam at index, output = orange

for collection in groceries :
    for iteam in collection:
        print(iteam, end = ",")
    print()
       