# Static methods == A method that belong to a class rather than any object from that class(instance) usually used for general utility functions.
# Instance Methods ==> Best for operations on instances of the class(objects)
# Static Methods ==> Best for Utility functions that do not need access to class data

class Employee:
    
    def __init__(self, name, position):
        self.name = name 
        self.position = position
        
    def get_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_position = ["manager", "Cashier", "cooker"]
        return position in valid_position
    
employee1 = Employee("soumen", "manager")    
employee2 = Employee("suman", "cashier")    

print(Employee.is_valid_position("manager"))
print(employee1.get_info())
print(employee2.get_info())