# Magic methods ==> Dunder methods (double underscore) __init__,__str__,__eq__
#                   They are automatically called by many of python's bulit -in operations.
#                   They allow developers to define or customize the behavior of objects.


class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        
    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"key '{key}' was not found"
    
book1 = Book ("The Hobbit", "j.R.R Tolkien", 310)
book2 = Book ("Harry potter", "j.k Rowling", 250)
book3 = Book ("The Lion, The witch and the wardrobe ", "c.s. Lewis", 172)

# print(book1 == book2)
print (book1['num_pages'])