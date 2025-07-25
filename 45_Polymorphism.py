#  Polymorphism == Greek word that means to "have many forms or faces"
#                  Poly = Many
#                  Morphe = Form

#                  Two ways to achieve Polymorphism
#                 1. Inheritance == An Object could be trated of the same type as a parent class
#                 2. "Duck typing" == Object must have necessary attributes/methods

from abc import ABC, abstractmethod

class shape:
    
    @abstractmethod
    def area(self):
        pass
    
class circle(shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14*self.radius**2   
        
class square (shape):
    def __init__(self, side):
        self.side = side
        
    def area(self):
        return self.side**2
        
class Triangle (shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def area(self):
        return self.base * self.height * 0.5
        
        
shape = [circle(7), square(9), Triangle(5,3)]

for shape in shape:
    print(f"{shape.area()}cm²")
     