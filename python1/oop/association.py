#We discussed three types of 
#relationships between objects: association, composition, and
#aggregation.
#Its a relationship between two classes and 
#that relationship is established through their objects. 
#Each object has its own life cycle and there is no owner object. 
#It is a weak type of relationship. 
#It can be one-to-one, one-to-many, many-to-one, or many-to-many.

#For example students and teachers, both 
#classes are associated with each other. 
#The objects of each class 
#have their own life cycle and there is no owner.
#Association is considered a weak relationship because 
#the classes involved are not tightly coupled. Changes 
#in one class do not necessarily impact the other class.

class Student:
    def __init__(self, name):
        self.name = name

    def attend_class(self, teacher):
        print(f"{self.name} is attending {teacher}'s class.")

class Teacher:
    def __init__(self, name):
        self.name = name

    def teach_class(self, student):
        print(f"{self.name} is teaching {student.name}.")

# Creating instances
student1 = Student("Alice")
student2 = Student("Bob")
teacher1 = Teacher("Ms. Johnson")

# Establishing association
student1.attend_class(teacher1)
teacher1.teach_class(student2)
