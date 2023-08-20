"""
In Python, a hashable object is an object that has a hash value that does not change over time. This hash value is used by dictionaries to quickly look up keys. Mutable objects cannot be hashable because their values can change, which would invalidate their hash values.This means that you cannot use mutable types, such as lists, dictionaries, and sets, as dictionary keys.

Type     	Hashable
Strings      	 Yes
Numbers      	 Yes
Tuples      	 Yes
Frozensets       Yes
Lists       	 No
Dictionaries     No
Sets       	     No 
"""

"""We use the del statement to remove an element from the dictionary."""

country_capitals = {
  "United States": "Washington D.C.", 
  "Italy": "Naples" 
}

for country in country_capitals:
    print(country)
"""print only keys"""

for country in country_capitals:
    print(country_capitals[country])
"""print values"""
del country_capitals["United States"]
print(country_capitals)
"""delete a item"""


numbers = {1: "one", 2: "two"}
numbers.clear()
print(numbers)


original_marks = original_marks = {'Physics': 67, 'Maths': {'First': 1, 'second': 2, 'third': 3}}
copied_marks = original_marks.copy()
"""Shallow copy"""
copied_marks['Maths']['First'] = 90
print('Original Marks:', original_marks)
print('Copied Marks:', copied_marks)
import copy
copied_marks = copy.deepcopy(original_marks)
copied_marks['Maths']['First'] =100
"""deepcopy"""
print('Original Marks:', original_marks)
print('Copied Marks:', copied_marks)


alphabets = {'a', 'b', 'c'}
number = 1
dictionary = dict.fromkeys(alphabets, number)
print(dictionary)


scores = {
    'Physics': 67, 
    'Maths': 87,
    'History': 75
}
result = scores.get('Physics',None)
"""If key not exist it will not give keyerror"""
print(result)    


my_dict = {'a': 1, 'b': 2, 'c': 3}

for value in my_dict.values():
	print(value)

for key, value in my_dict.items():
	print(key, value)

"""The popitem() method removes and returns the (key, value) pair from the dictionary in the Last In, First Out (LIFO) order."""

person = {'name': 'Phill', 'age': 22, 'salary': 3500.0}
result = person.popitem()

print('Return Value = ', result)
print('person = ', person)

"""Nested dictionaries"""


people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

people[3] = {}

people[3]['name'] = 'Luna'
people[3]['age'] = '24'
people[3]['sex'] = 'Female'
people[3]['married'] = 'No'

print(people[3])



marks = { 'Physics': 67, 'Chemistry': 72, 'Math': 89 }

element = marks.pop('Chemistry')

print('Popped Marks:', element)

"""dictionary
comprehensions"""

squares = {number: number**2 for number in range(100)}
print(squares)