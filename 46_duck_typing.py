# Duck Typing ==> Another way to achieve polymorphism besides inheritance
#                 object must have the minimum necessary attributes/methods
#                 "if it looks like a ducks and quacks like a duck, it must be a duck".

class animal:
    alive =True
    
class Dog(animal):
    def speak(self):
        print("WOOF!")
        
class Cat(animal):
    def speak(self):
        print("MEOW!")
        
class car:
    alive = False
    def speak(self):
        print("HONK!")
        
animals = [Dog(), Cat(), car()]

for animal in animals:
    animal.speak()
    print(animal.alive)
