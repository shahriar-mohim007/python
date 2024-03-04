# #In Python, inheritance is an is-a relationship. 
# #That is, we use inheritance only 
# #if there exists an is-a relationship between two classes. 
# #For example,
# #Car is a Vehicle
# #Apple is a Fruit
# #Cat is an Animal

# #Here, Car can inherit from Vehicle, 
# #Apple can inherit from Fruit, and so on.

# class Employee:

#     raise_amt = 1.04

#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.email = first + '.' + last + '@email.com'
#         self.pay = pay

#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)

#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amt)


# class Developer(Employee):
#     raise_amt = 1.10

#     def __init__(self, first, last, pay, prog_lang):
#         super().__init__(first, last, pay)
#         self.prog_lang = prog_lang


# class Manager(Employee):

#     def __init__(self, first, last, pay, employees=None):
#         super().__init__(first, last, pay)
#         if employees is None:
#             self.employees = []
#         else:
#             self.employees = employees

#     def add_emp(self, emp):
#         if emp not in self.employees:
#             self.employees.append(emp)

#     def remove_emp(self, emp):
#         if emp in self.employees:
#             self.employees.remove(emp)

#     def print_emps(self):
#         for emp in self.employees:
#             print('-->', emp.fullname())


# dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
# dev_2 = Developer('Test', 'Employee', 60000, 'Java')

# mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

# print(mgr_1.email)

# mgr_1.add_emp(dev_2)
# mgr_1.remove_emp(dev_2)

# mgr_1.print_emps()

# #Multiple inheritence
# class Mammal:
#     def mammal_info(self):
#         print("Mammals can give direct birth.")

# class WingedAnimal:
#     def winged_animal_info(self):
#         print("Winged animals can flap.")

# class Bat(Mammal, WingedAnimal):
#     pass

# # create an object of Bat class
# b1 = Bat()

# b1.mammal_info()
# b1.winged_animal_info()

# # Multilevel Inheritance
# class SuperClass:

#     def super_method(self):
#         print("Super Class method called")

# # define class that derive from SuperClass
# class DerivedClass1(SuperClass):
#     def derived1_method(self):
#         print("Derived class 1 method called")

# # define class that derive from DerivedClass1
# class DerivedClass2(DerivedClass1):

#     def derived2_method(self):
#         print("Derived class 2 method called")

# # create an object of DerivedClass2
# d2 = DerivedClass2()

# d2.super_method()  # Output: "Super Class method called"

# d2.derived1_method()  # Output: "Derived class 1 method called"

# d2.derived2_method()  # Output: "Derived class 2 method called"

# #Method Resolution Order (MRO)
# class SuperClass1:
#     def info(self):
#         print("Super Class 1 method called")

# class SuperClass2:
#     def info(self):
#         print("Super Class 2 method called")

# class Derived(SuperClass1, SuperClass2):
#     pass

# d1 = Derived()
# d1.info()  
# #In this case, the MRO specifies that methods should be inherited from the leftmost superclass first, 
# # so info() of SuperClass1 is called rather than that of SuperClass2.
# # Output: "Super Class 1 method called"

# class Animal:
#   def __init__(self, Animal):
#     print(Animal, 'is an animal.')

# class Mammal(Animal):
#   def __init__(self, mammalName):
#     print(mammalName, 'is a warm-blooded animal.')
#     super().__init__(mammalName)
    
# class NonWingedMammal(Mammal):
#   def __init__(self, NonWingedMammal):
#     print(NonWingedMammal, "can't fly.")
#     super().__init__(NonWingedMammal)

# class NonMarineMammal(Mammal):
#   def __init__(self, NonMarineMammal):
#     print(NonMarineMammal, "can't swim.")
#     super().__init__(NonMarineMammal)

# class Dog(NonMarineMammal, NonWingedMammal):
#   def __init__(self):
#     print('Dog has 4 legs.')
#     super().__init__('Dog')
    
# d = Dog()
# print('')
# bat = NonMarineMammal('Bat')

# # Dog has 4 legs.
# # Dog can't swim.
# # Dog can't fly.
# # Dog is a warm-blooded animal.
# # Dog is an animal.

# # Bat can't swim.
# # Bat is a warm-blooded animal.
# # Bat is an animal.

#Diamond Problem
     # A
   #  / \
   # B   C
  #   \ /
  #    D
# In this hierarchy, classes B and C both inherit from 
# class A, and class D inherits from both B and C. Now, 
# if there is a method or attribute in class 
# A that is overridden in both B and C, and class 
# D does not provide its own implementation, 
# there can be ambiguity in determining which overridden 
# method or attribute should be used 
# in instances of class D. This ambiguity is the diamond problem.
class A:
    def method(self):
        print("A method")

class B(A):
    def method(self):
        print("B method")

class C(A):
    def method(self):
        print("C method")

class D(C, B):
    pass

# Creating an instance of D
obj = D()

