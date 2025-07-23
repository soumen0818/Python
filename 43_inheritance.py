#  Inheritance  = Allows a class to inherit attributes and methods from another class 
#                 Help with code reusibility and extensibility
#                 class ==>  child(parent)

class animal:
    def __init__(self, name):
        self.name = name 
        self.is_alive = True
        
    def eat(self):
        print(f"{self.name} is eating")
        
    def sleep(self):
        print(f"{self.name} is sleeping")
        
class Dog(animal):
    def speak(self):
        print(f"{self.name} says Woof!")
class cat(animal):
    def speak(self):
        print(f"{self.name} says Meow!")
class mouse(animal):
    def speak(self):
        print(f"{self.name} says Squeak!")

Dog = Dog("Scooby")
cat = cat("Garfield")
mouse = mouse("Mickey")

# print(Dog.name)
# print(Dog.is_alive)
# Dog.eat()
# Dog.sleep()

cat.speak()
