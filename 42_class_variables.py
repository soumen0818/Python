# Class Variable ==> Shared among all instances of a class 
#                    Define outside the constructor 
#                    Allow you to share data among all objects ceated from that class

class student:
    class_year = 2024
    num_student = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age 
        student.num_student += 1
        
        
student1 = student("Soumen", 21)
student1 = student("suman", 20)
student1 = student("Souvik", 19)

# print(student1.name)
# print(student1.age)
# print(student1.class_year)

print(student.num_student)