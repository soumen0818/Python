# øbject ==> A "bundle" of related attributeds (variables) and methods (functions)
#            Ex - phone, cup, Book
#            you need a "class" to create many objects

# class ==> (blueprint) used to design the structure and layout of an object.


class car :
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
        
car1 = car("model", 2025, "Blue", False)

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)