# collection => single "variable" used to store multiple values 
# list => [] ordered and changeable . Dublicates ok
# set => {} unordered and immutable , but add/Remove ok. No Dublicates.
# Tuple = () ordered and unchangeable . Dublicates ok . Faster

# 1.list......................................................

fruits = ["apple", "orange", "banana", "coconut"]

# print(dir(fruits))
# print(help(fruits))
# print (len(fruits))  => find the lenth 
# print ("Guava" in fruits)  => find the elements , if there is present or not

# fruits[0] = "Guava"  => replace the index elements
# fruits.append("pineapple")  => Append object to the end of the list.
# fruits.remove("apple")     ==> Remove first occurrence of value.
# fruits.insert(0, "Guava")  ==> Insert object before index.
# fruits.sort()              ==> Sort the list in ascending order and return None.
# fruits.reverse()           ==> Reverse the collection
# fruits.clear()             ==> clear the hole collection of elements
# print(fruits.index("apple"))  ==> Return first index of value.
# print(fruits.count("coconut"))  ==> Return number of occurrences of value.

# print(fruits)


# print(fruits)   => output = ['apple', 'orange', 'banana', 'coconut']
# print (fruits[index])  => output = orange

# for fruit in fruits:
#     print(fruit)


# 2.Set...................................................................

fruits = {"apple", "orange", "banana", "coconut", "coconut"}

# print(dir(fruits))
# print(help(fruits))
# print (len(fruits))  => find the lenth 
# print ("Guava" in fruits)  => find the elements , if there is present or not

# fruits.add("Guava")     ==> Add an element to a set.
# fruits.remove("banana")  ==> Remove an element from a set; it must be a member.
# fruits.pop()               ==> in Python, the pop() method for sets is used to remove and return an arbitrary element from the set.
# fruits.clear()

# print(fruits)


# print(fruits)     ==> output = {'banana', 'orange', 'coconut', 'apple'} 

# for fruit in fruits:
#     print(fruit




# 2.Tuple...................................................................

fruits = ("apple", "orange", "banana", "coconut", "coconut")

# print(dir(fruits))
# print(help(fruits))
# print (len(fruits))  => find the lenth 
# print ("Guava" in fruits)  => find the elements , if there is present or not

# print(fruits.index("apple"))  ==> Return first index of value.
# print(fruits.count("coconut"))  ==> Return number of occurrences of value.

# print(fruits)

# print(fruits)      ==> output = ('apple', 'orange', 'banana', 'coconut', 'coconut')
 
for fruit in fruits:
    print(fruit)