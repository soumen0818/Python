# Class methods ==> Allow operations related to the class itself
#                   Take (cls) as the first parameter, which represents the class itself

# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not need access to class data
# class method = Best for class-level data or require access to the class itself
 

class student:
    
    count = 0
    total_gpa = 0
    
    def __init__(self, name, gpa):
        self.name = name 
        self.gpa = gpa
        student.count += 1
        student.total_gpa += 1
        
    # INSTANCE METHOD
    def get_info(self):
        return f"{self.name} {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total no of Students: {cls.count}"
    
    @classmethod
    def get_avarage_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Avarage gpa : {cls.total_gpa / cls.count: .2f}"
    
student1 = student("suman", 8.5)
student2 = student("souvik", 8.45)
student3 = student("soumen", 8)

print(student.get_count())
print(student.get_avarage_gpa())