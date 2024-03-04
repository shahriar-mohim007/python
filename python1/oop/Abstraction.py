from abc import ABC, abstractmethod

class Duck(ABC):
    @abstractmethod
    def quack(self):
        pass

class RobotDuck(Duck):
    def quack(self):
        print("Beep beep quack")

# Trying to create an instance of Duck (an ABC) without implementing quack will raise an error
# duck_instance = Duck()  # Raises TypeError


#Abstraction is a fundamental concept in object-oriented programming (OOP) languages like Java and C++. It refers to the process of hiding the complex implementation details of an object and exposing only the essential features or functionalities. Abstraction allows developers to focus on the high-level structure of a system without worrying about the intricate details.

#While duck typing is flexible, it can be challenging to ensure that a class adheres to a specific protocol or interface. This is where Abstract Base Classes (ABCs) come into play. ABCs allow you to define a set of methods and properties that must be implemented by any class that wants to be considered an instance of that class.

# Creating an instance of RobotDuck, which implements the required quack method
robot_duck_instance = RobotDuck()
robot_duck_instance.quack()  # Outputs: Beep beep quack

# In Python's standard library, abstract base classes (ABCs) are used to define common interfaces for various types of objects. These interfaces help ensure that different classes, which may have different implementations, adhere to a set of conventions or provide specific functionality. The collections module is a good example of this usage.

# Container:

#     The Container abstract base class in the collections module defines an interface for objects that support the in membership test (x in container).
#     Any class that wants to be considered a container needs to implement the __contains__ method. By doing so, it can be used in constructs like element in container.
#     Example:

from collections.abc import Container

class MyContainer(Container):
    def __contains__(self, item):
        # Implement the membership test logic
        return item % 2 == 0

my_container = MyContainer()
print(2 in my_container)  # Outputs: True


# Iterable:

#     The Iterable abstract base class defines an interface for objects that can be iterated over using a for loop (for element in iterable).
#     Classes that want to be considered iterable need to implement the __iter__ method.
#     Example:

from collections.abc import Iterable

class MyIterable(Iterable):
    def __iter__(self):
        # Implement the iteration logic
        return iter([1, 2, 3])

my_iterable = MyIterable()
for element in my_iterable:
    print(element)


# Hashable:

#     The Hashable abstract base class defines an interface for objects that can be used as keys in a dictionary (dict).
#     Classes that want to be considered hashable need to implement the __hash__ method.
#     Example:

from collections.abc import Hashable

class MyHashable(Hashable):
    def __hash__(self):
        # Implement the hash function
        return hash("example")

my_hashable = MyHashable()
my_dict = {my_hashable: "value"}


# By providing these abstract base classes, the collections module sets clear expectations for how certain types of objects should behave. This allows for consistency and interoperability across different parts of the Python standard library and other third-party libraries. It also makes it easier for developers to understand how to use and extend these classes in their own code, promoting good software design practices.

# Python introduced abstract base classes (ABCs) as a mechanism to facilitate abstract programming and interface design. The main motivations behind introducing abstract classes in Python include:

#     Interface Specification:
#         Abstract base classes allow developers to define and specify interfaces without necessarily providing a full implementation. This is particularly useful when you want to ensure that certain methods are present in all subclasses but don't want to dictate the exact implementation.

#     Enforcement of Method Implementation:
#         ABCs can include abstract methods that must be implemented by concrete subclasses. This helps ensure that specific methods, representing an expected interface, are present in derived classes.

#     Contractual Agreements:
#         ABCs serve as a form of a contractual agreement between the class designer and the class user. When a class inherits from an abstract class, it implicitly agrees to provide implementations for the methods specified by the abstract class.

#     Readability and Documentation:
#         Abstract classes make code more readable and act as a form of documentation. By using ABCs, you can clearly express the expected interface and behavior of a class, making it easier for other developers to understand and use your code.

#     Runtime Type Checking:
#         Python's abc module provides mechanisms to check for abstractness at runtime. This means that attempting to create an instance of a class that hasn't implemented all the abstract methods specified by its abstract base class will result in a TypeError. This helps catch potential errors early in the development process.

#     Consistent Design Patterns:
#         Abstract classes are commonly used in design patterns that involve defining interfaces. For example, the Template Method Pattern often uses abstract classes to define the structure of an algorithm, allowing subclasses to provide specific implementations for certain steps.

#     Integration with Standard Libraries:
#         Python's standard library uses abstract classes extensively. For instance, the collections module includes abstract base classes like Container, Iterable, and Hashable to define common interfaces for various container types.

#     Compatibility with Duck Typing:
#         While Python is a dynamically-typed language with strong support for duck typing, abstract classes provide a way to blend dynamic typing with more explicit interface specifications. This allows developers to enjoy the flexibility of duck typing while still having some level of structure and contract.