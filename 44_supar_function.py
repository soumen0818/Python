# supar()  ==> Function used in a child class to call methods from a parent class (suparclass)
#             --> Allows you to extend the functionality of the inherited methods 

class shape():
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
        
    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")
        
class circle(shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius
    def describe(self):
        print(f"It is a circle with an area of {3.14 * self.radius *self.radius} cm^2")
        super().describe()
        
class square(shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width
    def describe(self):
        print(f"It is a square with an area of {self.width*self.width} cm^2")
        super().describe()
        
class Triangle(shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height
    def describe(self):
        print(f"It is a Triangle with an area of {self.width*self.height / 2} cm^2")
        super().describe()
        
circle= circle(color="red", is_filled= True, radius=8)
square= square(color="Green", is_filled= False, width=5)
Triangle= Triangle(color="Blue", is_filled= True, width=7, height= 15)

print(circle.color)
print(circle.is_filled)
print(f"{circle.radius}cm")

Triangle.describe()