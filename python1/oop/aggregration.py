#Aggregation: In aggregation, the related objects are 
#considered as parts of the main object, but they can exist 
#independently. The main object does not have a strong 
#ownership of its parts, 
#and the parts can be shared among multiple main objects.
# In code, aggregation is represented by having a reference to another class within the main class, but the related objects 
#are not necessarily created or managed by the main object.

class Student:
    def __init__(self, name):
        self.name = name

class Course:
    def __init__(self, title):
        self.title = title
        self.students = []  # Association - Course has Students

    def add_student(self, student):
        self.students.append(student)

# Creating instances
student1 = Student("Alice")
student2 = Student("Bob")

course = Course("Computer Science 101")

# Creating an association
course.add_student(student1)
course.add_student(student2)

# Navigating the association
for student in course.students:
    print(f"{student.name} is enrolled in {course.title}")

# Aggregation is a concept in which an object of one class can own or access another independent object of another class. 

#     It represents Has-A’s relationship.
#     It is a unidirectional association i.e. a one-way relationship. For example, a department can have students but vice versa is not possible and thus unidirectional in nature.
#     In Aggregation, both the entries can survive individually which means ending one entity will not affect the other entity.
