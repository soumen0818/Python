# collection => single "variable" used to store multiple values 
# list => [] ordered and changeable . Dublicates ok
# set => {} unordered and immutable , but add/Remove ok. No Dublicates.
# Tuple = () ordered and unchangeable . Dublicates ok . Faster

fruits = ["apple", "orange", "banana", "coconut"]

# print(dir(fruits))
# print(help(fruits))
# print (len(fruits))  => find the lenth 
# print ("Guava" in fruits)  => find the elements , if there is present or not

# fruits[0] = "Guava"  => replace the index elements


# print(fruits)   => output = ['apple', 'orange', 'banana', 'coconut']
# print (fruits[index])  => output = orange

for fruit in fruits:
    print(fruit)