# Dictionary ==> A collection of {key:value} pairs.
#                ordered and changeable, No duplicates


capitals ={
    "USA": "washington D.C",
    "India": "New Delhi",
    "Russia": "Moscow"
}

# print(dir(capitals))
# print (help(capitals))
# print(capitals.get("USA"))

# if capitals.get("japan"):
#     print("The capital is exist")
# else :
#     print("The capitals is not exist")


# capitals.update({"Germany": "Barlin"})    ==> Using ubdate method , we can insert a key value pair or ubdate.
# capitals.update({"India":"Kolkata"})
# capitals.pop("Russia")        ==> remove specified key and return the corresponding value.
# capitals.popitem()            ==> Remove the latest added key value
# capitals.clear()

# key = capitals.keys()     ==> Return a set-like object providing a view on the dict's keys.
# for key in capitals.keys():
#     print(key)

# values = capitals.values()   ==> Return an object providing a view on the dict's values.
# for value in capitals.values():
#     print(value)

# items = capitals.items()     ==> Return a set-like object providing a view on the dict's items.
# for key, value in capitals.items():
#     print(f"{key} : {value}")


# print(capitals)