# Keyword arguments = an argument proceded by an identifier 
#                     helps with readability
#                     orders of arguments does not matter in keyword arguments
#                     1. Position, 2. Default, 3. Keyword, 4. Arbitrary

def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last} ")
    
hello("Hello", title = "Mr.",last= "Das", first = "Soumen")


# Exercise....................

def get_phone (country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=91, area=923, first=994,last=2624)
print(phone_num)