# Calling the method
obj.method()
print(D.__mro__)

#if you run the code, it will result in an output 
#like "B method" 
#or "C method,"
#depending on the method resolution order (MRO) of the classes.
#Python uses the C3 linearization algorithm to determine the MRO.


class Contact:
    all_contacts = []

    def __init__(self, name="", email="", **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.email = email
        self.all_contacts.append(self)

class AddressHolder:
    def __init__(self, street="", city="", state="", code="", **kwargs):
        super().__init__(**kwargs)
        self.street = street
        self.city = city
        self.state = state
        self.code = code

class Friend(Contact, AddressHolder):
    def __init__(self, phone="", **kwargs):
        super().__init__(**kwargs)
        self.phone = phone


friend = Friend(name="John", email="john@example.com", street="123 Main St", city="Cityville", state="CA", code="12345", phone="555-1234")


class Car:
    # Class attribute
    wheels = 4

    def __init__(self, make, model):
        # Instance attributes
        self.make = make
        self.model = model

class ElectricCar(Car):
    # Class attribute (overriding the parent class)
    wheels = 3

    def __init__(self, make, model, battery_range):
        # Calling the parent class constructor
        super().__init__(make, model)

        # Instance attribute specific to ElectricCar
        self.battery_range = battery_range

# Creating instances of Car and ElectricCar
regular_car = Car("Toyota", "Camry")
electric_car = ElectricCar("Tesla", "Model S", 300)

# Accessing class attributes
print("Number of wheels for a regular car:", regular_car.wheels)    # Output: 4
print("Number of wheels for an electric car:", electric_car.wheels)  # Output: 3

# Accessing instance attributes
print("Make of the regular car:", regular_car.make)                  # Output: Toyota
print("Battery range of the electric car:", electric_car.battery_range)  # Output: 300


class MyClass:
    # Class attribute
    class_attribute = "Original Value"

# Accessing the class attribute using the class name
print("Class attribute value:", MyClass.class_attribute)  # Output: Original Value

# Changing the class attribute using the class name
MyClass.class_attribute = "New Value"

# Accessing the updated class attribute using the class name
print("Updated class attribute value:", MyClass.class_attribute)  # Output: New Value

# Creating instances of the class
obj1 = MyClass()
obj2 = MyClass()

# Accessing the class attribute using an instance
print("Class attribute value for obj1:", obj1.class_attribute)  # Output: New Value (updated value)

# Changing the class attribute using an instance
obj1.class_attribute = "Instance Value"

# Accessing the class attribute using an instance after modification
print("Class attribute value for obj1 after modification:", obj1.class_attribute)  # Output: Instance Value
print("Class attribute value for obj2:", obj2.class_attribute)  # Output: New Value (unchanged for obj2)

#In Python, both classmethod and staticmethod are decorators that can be used to define special types of methods within a class. Here's a breakdown of the differences between classmethod and staticmethod:
# classmethod:

#     Usage:
#         Decorated with @classmethod.
#         Takes the class itself (cls) as the first parameter.
#         Commonly used to create factory methods or methods that operate on the class and not on instances.

#     Access to Class:
#         Has access to the class itself and can modify class-level attributes.

#     Access to Instance:
#         Can access and modify class attributes, but cannot access or modify instance attributes directly.


class MyClass:
    class_attribute = "Original Value"

    @classmethod
    def modify_class_attribute(cls, new_value):
        cls.class_attribute = new_value

# Usage
MyClass.modify_class_attribute("New Value")
print(MyClass.class_attribute)  # Output: New Value


#staticmethod:

    # Usage:
    #     Decorated with @staticmethod.
    #     Takes neither the instance nor the class as the first parameter.
    #     Used for methods that don't depend on the instance or class state.

    # Access to Class:
    #     Has no access to the class itself.

    # Access to Instance:
    #     Doesn't have access to the instance and cannot modify instance attributes.

class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

# Usage
result = MathOperations.add(3, 5)
print(result)  # Output: 8

#How inheritance works with static method?

class Dates:
    def __init__(self, date):
        self.date = date
        
    def getDate(self):
        return self.date

    @staticmethod
    def toDashDate(date):
        return date.replace("/", "-")

class DatesWithSlashes(Dates):
    def getDate(self):
        return Dates.toDashDate(self.date)

date = Dates("15-12-2016")
dateFromDB = DatesWithSlashes("15/12/2016")

if(date.getDate() == dateFromDB.getDate()):
    print("Equal")
else:
    print("Unequal")

# How the class method works for the inheritance?

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def fromFathersAge(name, fatherAge, fatherPersonAgeDiff):
        return Person(name, date.today().year - fatherAge + fatherPersonAgeDiff)

    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))

class Man(Person):
    sex = 'Male'

man = Man.fromBirthYear('John', 1985)
print(isinstance(man, Man))

man1 = Man.fromFathersAge('John', 1965, 20)
print(isinstance(man1, Man))