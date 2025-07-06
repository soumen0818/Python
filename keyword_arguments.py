# Keyword arguments = an argument proceded by an identifier 
#                     helps with readability
#                     orders of arguments does not matter in keyword arguments
#                     1. Position, 2. Default, 3. Keyword, 4. Arbitrary

def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last} ")
    
hello("Hello", title = "Mr.",last= "Das", first = "Soumen")